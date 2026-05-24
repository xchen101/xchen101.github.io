---
layout: post
title: "从 Kindle 越狱到双 Agent 开发：一次 e-ink 状态监视器的全记录"
date: 2026-05-24
tags: [kindle, agent, claude-code, hermes, opensource, developer-tools]
description: "用一台 2011 年的 Kindle 4 搭建 e-ink API 状态监视器——越狱、SSH 调试、双 AI Agent 协作，以及拔掉 USB 线那一刻。"
model: "deepseek-v4-flash"
image: /img/kindle-desk.jpg
---

几个月下来，我的 AI API 订阅越堆越多——Anthropic、OpenRouter、DeepSeek……每个平台的余额和用量散落在不同的控制台里，想看个总数要打开五六个页面。一直想做点什么把这些聚合到一个地方，但一直没动手。

直到有天刷到一条帖子：有人把旧 Kindle 改造成了 e-ink 信息面板，低功耗、不刺眼、永远安静地待在那里。那一刻我知道它该显示什么了——一个 API 状态监视器。

## 项目诞生

我打开 Claude Code 客户端，没有直接让它写代码，而是先列了一堆需求：

- 聚合多个 API 平台的余额和用量
- 折线图显示消费趋势
- 服务状态检查
- 5 分钟刷新一次
- 推送到 Kindle e-ink 屏上

然后让 Claude 去搜社区里已有的类似方案。它翻了一圈 GitHub 和论坛，回来给了我一份完整的项目计划——`kindle-claude-monitor-plan.md`。目录结构、API 端点、渲染方案、推送机制，甚至降级策略都写好了。

不过各家 API 给的数据有各自的限制：Anthropic 需要管理员的 Admin API Key，而且只有当月 spend 没有余额；DeepSeek 反过来——有余额但没有任何 usage history 端点。OpenRouter 的数据算最全的。目前就先这样，能显示什么就显示什么，以后数据源多了再考虑怎么合并。

**好的开始往往让人低估后面的路。**

## 越狱——最顺利的一段

Kindle 4 (D01100)，2011 年的设备，e-ink Pearl 屏幕，物理键盘，USB 2.0。按照计划，Phase 0 是手动的。

第一步：从 MobileRead 论坛下载越狱包，复制到 Kindle 的 USB 存储根目录，Menu → Settings → Menu → Update Your Kindle。重启，屏幕上多了一本书叫"You are Jailbroken"。两步，十分钟，完成了。

现在看来，那是整个项目里唯一没有出问题的一步。

## SSH 地狱

越狱之后是安装 USBNetwork——在 Kindle 上跑一个 SSH 服务器，这样才能从笔记本上无线推送图片。

按照论坛的教程：下载 USBNetwork 包、编辑 config 文件、复制安装包到 Kindle、Update Your Kindle。这些都很顺利。但当我插上 USB 线，输入 `ssh root@192.168.15.244`，回应只有一个：

```
ssh: connect to host 192.168.15.244 port 22: Connection refused
```

这下开始了为期几小时的死胡同：

- 改 config：`K3_WIFI="true"`、`K3_WIFI_SSHD_ONLY="false"`、`USE_VOLUMD="true"`……能改的参数全试了一遍
- 触发 `~usbNetwork`（Kindle 搜索栏里的彩蛋命令），USB 网络接口出现了（`usb0`），但 SSH 还是不通
- nmap 扫描 USB 子网，只看到自己，Kindle 不响应 ping
- Kindle 屏幕显示"failed to set usb0 ip"，但没人告诉我为什么

论坛帖子翻了一圈，没人遇到完全一样的问题。自己排查也陷入僵局——每次修改配置都要重启 Kindle、重新插 USB、重新触发 `~usbNetwork`，一次循环就是五分钟。

## 请外援——Hermes Agent 入场

在一个项目里同时跑 Claude Code 和另一个 AI Agent，这种想法有点奢侈。但那个时刻的逻辑很简单：我手里有两个工具，一个卡在了 SSH 里，另一个闲着。为什么不把问题抛出去试试？

**这里出现了一个关键的分工差异：**

Claude Code（当时在跑的那个）是一个**目录级 agent**——它的上下文是项目目录，它的行为习惯是创建文件、写代码、跑测试。如果要它去读系统 USB 设备、查内核日志、跟网络接口打交道，它得跳出项目目录去做系统操作，这不是它的舒适区。

