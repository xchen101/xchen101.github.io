# Personal site — post-DataCite transition rewrite

**Date**: 2026-05-08
**Owner**: Xiaoli Chen
**Status**: design approved, awaiting implementation plan

## Background

The current landing on `xchen101.github.io` was written when "Project Lead at DataCite" was the live full-time role. Three problems surfaced in feedback:

1. **Title expiry**: the DataCite Project Lead role ends June 2026. After that date, the hero eyebrow and `_config.yml` `description` will be a lie.
2. **Audience mismatch**: the page narrates DataCite outputs in internal-performance-review language (deliverables managed, conferences attended, schema additions). Stranger readers — particularly potential clients of the new consulting studio — cannot translate that into "what problems does Xiaoli solve for me."
3. **Location confusion**: `_config.yml` says "Edinburgh, UK"; the DataCite timeline entry says "Remote · Edinburgh UK / Munich DE." This reads like dual-residency. Xiaoli is based in Edinburgh; Munich is a past address.

## What's changing

After June 2026, Xiaoli is co-founder of **Semantify**, an open science consulting studio (semantify.co, registered in Scotland, launching October 2026). The studio handles its own client conversion at semantify.co. This personal site does not need to be a sales pitch.

### Audience priority for `xchen101.github.io`

In order:

1. **Potential client backcheck** — clients see Semantify proposal, search Xiaoli, land here. Site needs to read as credible to a stranger considering hiring her.
2. **Future employer / full-time CV** — backup function if Semantify path changes.
3. **Personal identity** — photography, writing, current consumption (`now` widget). Carried by hero photo, blog, projects.
4. **Community / peers** — RDA/FORCE11/China-international circle. Lowest priority; insider language is not the goal.

### Information architecture decisions

- **Personal brand stays primary.** Hero remains "Xiaoli Chen"; Semantify is a named identity within the site, not the site's owner.
- **Semantify is a sibling site, linked from here.** No sales-focused copy on `xchen101.github.io` — that is `semantify.co`'s job.
- **Hero eyebrow uses composite role** during the May→June transition: "Co-founder, Semantify · Project Lead, DataCite." After June 30, drop the DataCite half.
- **Timeline is past-and-present only.** No future entries. Semantify enters the timeline when it actually launches in October 2026 (Phase 2).

## Phase 1 — ship now (before end of June)

Scope: cosmetic-and-truth fixes that do not require Semantify's final positioning copy. Goal: stop the page from misrepresenting the present, without committing to copy that will be rewritten in Phase 2.

### File 1 — `_config.yml`

Two keys change. Final values:

```yaml
description: Co-founder of Semantify — open science consulting studio launching October 2026 from Edinburgh. Currently Project Lead at DataCite (through June 2026).

author:
  role: "Co-founder, Semantify · Project Lead, DataCite"
```

`description` is the SEO meta line (was: "Project Lead at DataCite — open science infrastructure, persistent identifiers, and community engagement."). `author.role` renders in hero eyebrow via `{{ site.author.role }}` (was: "Project Lead, DataCite"). `author.location` is already "Edinburgh, UK" and does not change — Munich only exists in the experience timeline and gets removed there. Other `author.*` keys (`name`, `email`) are unchanged.

**Eyebrow length fallback**: the new role string is 47 characters. If it does not fit one line on desktop (or wraps awkwardly), break to two lines explicitly — either by inserting a `<br>` mid-string (requires the include to render `author.role` as raw HTML rather than escaped text), or by hardcoding the two-line structure directly in `_includes/hero.html` and removing the dependency on `site.author.role`. The user's preference is two lines over an awkward one-line wrap.

### File 2 — `_includes/hero.html`

**Replace the bio paragraph** (currently lines 9–11) with:

