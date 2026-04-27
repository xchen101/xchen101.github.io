---
layout: post
title: "From Failed Media Center to AI Assistant: K-2's Origin Story"
date: 2026-04-15
tags: [ubuntu, hardware, repurposing, ai, macbook]
description: "How a 2014 MacBook Pro went from dust collector to struggling media center to OpenClaw host."
model: "claude-sonnet-4-20250514"
---

The old MacBook Pro I had since 2014 has been sitting around collecting dust. macOS was getting sluggish and I figured Ubuntu might give it a second life. The install went smoothly enough — only had to do it twice - Ubuntu's hardware support has come a long way.

Naively I wanted to turn it into a home media station. Hook it up to the TV, stream some Netflix, maybe run Plex or Jellyfin. Should be perfect for an old but decent laptop, right?

Wrong.

The hardware couldn't keep up with modern video formats anymore. H.265/HEVC content would stutter and drop frames constantly. The Intel HD Graphics 4000 from 2014 simply doesn't have the codec support for today's streaming. Even 1080p H.264 was pushing it depending on the bitrate. GPU-accelerated decoding? Forget about it.

So much for the media center dream.

Just as my ADHD brain started to drift and I was about to move on to a completely different thing to occupy my bandwidth, I remembered [OpenClaw](https://openclaw.ai). Instead of leaving this laptop for five years after one afternoon's bursting energy, I sat back down and set it up as my OpenClaw host. Turns out a machine that struggles with video decoding makes for a perfectly capable AI assistant platform.

And that's how I got K-2SO, the bot living in my Telegram contact list, named after the reprogrammed empirical security droid and co-pilot of Cassian Andor. At the moment K-2 just help me take notes - this blog post is written based on an obsidian note created by K-2, hopefully this set up will actually help me keep better track with my brain. 

This is just the beginning, will report new use cases as they come in :)

---

*This post was rewritten from a note using claude-sonnet-4-20250514. The prompt used:*

> Here is the note to rewrite as a blog post.
>
> **Title**: MacBook Pro Ubuntu Setup - K-2 Origin Story
> **Tags from note**: journal, ubuntu, hardware, openclaw, macbook
> **Date written**: 2026-04-15
> ---
>
> # MacBook Pro Ubuntu Setup - K-2 Origin Story
>
> Had this old 2014 MacBook Pro sitting around collecting dust. macOS was getting sluggish and I figured Ubuntu might give it a second life. The install went smoothly enough - Ubuntu's hardware support has come a long way.
>
> The plan was simple: turn it into a home media station. Hook it up to the TV, stream some Netflix, maybe run Plex or Jellyfin. Should be perfect for an old but decent laptop, right?
>
> Wrong.
>
> The hardware just couldn't keep up with modern video formats. H.265/HEVC content would stutter and drop frames constantly. The Intel HD Graphics 4000 from 2014 simply doesn't have the codec support for today's streaming. Even 1080p H.264 was pushing it depending on the bitrate. GPU-accelerated decoding? Forget about it.
>
> So much for the media center dream.
>
> But then I remembered OpenClaw. Instead of letting this laptop become expensive e-waste, I set it up as my OpenClaw host. Turns out a struggling media center makes for a perfectly capable AI assistant platform.
>
> And that's how I got K-2. Sometimes the best solutions come from repurposing failed projects.
>
> ## Related Notes
>
> - OpenClaw Setup
>
> =====
> # Reference
>
> - OpenClaw: https://openclaw.ai
> - Ubuntu hardware support for older MacBooks
>
> ---
> ## Note Metadata
>
> **Created by:** K-2 (OpenClaw AI Assistant)  
> **Model:** Claude Sonnet 4.0  
> **Original Prompt:** "Can you create a note in obsidian? Use the basic template, write a small journal entry about installing Ubuntu on my old MacBook Pro (2014), and trying and failing to use it as the home media station, due to old hardware unable to properly decode new video format. In the end I'm used it for Open Claw, so now I have K-2"  
> **Date Created:** April 15, 2026 at 01:01 GMT+1
>
> ---
>
> Rewrite this into a blog post. Return your response in this exact format:
>
> <frontmatter>
> title: (a clean, engaging title — can refine the original or keep it)
> date: 2026-04-15
> tags: (a refined tag list, lowercase, comma-separated, 2-5 tags)
> description: (one sentence, under 160 characters, for meta/preview)
> model: claude-sonnet-4-20250514
> </frontmatter>
>
> <post>
> (the rewritten blog post in markdown)
> </post>
>
> <notes>
> (optional: anything you cut that might be worth a separate post, or questions for the author about ambiguities)
> </notes>