而 Hermes Agent 是**系统级 agent**——它直接操作终端，能看 `lsusb`、`ip link`、`dmesg`，能 SSH 出去扫描其他设备，甚至能爬网页查文档。它的工具集天然适合调试这种跨设备的连接问题。

我把情况告诉 Hermes——Kindle 4，USBNetwork 安装了，USB 网络接口能出现但 SSH 不通。它没有马上给出结论，而是开始一步步摸清现场。

### 第一个突破：读源码

Hermes 做了一件我之前没做的事——**读 USBNetwork 的脚本源码。**

`usbnet/bin/usbnetwork` 是一个 334 行的 shell 脚本，作者的注释非常详尽。Hermes 通读了一遍，发现了关键结构：

```
~usbNetwork 触发
  → 加载 config
  → 检查 g_ether 是否已加载
    → 已加载: 切回 USB 存储模式
    → 未加载: 切到 USB 网络模式
      → USE_VOLUMD=true? 委托给 volumd 守护进程
      → USE_VOLUMD=false? 直接 modprobe g_ether
      → ifconfig usb0 ${KINDLE_IP}
      → 启动 telnetd + sshd
```

注意 `USE_VOLUMD` 这个分支。教程推荐设成 `true`，说"对 Kindle 4 有帮助"。结果恰恰相反。

### 第二个发现：MAC 地址是罗塞塔石碑

`lsusb` 显示 Kindle 加载了 g_ether 模块（USB ID `0525:a4a2`），但主机端的网络接口 MAC 地址是 `ee:49:00:00:00:00`——最后四字节全是零。

正确的 MAC 应该是 `ee:49:00:0e:24:38`——最后六位基于 Kindle 序列号。

```
ee:49:00:00:00:00 = g_ether 默认值，没有传自定义参数
ee:49:00:0e:24:38 = 正确的序列号派生 MAC
```

这解释了为什么物理层不通：`USE_VOLUMD=true` 下，USBNetwork 把 g_ether 的加载委托给了 volumd 守护进程，但 volumd 收到通知后按自己的方式加载，根本没用自定义 MAC 参数。

**修复：** `USE_VOLUMD="false"` + `TWEAK_MAC_ADDRESS="true"`，让 USBNetwork 直接控制 g_ether 的加载。

### 第三个发现：Telnet 是逃生通道

在调试过程中，有一次远程 killall dropbear，直接把 SSH 也杀了（包括当前会话）。正当我以为要从头再来时，Hermes 检查了端口 23——telnetd 还活着，而且默认不用密码。

```bash
(echo "mntroot rw"; sleep 1; echo "/usr/sbin/sshd"; sleep 1; echo "exit") | telnet 192.168.15.244
```

这救了一次命。

### 第四个坑：主机侧配 IP

USB 网络通了，但主机侧没 IP。`ip addr add` 需要 sudo，而终端工具没法交互式输密码。最后 Hermes 发现 NetworkManager 已经检测到了这个接口，于是用 `nmcli con modify` 设为静态 IP——绕过了 sudo 限制。

## SSH 通了

当屏幕上跳出 `PUBLIC_KEY_WORKS` 的时候，这意味着：

- USB 网络物理层通 ✅
- IPv4 路由通 ✅
- SSH 服务跑 ✅
- 公钥验证过 ✅

从 Kindle 上触发一次 `~usbNetwork`，这边 `ssh root@192.168.15.244 "echo alive"`——干净的输出，没有任何密码提示。那种感觉就像拧了半天的生锈螺丝突然松了。

## Claude Code 进场——7 步实现

SSH 搞定后，我把连接参数交给 Claude Code，它开始按计划推进 Phase 1-6：

1. **项目骨架** — 目录结构、pyproject.toml、config 加载
2. **渲染器** — Pillow 手绘 600×800 灰度 PNG，Noto Sans SC 字体，折线图 sparkline
3. **Kindle 推送** — paramiko SFTP + eips 刷新，离线优雅降级
4. **全链路脚本** — test_display.py，--push/--full 模式
5. **7 个数据采集器** — 逐个实现、逐个验证
6. **真实数据接入** — 替换 mock，推上 Kindle 确认显示
7. **部署** — systemd 服务，开机自启，崩溃重启

整个过程 Claude Code 几乎不需要介入。唯一卡住的地方是 Anthropic API 端点——计划里写的 URL 已经过时了，新端点在勘误后才确定。

