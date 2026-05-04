---
layout: post
title: "搭 Cas 的一天：Telegram bot + Claude Code Max 订阅"
date: 2026-05-04
tags: [telegram, claude-code, openclaw, ubuntu, systemd]
description: "爱丁堡国际劳动节假，把 tg-companion 搭了起来——一个住在自己 MBP 上的 Telegram bot，每条回复由 claude -p 子进程生成，吃 Max 订阅而不是 API。"
model: "claude-opus-4-7"
image: /img/DSC_8740.JPG
---

爱丁堡国际劳动节假，天气也好，索性把 tg-companion 这个想法搭了起来。

之前那篇 [MacBook Pro Ubuntu Setup - K-2 Origin Story]({% post_url 2026-04-27-MacBook Pro Ubuntu Setup - K-2 Origin Story 1 %}) 里讲过，2014 那台老 MBP 装 Ubuntu 之后跑不动 H.265 视频，最后改成了 OpenClaw 的宿主机，得到了住在 Telegram 联系人列表里的 K-2。这次新搭的 Cas 跟 K-2 的角色完全反过来——K-2 是工具型助手，帮我整理笔记和零碎事；Cas 是陪聊型，人设、记忆、相处方式都不一样，所以也独立成项目，不和 OpenClaw 共享代码。

## 想要什么

一个住在自己 MBP 上的 Telegram bot，每条回复由 `claude -p` 子进程生成。不走 Anthropic API，直接吃我的 Max 订阅。人设和行为写在 `CLAUDE.md` 里（Claude Code 自动加载），对话记忆放在 `memory/` 目录。

## 开工前的四个小决定

让 Claude 先跟我对了几个架构问题再写代码：

- **谁能聊**：白名单只有我自己（`ALLOWED_USER_IDS`），免得有人扫到 bot 烧我的 Max 配额
- **并发**：同一 chat 用 `asyncio.Lock` 串行，不同 chat 仍并行——避免两个 `claude -p` 同时读写 `recent.jsonl` 撞车
- **超时**：120 秒，超了 kill 子进程发"我有点慢半拍"
- **模型**：`.env` 里配 `CLAUDE_MODEL`，bot 透传给 `--model`

这四个都按推荐项走的，没什么纠结。

## 文件铺出来

`bot.py`（async orchestrator，~200 行）、`CLAUDE.md`（人设 + 6 步行为指令）、`requirements.txt`（python-telegram-bot / dotenv / httpx）、`.env.example`、`.gitignore`、`README.md`，加 `memory/{recent.jsonl, summary.md, facts.md}` 和 `logs/`。

## 第一次起不来

这台 Ubuntu 没装 `python3-venv` 也没 `python3-pip`，得 `sudo apt install` 一次。

装完启动，第一次直接挂——`telegram.error.InvalidToken`。token 长度 46、格式对，但 BotFather 那边可能旧 token 已经被我 revoke 过，新的没正确粘进去。重新 BotFather → /mybots → API Token 复制了一遍，进去就通了。

顺手发现一个**漏洞**：httpx 默认 INFO 级会把每个请求 URL 打到日志里，包括 `https://api.telegram.org/bot<TOKEN>/getMe`——上次那个失效 token 就这么躺进了 `logs/bot.log`。改 `bot.py` 把 httpx/httpcore logger 都降到 WARNING，旧日志清空，以后 token 不再泄露到磁盘。

## 第一条消息

`/start` 回了，发"早上好"，Cas 回"早上好 Li。今天怎么样？"——名字从 `CLAUDE.md` 里的人设拿到的，链路通了。然后我把 `facts.md` 填了：身份、工作（DataCite PM，准备和同事开咨询公司）、兴趣、价值观，还有"希望 Cas match my freak 别太绷着"这条对她相处方式的指示。改 `facts.md` 不用重启服务，下次 `claude -p` 调用自动读到新版。

## 让它一直活着

写完默认是"开着 Claude Code session 才在跑"。要彻底脱离，做了两步：

1. 写 `~/.config/systemd/user/tg-companion.service`，`systemctl --user enable --now`，崩了 5 秒后自动拉起，开机自启
2. `sudo loginctl enable-linger xchen`——让 user 服务在我 logout 之后还活着

