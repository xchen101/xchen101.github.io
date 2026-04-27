---
layout: post
title: "NFC-Tagged Keyboards: Linking Hardware to Manuals"
date: 2026-04-27
tags: [keyboards, nfc, organization, mechanical-keyboards]
description: "I solved the problem of forgetting key combos across 8 mechanical keyboards with a simple NFC tag solution."
model: "claude-sonnet-4-20250514"
image: /img/20260220_100119.jpg
---

I have eight mechanical keyboards. This sounds excessive until you consider that each serves a different purpose: a 40% for travel, a 60% for gaming, a TKL for work, a full-size for data entry, and various others for specific layouts - that's what you would expect me to say. Frankly it's just because I like the way they look and they all sound delightful. Each one has custom keymaps, different remapping software, and unique key combinations for everything from layer toggles to RGB control.

The problem became clear when I'd sit down at a keyboard I hadn't used in a week and completely blank on how to access the second layer, or worse, accidentally trigger the firmware reset sequence while trying to adjust the backlight. I was constantly googling the same information: which software does this board use, what's the magic key combo, where did I put the manual link?

Muscle memory doesn't transfer between boards when one uses QMK, another uses VIA, and a third requires the manufacturer's proprietary software. I needed a way to connect each physical keyboard to its specific documentation and configuration details.

I bet sticking NFC tags on each keyboard would solve this problem: each keyboard gets a small NFC tag attached to its underside that stores a link to its manual, key references, and configuration details. One tap with my phone brings up everything I need to know about that specific board. No more hunting through bookmarks or trying to remember if this is the keyboard that uses Fn+Space or Fn+Caps for layer switching.

I got these cheap NFC tags lying around since I don't remember when, probably costed a pound a dozen. The idea is to write the tags to contain a URL pointing to a cloud-hosted page with the keyboard's documentation. For my 60% board, tapping the tag brings up a page that immediately shows me "Layer toggle: Fn+Space / Reset: Fn+Esc+R / RGB menu: Fn+G" along with links to the VIA configuration file and the original manual.

Setting this up will require creating a simple documentation system. A folder structure with each keyboard getting its own page containing the manual link, keymap reference, software details, and backup configuration file. The whole thing lives in my Obsidian vault and publishes to a simple static site. When I need to update a configuration or add notes about a new keymap, I edit the markdown file and the change propagates to the tag's target.

Just have to make sure to use the anti-metal variety with the metal case keyboards. Which I don't have at the moment. Need to hunt them down.

I can imagine this approach to go beyond keyboards too. I can also tag my game controllers with their button mapping references and headset firmware notes. Those are notoriously confusing especially for someone who go between Nintendo, PlayStation, PC, and general use i.e. remapped gamepad that controls the Macbook. I'll talk about that another time.


<div class="transparency-footer" markdown="0">
<p class="transparency-label"><em>This post was rewritten from a note using claude-sonnet-4-20250514. The prompt used:</em></p>
<pre class="transparency-prompt">
Here is the note to rewrite as a blog post.

**Title**: NFC-Tagged Keyboards: Linking Hardware to Manuals
**Tags from note**: 
**Date written**: 2026-04-27
---

# NFC-Tagged Keyboards: Linking Hardware to Manuals

---
**Created by:** K-2 (OpenClaw AI Assistant)
**Model:** Claude Haiku 4.5
**Original prompt:** Create note on sticking NFC tags to keyboards to link to manuals. Use case: organizing 8+ customizable mechanical keyboards (40%-100%) from different manufacturers with different remapping software. Also applicable to gamepads/controllers.
**Date created:** 2026-04-27

---

## The Problem

You own 8+ mechanical keyboards across different form factors (40%, 60%, TKL, 100%, etc.) from different manufacturers. Each has:
- Custom keymaps (QMK, VIA, manufacturer-specific software)
- Different layout conventions and layer setups
- Unique key combinations for remapping, RGB control, firmware flashing
- Scattered documentation across manufacturer websites, GitHub repos, Discord posts

**Reality:** It&#x27;s easy to forget which keyboard uses which software, which keybind toggles which layer, or where the manual actually lives. Muscle memory doesn&#x27;t transfer between boards. You end up googling the same info repeatedly.

## The NFC Solution

**Stick an NFC tag on each keyboard** (underside, or integrated into the case) that stores:
- A link to the keyboard&#x27;s manual/documentation
- Quick reference to remapping software used
- Critical key combos (layer toggles, firmware reset, RGB menu)
- Configuration backup location
- Model/serial number for warranty/repair tracking