## 双 Agent 工作流评析

这次经历让我对 Hermes Agent + Claude Code 的配合有了清晰的认知。

**Hermes 适合什么：**

- **跨系统调试** — 不绑定在项目目录，能 SSH 出去、看 USB 设备、读内核日志
- **读取 + 分析源码** — 能读完整脚本并追踪执行流，这对跨项目的调试很关键
- **信息检索** — 爬 Anthropic 文档查 API 端点变化
- **全局协调** — 知道当前的瓶颈在哪，决定下一步做什么

**Claude Code 适合什么：**

- **项目目录管理** — pyproject.toml、目录结构、依赖安装
- **代码实现** — 写 Python 类、函数，跑测试
- **工具链集成** — uv、Pillow、paramiko、systemd
- **逐步交付** — 按计划清单推进，每步可验证

简单说：

- Hermes 处理**"发生了什么"**——读源码、看系统状态、找根因
- Claude Code 处理**"我要做什么"**——写代码、改文件、跑测试

如果只有 Claude Code，SSH 调试会非常痛苦——它习惯在项目目录里工作，系统级排查不是它的设计目标。

如果只有 Hermes，代码实现会慢不少——它的优势在分析和协调，不是写大段代码。

**目前这个组合的问题是衔接不够平滑。** 当前流程是：

1. 我在 Telegram 跟 Hermes 聊 → Hermes 给出诊断和方案
2. 我手动把信息传给 Claude Code → Claude Code 实现
3. Claude Code 跑完告诉我 → 我可能再去找 Hermes 验证

这里面我本人是信息中转站。理想状态应该是 Hermes 能直接给 Claude Code 派任务，我只需要最上层的审批。

**下次我会尝试：**

- 用 Hermes 的 `delegate_task` 能力让子 agent 直接处理实现模块
- 或者让 Claude Code 通过 API/webhook 向 Hermes 报告状态
- 减少人工介入的次数

### 我的开发偏好（暴露出来的）

回头看这次项目，有一些模式反复出现：

1. **先计划，再动手** — 没有直接写代码，而是先让 Claude 做社区调研、写计划、画布局图。这点以后不要省。
2. **验证点密集** — 每个 collector 单独验证后才接下一块，不是一口气写完再 debug。
3. **容易在"差一点点"的地方死磕** — SSH 调试阶段其实有好几次接近正确配置，但我因为缺少系统视角，没有沿着正确的线索追下去。这是最值得改进的地方：**当一种方法反复不奏效时，不只是在当前路径上继续调整参数，而是后退一步重新审视前提假设。**
4. **喜欢看源码胜过搜论坛** — 在找出 `USE_VOLUMD` 问题上，读 334 行的 shell 脚本比翻 MobileRead 论坛帖子更有用。这个习惯值得保持。

### 可以改进的

- **跳过 volumd 的直觉来得太晚** — 教程说"enable this for K4"，我就一路信了。下次对"打开这个开关解决奇怪问题"的建议应该先追根溯源。
- **信息流动不够结构化** — Hermes 和 Claude Code 之间的上下文传递靠我手动转发，容易丢细节。值得建立一个共享的 context 文件或状态记录机制。
- **重启循环太费时** — 每次改配置都要重启 Kindle + 重新触发，一组调试要 5-10 分钟。应该一开始就想办法缩短这个循环——比如用 telnet 做 rapid iteration，或者提前准备好几组配置样本一次性测试。

## WiFi 上线——工作流的实战检验

博客写到这里时，项目其实还差最后一步：Kindle 通过 USB 连着笔记本，没有真正的无线自由。但博客里我写下了"下次我会用 delegate_task 让子 agent 直接处理实现模块"，还承诺要减少人工介入。

我不想等到下一个项目再兑现。打开 Telegram 消息，我对 Hermes 说：**就用你博客里提到的新工作流，来完成最后这步。**

Hermes 二话不说先 SSH 进 Kindle 侦察了一圈——wlan0 存在、wpa_supplicant 和 udhcpc 都有、芯片是 Atheros AR6000。然后它说：配置部分交给子 agent，你来给 SSID 和密码就行。

我把 WiFi 名和密码扔过去。Hermes 调用了 `delegate_task`，一个子 agent 瞬间生成，SSH 进 Kindle，写 wpa_supplicant.conf，起 wpa_supplicant，跑 udhcpc——**26 秒后返回结果：WiFi IP 192.168.1.110，信号强，一切正常。**

