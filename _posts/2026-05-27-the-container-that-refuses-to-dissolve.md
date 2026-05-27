---
layout: post
title: "The Container That Refuses to Dissolve"
date: 2026-05-27
tags: [scholarly-publishing, AI, MCP, open-access, peer-review]
description: "On publishers building MCP endpoints, the changing nature of scholarly output, and why the paper container no longer anchors the system."
lang: en
image: /img/container-that-refuses-to-dissolve.jpg
---

# The Container That Refuses to Dissolve

A recent piece on the Scholarly Kitchen (sponsored by Silverchair, disclosure duly noted) makes a case that publishers urgently need to build Model Context Protocol (MCP) endpoints — lest the defaults for how AI agents access scholarly content be "set without them." The argument isn't wrong in its premises: MCP downloads went from 100,000 to 97 million monthly in a year, and most publishers haven't even heard of it. If you don't build the infrastructure, someone else will.

But the article frames this as a straightforward imperative: publishers should build MCP endpoints because they are the natural custodians of "the values of scholarly publishing" — attribution, version control, retraction handling, and entitlement management.

That last one does a lot of heavy lifting.

## Whose Values?

Attribution and version control are genuinely shared values between publishers and the research community. Entitlement management is not. It is a business requirement. By bundling it into the same list — by treating "who paid for access" as a first-class property of scholarly infrastructure on par with "who wrote this" and "which version is current" — the industry risks encoding paywalls into the protocol layer before anyone asks whether that's what scholarly communication needs.

The JAMA Network's trajectory is instructive. In early 2024 it fully blocked AI crawlers. By fall 2025 it had reversed course, selectively allowing certain agents back in — not because blocking was wrong in principle, but because some bots turned out to drive useful referral traffic. The calculus was ROI, not principle. Publishers engaging with AI are making business decisions dressed as infrastructure decisions. Consider this a reminder, not a criticism: they are far from neutral actors in this space. We should not forget that if the only stakeholders building the pipes are the ones who profit from scarcity, the pipes will be built for scarcity.

## Meanwhile, the Research Community Has Already Started Moving

The deeper problem with the "build MCP endpoints fast" framing is that it assumes the paper — the journal article — remains the natural unit of scholarly output. An MCP endpoint serves up a DOI-grounded, metadata-rich, entitlement-checked article object. It makes the paper legible to AI systems. It does not question whether the paper is still the right thing to be serving, when the trends on the ground suggest it increasingly isn't.

In computationally intensive STEM fields, the research output triad is already GitHub + Colab + Hugging Face. Datasets, models, notebooks, and reproducible pipelines are the primary products. The paper, where it exists, is a README — a contextualizing narrative, optional. The community has already lowkey moved the center of gravity from "publish in journal X" to "push to repo, tag a release, let the community fork and build." ArXiv validated this path twenty years ago: speed and openness beat prestige when the community is healthy enough to self-correct.

In the humanities and social sciences, the same logic manifests differently. When AI makes it frictionless to transform field notes, ethnographic recordings, or archival materials into any format — a monograph, a podcast, a mobile app, a short play — the form itself stops signaling legitimacy, the work does. An anthropologist whose fieldwork results in a mobile app and a verse essay has produced research. Whether anyone "published a paper" is secondary to whether the work was rigorous, grounded, and findable.

## Form Is Cheap Now. That Changes Everything.

AI has made formatting outcomes into practically any container frictionless and effectively costless. When a researcher can — in minutes — produce a structured report, an interactive visualization, a podcast summary, and a formatted manuscript from the same underlying work, the choice of format carries no information about effort, rigor, or quality. It is a presentation layer.

Prestige has always been carried, in part, by form — by the fact that getting something into a particular format was hard and required a particular kind of institutional gatekeeping. When that gatekeeping disappears, prestige must relocate to the production process. Who reviewed this? How reproducible is it? Who is citing or forking or building on it? The value is attached to the behavioral signals, instead of submission signals.

The paper remains useful as a narrative structure. The Abstract-Introduction-Methods-Results-Discussion arc is a good cognitive scaffold. But it is no longer the only scaffold, and as AI-driven synthesis tools make it trivial to generate that narrative from underlying data, its uniqueness dissolves.