**One tap with your phone = instant access to everything you need for that specific board.**

## Implementation

### NFC Tag Selection

- **Type 2 tags** (ISO14443A): Most common, cheap, ~64-180 bytes
- **Type 4 tags** (NFC Forum Type 4): More storage (4-32KB), better for rich data
- **Recommendation:** NTAG213/NTAG215 (cheap, ~$0.10-0.50, 180/888 bytes usable)

### What to Store on Each Tag

**Option 1: Simple (Minimal Data)**
```
https://qr-or-direct-link.com/keyboard-name/manual
Quick ref: Layer toggle: Fn+Space | Reset: Fn+R | RGB: Fn+G
```

**Option 2: Rich (Full Details)**
- Markdown or text file link
- QR code pointing to cloud-hosted keyboard profile
- VIA/QMK GitHub link
- Remapping software version used
- Backup config file location

### Physical Installation

1. **Find the spot:** Underside of keyboard (if flat), inside the case, or use adhesive NFC sticker
2. **Placement:** Away from metal shielding (interferes with NFC)
3. **Label:** Optional — mark which keyboard it is for quick ID
4. **Durability:** Use waterproof stickers or epoxy coating to protect tags

### Data Hosting

**Where to put the actual manuals/configs:**

- **Cloud:** Google Drive, Notion, Obsidian Publish, GitHub Pages
  - Pros: Accessible anywhere, versioned, no local storage needed
  - Cons: Requires internet when you need it
  
- **Local Wiki/Server:** Host on your Obsidian vault or a personal wiki
  - Pros: Full control, works offline with proper setup
  - Cons: Requires accessible server/network

- **Hybrid:** Cloud as primary, local backup
  - Best of both worlds, but more setup

### Recommended Setup

1. **Create a dedicated Obsidian folder:** `Keyboards/` with subfolders per board
   - Each board gets: manual.md, keymaps.md, software.md, config-backup.txt
   
2. **Host via Obsidian Publish or static site** (GitHub Pages)

3. **Generate NFC tag data:** URL to the published page + emergency quick-ref text

4. **Stick tags:** Standardized location on each board (e.g., bottom-right corner)

## Extension: Gamepads &amp; Controllers

This scales perfectly to gaming peripherals:

- **Fighting game controllers:** Link to layout diagrams, button mapping, fightstick software docs
- **Arcade sticks:** Custom button assignments, sensitivity settings, firmware version
- **Racing wheels:** Calibration guides, pedal mapping, force feedback configs
- **Headsets:** Firmware updates, EQ profiles, battery specs
- **Mice:** DPI presets, software, warranty/support links

**Same principle:** One tap = all the info you need for that peripheral.

## Benefits

✅ **No more Googling** — Everything you need is one tap away
✅ **Muscle memory unlocked** — Quickly recall which key combo does what
✅ **Guest-friendly** — Show someone else your setup instantly
✅ **Documentation stays with hardware** — No more orphaned manuals
✅ **Scalable** — Works for keyboards, controllers, streamdecks, macro pads, anything
✅ **Cheap &amp; durable** — NFC tags cost pennies, last years
✅ **Future-proof** — Just rewrite the tag if you change configs

## Next Steps

1. **Audit keyboards:** List all 8 boards, their keymaps, remapping software
2. **Centralize docs:** Create Obsidian vault structure + hosted version
3. **Order NFC tags:** NTAG215 stickers, 10-pack (~$5)
4. **Generate tag payloads:** Use an NFC app (e.g., TagWriter, NFC Tools) to write data
5. **Install &amp; test:** Stick tags, test tap response, iterate

---

**This is a living project.** As your keyboard collection evolves, the tags and linked docs evolve with it.

---

Rewrite this into a blog post. Return your response in this exact format:

&lt;frontmatter&gt;
title: (a clean, engaging title — can refine the original or keep it)
date: 2026-04-27
tags: (a refined tag list, lowercase, comma-separated, 2-5 tags)
description: (one sentence, under 160 characters, for meta/preview)
model: claude-sonnet-4-20250514
&lt;/frontmatter&gt;

&lt;post&gt;
(the rewritten blog post in markdown)
&lt;/post&gt;

&lt;notes&gt;
(optional: anything you cut that might be worth a separate post, or questions for the author about ambiguities)
&lt;/notes&gt;

**Author feedback on previous draft**: rewrite the article from the first person perspective, I have problems remembering the key combos of my 8 mechanical keyboards, and plan to use nfc tags to solve this problem. prefer prose than bullet points, keep the technicality to a reasonable amount.
</pre>
</div>