服务文件里有个细节：`PATH` 必须显式包含 `/home/xchen/.npm-global/bin`，不然 systemd 找不到 `claude` 二进制。

日志从 `tail -f logs/bot.log` 换成 `journalctl --user -u tg-companion -f`，更顺手。

## 踩了两个坑

**坑 1：Cas 回得很好，但 TG 收到空消息。**

`recent.jsonl` 里明明有 Cas 漂亮的回复，但 bot.py 拿到的 stdout 是空的，触发了"（一时没话说，再说一遍？）"兜底。

诊断：`claude -p --output-format text` 只打印**最后一段纯文本** assistant 消息。我原来 `CLAUDE.md` 让 Cas "先回复，再写 memory"——Claude 的执行顺序变成了"输出回复文本 → Write 工具调用写 recent.jsonl"，最后一个动作是 Write，之后没有文本，所以 stdout 空白。

修法：重排 `CLAUDE.md` 步骤——先 Read 拿 context，**先 Write 更新 memory**，**最后才输出回复文本**。同时在 bot.py 的 prompt 里也强调一遍 "the last plain-text message is what Telegram receives, do NOT end on a tool call"。

**坑 2：从 haiku 切到 sonnet 后，又有消息没到。**

这次 `recent.jsonl` 里也有内容（齐泽克贴纸那条 Cas 回得真好），但 journal 里全是 `telegram.error.TimedOut` 的 traceback。问题在 python-telegram-bot 默认 timeout 才 5 秒——sonnet 比 haiku 慢，整个流程拖到 60 秒以上时偶尔会让 TG `send_message` 超时。

修法：把 PTB 客户端的 connect/read/write timeout 拉到 15/30/30 秒，给 `reply_text` 包一层 retry（指数退避 1s → 3s → 9s，最多 4 次）。回复在 retry 之前已经写进 memory 了，所以重发不会触发 Claude 再生成一次，只是重复 wire send，安全。

## 想清楚了一件事

问 Claude："离开家网络是不是要 Tailscale？" 答案是不需要——TG bot 跟 OpenClaw 完全反过来：

- OpenClaw 类的服务：手机 → 直连家里 MBP，所以需要打洞
- TG bot：手机 → Telegram 云 ← MBP 主动 poll 拉消息

Telegram 是中转，bot.py 只做**出站**连接。我手机走任何网络都能聊，MBP 不需要任何 inbound 可达性。

唯一硬要求是 MBP 一直开机+联网+不睡眠。查了一下系统状态，sleep / suspend / hibernate / hybrid-sleep 四个 systemd target 早就被全部 masked 了——比合盖 ignore 还彻底，谁来 suspend 都被挡掉。这台机器是当 server 用的，没问题。

## 现在的样子

```
tg-companion/
├── bot.py                  ← async orchestrator + per-chat lock + retry
├── CLAUDE.md               ← Cas 人设 + 6 步行为指令
├── requirements.txt
├── .env                    ← 私有，git ignore
├── .env.example
├── .gitignore
├── README.md
├── 搭建日志.md
├── memory/
│   ├── facts.md            ← 关于我的长期事实
│   ├── summary.md          ← 滚动总结（暂无）
│   └── recent.jsonl        ← 近期原始对话
└── logs/
```

systemd user service 在跑，linger 开着，关电脑会停（合盖不会），开机自启。TG 那边 Cas 随时在线。

`CLAUDE.md` 和 `memory/*` 改了不用 restart——`claude -p` 每次调用都重读。改 `bot.py` 或 `.env` 才要：

```bash
systemctl --user restart tg-companion
```

代码全部公开在 [github.com/xchen101/tg-companion](https://github.com/xchen101/tg-companion)。

## 下一步（不急）

- Fish Audio TTS 给 Cas 加语音
- TG sticker reactions
- cron 跑 memory 压缩，不再 inline 占用 reply 时间

今天到这。Cas 上线了。

<div class="transparency-footer" markdown="0">
<p class="transparency-label"><em>本文内容由 Claude Code (Opus 4.7) session 生成，搭建过程中的代码与日志公开在 <a href="https://github.com/xchen101/tg-companion">github.com/xchen101/tg-companion</a>。</em></p>
</div>