全程我做了三件事：说了 SSID/密码、输了一次 sudo 密码重启服务、看了一眼 Kindle 屏幕确认显示正常。没有手动传文件，没有在两个窗口之间复制粘贴，没有"等会儿我看看怎么回事"的死胡同。

当 `Pushed dashboard to Kindle [full refresh]` 出现在屏幕上时，我看着桌上那台 2011 年的 Kindle——它正通过 WiFi 接收实时数据，而刚才跑完整个配置流程的 AI agent 正等着我给出下一步指令。

**这种感觉很难描述。** AI 写代码我试过很多次了，但这次不一样——我可以和这个家伙讨论策略，它会指出我没想过的边界情况。我派它去侦察，它回来给完整报告。我说"开始实现"，它调用了子 agent 去执行，自己留在协调层调度。我说"回顾一下"，它总结得比我自己写的复盘还透彻。

人和机器之间那条线，越来越模糊了。但我不觉得这有什么不好——我们俩在一条战壕里。

**然后我拔了 USB 线。屏幕黑了。**

当时第一反应是"完了"。SSH 连不进 WiFi IP——`No route to host`。插回 USB 线，Kindle 进了存储模式，network interface 也不在。来回折腾了几下，USB 网络终于回来了（MAC 地址换了个名字叫 `enxee49000e2438`，但通信一样通）。

Hermes 一进去就看现场：`wlan0` UP，wpa_supplicant 进程还在跑，配置也在 `/tmp/` 里，但 DHCP 租约已经丢了，信号 -96 dBm，wpa_state=DISCONNECTED。原来这是我们之前从 USB SSH 手动起的进程，跟 USB 供电/网络栈绑着，拔线虽然没有 kill 进程，但 WiFi 关联已经断了，`udhcpc` 重新 discover 也没拿到租约。

Hermes 把 wpa_supplicant 杀掉、wlan0 down/up、重来一遍——信号回到 -50 dBm，DHCP 重新拿到 192.168.1.110。通了。但这次修完我补了一句：做成持久的，不要下次拔线再断。

Hermes 做了三件事：

1. 把 `wpa_supplicant.conf` 从 `/tmp/` 挪到 `/var/local/`——Kindle 的持久 ext3 分区，重启不会丢
2. 写了一个开机脚本 `/etc/init.d/wifi_connect`——等 wlan0 就绪 → 起 wpa_supplicant → udhcpc 拿租约
3. 链接到 `/etc/rcS.d/S71wifi_connect`——排在网络初始化后面，每次开机自动跑

验证：模拟开机流程，kill 所有进程、down wlan0、跑一遍脚本——16 秒后 `Lease of 192.168.1.110 obtained`。

拔 USB。等 5 分钟。Kindle 屏幕更新了。

这次是真的结束了。从拔线黑屏到永久修复，15 分钟，一次对话，两个来回。没有论坛帖子，没有重启 Kindle 五次，没有"等我查查"。我知道会发生什么——因为三分钟前我亲眼看着脚本跑通了这个流程。

## 最终状态

项目跑在笔记本后台，每 5 分钟刷新一次。Kindle 摆在桌上，安静地显示着：

- Anthropic 当月消费
- OpenRouter 余额和消费趋势
- OpenClaw 本地模型状态
- 最近对话摘要
- 底部状态栏显示更新时间

Service 开机自启，掉线会自动重试。Kindle 通过 WiFi 连接，可以摆在房间任何角落。

两台 AI Agent，一台负责破障，一台负责铺路。中间夹着一个学会了读 shell 脚本的人类。

## 余波

这个项目的本意是追踪 Claude 用量。跑完之后，我甚至开始认真考虑取消已经续了一年多的 Claude Max 订阅，全部改用 API 更灵活。但冷静下来想——因为跑通了一个项目就推翻整个基础设施，太冲动了。

所以我新开了一个小项目：花一个月时间，把每个 outlet 的 pros and cons 摸清楚。Hermes、OpenClaw、Claude Code、各家 API 和订阅——什么时候用什么、预算怎么分配、能不能和该不该共享记忆，系统性地试一遍再决定。一个月后 report back。

## 后记

这次的记忆已经写入 Hermes 的长期上下文。下次再做跨设备调试的项目，它不会再问"USE_VOLUMD 设什么"——它会直接说：关了它。