> Co-founder of **[Semantify](https://semantify.co/)** — after a decade inside the field at DataCite, CERN, and the wider open science community. I architect open research practical implementation across the full research project lifecycle, with equal care for domain specificity and metadata interoperability. Through June 2026, wrapping up the [FAIR Workflows project](https://doi.org/10.54224/20568) at DataCite.

Two links in the bio: "Semantify" → `https://semantify.co/`, "FAIR Workflows project" → `https://doi.org/10.54224/20568`. The bold styling on Semantify is preserved. Bio writes as HTML in the include:

```html
<p class="hero-bio">
  Co-founder of <strong><a href="https://semantify.co/">Semantify</a></strong> — after a decade inside the field at DataCite, CERN, and the wider open science community. I architect open research practical implementation across the full research project lifecycle, with equal care for domain specificity and metadata interoperability. Through June 2026, wrapping up the <a href="https://doi.org/10.54224/20568">FAIR Workflows project</a> at DataCite.
</p>
```

Note: the appositive describing Semantify ("an open science consulting studio based in Edinburgh and launching October 2026") was removed from the bio at user's request. The studio's identity and timing live in `_config.yml description` (SEO meta) and on `semantify.co` itself; not duplicated in hero bio.

**Replace the credential pills** (currently lines 14–19) with:

```html
<span class="pill">SEMANTIFY</span>
<span class="pill">MLIS</span>
<span class="pill">DATACITE</span>
<span class="pill">CERN ALUM</span>
```

Removed: `TRYING MY BEST`, `ADHD`, `ENFP`. The personality layer those pills carried is preserved elsewhere (photography in hero, `now` widget, blog). The eyebrow region is being upgraded for client-readability — this is a deliberate trade-off.

### File 3 — `_includes/experience.html`

**Modify the DataCite timeline entry** (the first `<article class="timeline-entry">`, currently lines 10–35):

- Line 13: `<div class="timeline-date-main">Present</div>` → `<div class="timeline-date-main">Jun 2026</div>`
- Line 14: `<div class="timeline-location">Remote · Edinburgh UK / Munich DE</div>` → `<div class="timeline-location">Remote · Edinburgh, UK</div>`

The three `<dl class="timeline-highlights">` blocks (Grant leadership / Community engagement / Service development) **stay untouched in Phase 1**. Their internal-performance-review tone is exactly what Phase 2 will rewrite into challenge/action/outcome language. Touching them now risks two rewrites.

**No new Semantify timeline entry** in Phase 1. Rationale: the timeline is reverse-chronological work history. A "launching October 2026" future entry breaks that contract and reads as inflated. Hero eyebrow + bio + pill carry the Semantify-exists message until October. When Semantify actually launches, Phase 2 inserts the real entry.

### Phase 1 ship plan

1. Make the three file edits.
2. **User runs `jekyll serve` locally and reviews before push.** Spot-check items: hero eyebrow displays the composite role (one line if it fits, two if it doesn't — both acceptable), bio renders bold + both links work, pills show the four-item list, DataCite timeline shows `Oct 2021 — Jun 2026` with location `Remote · Edinburgh, UK` (no Munich anywhere on page).
3. If anything is off, iterate locally.
4. Once the user is satisfied, commit all three file changes as a single commit, push to `master`. GitHub Pages auto-builds.

If Ruby/Jekyll is not currently installed on the user's machine (the prior memory snapshot suggested it wasn't), step 2 requires that to be set up first — implementation plan should account for that as a possible blocker, but the spec assumes the user can preview.

## Phase 2 — after Semantify content is ready (roughly Oct 2026)

Triggered by: Xiaoli has decided Semantify's final tagline, service categories, and case-study language. Goal: turn this site from "honest about transition" into "useful credibility document for clients."

### File 4 (new) — `_includes/services.html`

A new section, slotted between hero and projects in `_layouts/landing.html`. Section eyebrow numbering: insert as `01½` or renumber `02 / 03 / 04 ...` (decide at implementation time based on visual flow).

Structure:

- Eyebrow + title: e.g., "— 01½ / Practice", title "What I work on" or "How I help"
- Three short prose lines, each one a service category Semantify offers. Wording sourced from Semantify's final positioning, not invented here.
- Closing line linking to semantify.co — e.g., "Through **Semantify** — semantify.co →"

This is the section that directly addresses the audience-mismatch feedback. It speaks to a stranger client in their language, before the experience timeline gets a chance to drown them in DataCite-internal jargon.

### File 5 — `_includes/experience.html` (round two)

**Insert Semantify entry** at the top of `<div class="timeline">`:

```html
<article class="timeline-entry">
  <div class="timeline-date">
    <div class="timeline-date-main">Oct 2026 —</div>
    <div class="timeline-date-main">Present</div>
    <div class="timeline-location">Edinburgh, UK</div>
  </div>
  <div class="timeline-content">
    <h3 class="timeline-role">Semantify</h3>
    <div class="timeline-title">Co-founder</div>
    <p class="timeline-summary">[Real summary: what Semantify does, who it serves, written in client-readable language. Sourced from Semantify's positioning when ready.]</p>
    <!-- Optional: <dl class="timeline-highlights"> with concrete service categories -->
  </div>
</article>
```

**Rewrite DataCite three highlights** from internal-performance-review language to challenge → action → outcome microformat. Each highlight should answer: what problem existed, what did Xiaoli do, what changed. Examples (illustrative, not final):

- *Grant leadership*: instead of "Managed project milestones across distributed teams; tracked reuse..." → name the underlying challenge ("seven international partners with diverging publication timelines"), the action, the outcome ("38 deliverables shipped on schedule, including X").
- *Service development*: the CSTR-as-alternate-identifier line is already strong because it has a concrete artifact. Light edit only.
- *Community engagement*: hardest to rewrite as outcome-language. Possibly recasts as "where my judgment is trusted" rather than activity counts.

This rewrite happens with Semantify's positioning in hand so the language across both timeline entries is consistent.

## Out of scope

- Architectural rebuild of the landing page. Section ordering, photography treatment, dark theme, type system, social-icons footer, projects/publications/blog regions, `now` widget — none of these change.
- Adding sales copy, calls-to-action, contact forms beyond the existing email link. Conversion lives at `semantify.co`.
- Touching the personal identity layer (photography, blog, `now`, education, community section) beyond the small pill cleanup.
- Touching `_data/projects.yml`, `_data/publications.yml`, `_data/now.yml`.

## Open items the user will fill in for Phase 2

- Semantify's final tagline (placeholder: "Clarity for open research")
- Three (or so) service category lines for the new section
- The Semantify timeline summary copy
- Decision on whether Semantify entry gets a `<dl class="timeline-highlights">` block

## Risks and reversal

All Phase 1 changes are text-only edits to three files. Reversible by a single revert commit. No data, layout, or asset changes. No risk to the photography aesthetic or any visitor-facing region beyond the hero and the DataCite timeline entry.