## What Papers Still Do (And What They Don't)

Papers had been serving a few real functions:

- **Certification:** Peer review attached to a fixed version of record signals quality.
- **Anchoring:** Version of record pins an acknowledged progress to the map of a domain.
- **Narrative:** Someone structured this knowledge into a story.

But none of these functions is intrinsically tied to the journal article container. Certification can attach to a dataset, a protocol, a registered report, a model card. Anchoring is done through the registration of persistent identifiers with their associated metadata — a point of reference the community can cite, regardless of the type of output. Narrative can be auto-generated from structured data.

The paper is one container among many. It retains value. It has a higher chance of retaining value than the journal, which is an aggregation layer onto containers. But it does not have a higher *prestige rank* than other containers by default — and the younger the researcher, the less they assume it does.

## The Real Game: Tenure Committees

The old guard's prestige model is sustained by institutional inertia. As long as tenure committees count papers and ignore Hugging Face stars, the journal article retains a structural advantage that no amount of technological change alone can dissolve.

But the pressure is building from the bottom. In computational fields, young faculty are already building cases around open infrastructure — "my model was forked 12,000 times, independently reproduced by three labs, and cited as a benchmark in X papers." Mathematics and physics have been here for decades with the arXiv preprint as the de facto primary publication.

A common counterargument is that high-energy physics — the poster child for the preprint-first model — is structurally unique: massive collaborations, shared mega-facilities, centralized data pipelines, a relatively small and tightly connected community. The model worked there, the argument goes, because the community started with shared infrastructure rather than having to build it.

AI tools make that objection harder to sustain. They don't magically solve coordination overnight, but they lower the cost of building data-sharing discipline to a point where more communities find it worth the effort. A lab in synthetic biology, a network of climate researchers, a distributed anthropology project — none of them needs CERN-scale coordination to adopt the core practices that made HEP work: shared repositories, versioned outputs, preprint-first dissemination. The infrastructure that once demanded a generation of institutional consensus and dedicated engineering now becomes accessible to a smaller, more motivated group. Once that door opens — once a community has tasted what it means to circulate and build on each other's work without journal intervention — it does not swing shut.

The question has shifted from whether this spreads to which disciplines break next, and how fast.

The tenure committee that accepts a Hugging Face leaderboard position as equivalent to a high-impact publication is the milestone. And it is coming — for the simple reason that in the disciplines where this matters most, the people evaluating tenure are increasingly the people who grew up doing their work this way.

## So Let Them Build Their Walls

If publishers want to build MCP endpoints that enshrine paywalls in the protocol layer — that lock scholarly content behind entitlement checks at the infrastructure level — let them. They are building the best possible infrastructure for a world that is slowly ceasing to need the paper they are optimizing for.

The infrastructure that will actually support diverse research outputs — code repositories, model registries, data archives, interactive notebooks, multimedia scholarship — needs to be open by design. Not open as a slogan, but open in the structural sense: the more it exposes standard interfaces, the easier it is to integrate into workflows, and the more robust it becomes. Openness is a network effect for infrastructure. Every new integration increases its value; every locked endpoint reduces its reach. Publishers building proprietary MCP endpoints are placing a bet on scarcity. The community building openly on DOIs, ORCIDs, RO-Crates, and standard APIs is placing a bet on composability.

The more deeply AI integrates into research workflows, the more diverse and container-agnostic the output becomes. The paper will not disappear. It will become one option among many, without automatic priority. The institutions that bet everything on being the best paper container will maintain the finest infrastructure for a format that no longer anchors the system.

<div class="transparency-footer" markdown="0">
<p class="transparency-label"><em>This post was drafted by K-2 (OpenClaw AI Assistant, DeepSeek V4 Flash) based on a discussion with the author, then manually reviewed and approved for publication. The source note and driving prompt are reproduced verbatim below.</em></p>
<pre class="transparency-prompt">
Appendix: source note and prompts
Reproduced verbatim.

--- Source note metadata ---
Created by: K-2 (OpenClaw AI Assistant)
Model: openrouter/deepseek/deepseek-v4-flash (DeepSeek V4 Flash)
Date created: 2026-05-27

--- Original prompt (posts to K-2, in Chinese, verbatim) ---

把咱们讨论的这一段写篇短文章吧我想发博客上。写英文的，从scholarly kitchen哪篇切入，出版社和学术社区的利益重合度的降低，出版社heavy handed商业模式虎视眈眈想在AI时代把paywall再建回去；但如果它们想守着论文那一亩三分地就随他们去，深入的AI集成让学术社区可以afford to move on from papers，papers还具有一定的价值，但不比任何其它形式的科研产出更prestigeous；就落脚在你说的这点，拭目以待tenure committee与时俱进的这一刻。

--- Source note (the complete K-2 output that became this post) ---

# The Container That Refuses to Dissolve

A recent piece on the Scholarly Kitchen (sponsored by Silverchair, disclosure duly noted) makes a case that publishers urgently need to build Model Context Protocol (MCP) endpoints — lest the defaults for how AI agents access scholarly content be "set without them." The argument isn't wrong in its premises: MCP downloads went from 100,000 to 97 million monthly in a year, and most publishers haven't even heard of it. If you don't build the infrastructure, someone else will.

But the article frames this as a straightforward imperative: publishers should build MCP endpoints because they are the natural custodians of "the values of scholarly publishing" — attribution, version control, retraction handling, and entitlement management.

That last one does a lot of heavy lifting.

## Whose Values?

Attribution and version control are genuinely shared values between publishers and the research community. Entitlement management is not. It is a business requirement. By bundling it into the same list — by treating "who paid for access" as a first-class property of scholarly infrastructure on par with "who wrote this" and "which version is current" — the industry risks encoding paywalls into the protocol layer before anyone asks whether that's what scholarly communication needs.

The JAMA Network's trajectory is instructive. In early 2024 it fully blocked AI crawlers. By fall 2025 it had reversed course, selectively allowing certain agents back in — not because blocking was wrong in principle, but because some bots turned out to drive useful referral traffic. The calculus was ROI, not principle. Publishers engaging with AI are making business decisions dressed as infrastructure decisions. Consider this a reminder, not a criticism: they are far from neutral actors in this space. We should not forget that if the only stakeholders building the pipes are the ones who profit from scarcity, the pipes will be built for scarcity.

## Meanwhile, the Research Community Has Already Started Moving

The deeper problem with the "build MCP endpoints fast" framing is that it assumes the paper — the journal article — remains the natural unit of scholarly output. An MCP endpoint serves up a DOI-grounded, metadata-rich, entitlement-checked article object. It makes the paper legible to AI systems. It does not question whether the paper is still the right thing to be serving, when the trends on the ground suggest it increasingly isn't.

In computationally intensive STEM fields, the research output triad is already GitHub + Colab + Hugging Face. Datasets, models, notebooks, and reproducible pipelines are the primary products. The paper, where it exists, is a README — a contextualizing narrative, optional. The community has already lowkey moved the center of gravity from "publish in journal X" to "push to repo, tag a release, let the community fork and build." ArXiv validated this path twenty years ago: speed and openness beat prestige when the community is healthy enough to self-correct.

In the humanities and social sciences, the same logic manifests differently. When AI makes it frictionless to transform field notes, ethnographic recordings, or archival materials into any format — a monograph, a podcast, a mobile app, a short play — the form itself stops signaling legitimacy, the work does. An anthropologist whose fieldwork results in a mobile app and a verse essay has produced research. Whether anyone "published a paper" is secondary to whether the work was rigorous, grounded, and findable.

## Form Is Cheap Now. That Changes Everything.

AI has made formatting outcomes into practically any container frictionless and effectively costless. When a researcher can — in minutes — produce a structured report, an interactive visualization, a podcast summary, and a formatted manuscript from the same underlying work, the choice of format carries no information about effort, rigor, or quality. It is a presentation layer.

Prestige has always been carried, in part, by form — by the fact that getting something into a particular format was hard and required a particular kind of institutional gatekeeping. When that gatekeeping disappears, prestige must relocate to the production process. Who reviewed this? How reproducible is it? Who is citing or forking or building on it? The value is attached to the behavioral signals, instead of submission signals.

The paper remains useful as a narrative structure. The Abstract-Introduction-Methods-Results-Discussion arc is a good cognitive scaffold. But it is no longer the only scaffold, and as AI-driven synthesis tools make it trivial to generate that narrative from underlying data, its uniqueness dissolves.

## What Papers Still Do (And What They Don't)

Papers had been serving a few real functions:

- **Certification:** Peer review attached to a fixed version of record signals quality.
- **Anchoring:** Version of record pins an acknowledged progress to the map of a domain.
- **Narrative:** Someone structured this knowledge into a story.

But none of these functions is intrinsically tied to the journal article container. Certification can attach to a dataset, a protocol, a registered report, a model card. Anchoring is done through the registration of persistent identifiers with their associated metadata — a point of reference the community can cite, regardless of the type of output. Narrative can be auto-generated from structured data.

The paper is one container among many. It retains value. It has a higher chance of retaining value than the journal, which is an aggregation layer onto containers. But it does not have a higher *prestige rank* than other containers by default — and the younger the researcher, the less they assume it does.

## The Real Game: Tenure Committees

The old guard's prestige model is sustained by institutional inertia. As long as tenure committees count papers and ignore Hugging Face stars, the journal article retains a structural advantage that no amount of technological change alone can dissolve.

But the pressure is building from the bottom. In computational fields, young faculty are already building cases around open infrastructure — "my model was forked 12,000 times, independently reproduced by three labs, and cited as a benchmark in X papers." Mathematics and physics have been here for decades with the arXiv preprint as the de facto primary publication.

A common counterargument is that high-energy physics — the poster child for the preprint-first model — is structurally unique: massive collaborations, shared mega-facilities, centralized data pipelines, a relatively small and tightly connected community. The model worked there, the argument goes, because the community started with shared infrastructure rather than having to build it.

AI tools make that objection harder to sustain. They don't magically solve coordination overnight, but they lower the cost of building data-sharing discipline to a point where more communities find it worth the effort. A lab in synthetic biology, a network of climate researchers, a distributed anthropology project — none of them needs CERN-scale coordination to adopt the core practices that made HEP work: shared repositories, versioned outputs, preprint-first dissemination. The infrastructure that once demanded a generation of institutional consensus and dedicated engineering now becomes accessible to a smaller, more motivated group. Once that door opens — once a community has tasted what it means to circulate and build on each other's work without journal intervention — it does not swing shut.

The question has shifted from whether this spreads to which disciplines break next, and how fast.

The tenure committee that accepts a Hugging Face leaderboard position as equivalent to a high-impact publication is the milestone. And it is coming — for the simple reason that in the disciplines where this matters most, the people evaluating tenure are increasingly the people who grew up doing their work this way.

## So Let Them Build Their Walls

If publishers want to build MCP endpoints that enshrine paywalls in the protocol layer — that lock scholarly content behind entitlement checks at the infrastructure level — let them. They are building the best possible infrastructure for a world that is slowly ceasing to need the paper they are optimizing for.

The infrastructure that will actually support diverse research outputs — code repositories, model registries, data archives, interactive notebooks, multimedia scholarship — needs to be open by design. Not open as a slogan, but open in the structural sense: the more it exposes standard interfaces, the easier it is to integrate into workflows, and the more robust it becomes. Openness is a network effect for infrastructure. Every new integration increases its value; every locked endpoint reduces its reach. Publishers building proprietary MCP endpoints are placing a bet on scarcity. The community building openly on DOIs, ORCIDs, RO-Crates, and standard APIs is placing a bet on composability.

The more deeply AI integrates into research workflows, the more diverse and container-agnostic the output becomes. The paper will not disappear. It will become one option among many, without automatic priority. The institutions that bet everything on being the best paper container will maintain the finest infrastructure for a format that no longer anchors the system.
</pre>
</div>
