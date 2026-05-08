# Site transition — Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update `xchen101.github.io` so it honestly represents Xiaoli's transition: introduce Semantify co-founder identity, set DataCite role to ending Jun 2026, drop Munich from location, and tighten credential pills for client-readability — all via text edits to three files.

**Architecture:** Three small file edits (`_config.yml`, `_includes/hero.html`, `_includes/experience.html`). User runs `jekyll serve` locally to verify rendering before any push. Single commit covering all three files when satisfied. GitHub Pages auto-builds on push to `master`.

**Tech Stack:** Jekyll (GitHub Pages bundled — no Gemfile in repo), HTML, Liquid templating, YAML frontmatter, no JS or build step beyond Jekyll's own.

**Spec:** `docs/superpowers/specs/2026-05-08-site-transition-rewrite-design.md`

---

## Pre-flight

### Task 0: Verify working tree state

**Files:** none (read-only check)

- [ ] **Step 1: Confirm clean working tree on `master`**

Run: `git status --short`

Expected: only the listed `?? img/DSC_*.JPG` untracked photo files (no modified files in `_config.yml`, `_includes/`, etc.). If anything else shows up modified, surface it to the user before proceeding — don't blindly edit on top of in-progress work.

- [ ] **Step 2: Confirm we're on `master`**

Run: `git branch --show-current`

Expected output: `master`

- [ ] **Step 3: Confirm Jekyll is available for local preview**

Run: `jekyll --version`

Expected: a version string (e.g., `jekyll 4.x.x`).

If Jekyll is not installed, **stop and tell the user**. They will need to install Ruby + `gem install jekyll bundler` before this plan can proceed past Task 4 (where local preview happens). All edit tasks (1–3) can still proceed — verification just gets pushed to after install.

---

## File edits

### Task 1: `_config.yml` — description and role

**Files:**
- Modify: `_config.yml:3` (description) and `_config.yml:9` (author.role)

- [ ] **Step 1: Read current state**

Read `_config.yml`. Confirm exact existing content:
- Line 3: `description: Project Lead at DataCite — open science infrastructure, persistent identifiers, and community engagement.`
- Line 9: `  role: "Project Lead, DataCite"`

If either line differs from this, **stop and report** — don't edit unfamiliar content.

- [ ] **Step 2: Replace `description` line**

Edit `_config.yml`:

`old_string`:
```
description: Project Lead at DataCite — open science infrastructure, persistent identifiers, and community engagement.
```

`new_string`:
```
description: Co-founder of Semantify — open science consulting studio launching October 2026 from Edinburgh. Currently Project Lead at DataCite (through June 2026).
```

- [ ] **Step 3: Replace `author.role` line**

Edit `_config.yml`:

`old_string`:
```
  role: "Project Lead, DataCite"
```

`new_string`:
```
  role: "Co-founder, Semantify · Project Lead, DataCite"
```

- [ ] **Step 4: Verify both edits applied**

Read `_config.yml` again. Confirm:
- Line with `description:` now starts with `Co-founder of Semantify — open science consulting studio...`
- Line with `role:` now contains `"Co-founder, Semantify · Project Lead, DataCite"`
- `author.location` is still `"Edinburgh, UK"` (untouched)
- `author.email` is still `zoe.chen.xiaoli@gmail.com` (untouched)

No commit yet — all three files commit together at the end.

---

### Task 2: `_includes/hero.html` — bio paragraph

**Files:**
- Modify: `_includes/hero.html:9-11` (bio paragraph)

- [ ] **Step 1: Read current state**

Read `_includes/hero.html`. Confirm lines 9–11 exactly:
```html
    <p class="hero-bio">
      A decade building open science infrastructure — persistent identifiers, metadata standards, and the communities that depend on them. I bridge Chinese and international research ecosystems, with equal care for both.
    </p>
```

If different, **stop and report**.

- [ ] **Step 2: Replace the bio paragraph**

Edit `_includes/hero.html`:

`old_string`:
```
    <p class="hero-bio">
      A decade building open science infrastructure — persistent identifiers, metadata standards, and the communities that depend on them. I bridge Chinese and international research ecosystems, with equal care for both.
    </p>
```

`new_string`:
```
    <p class="hero-bio">
      Co-founder of <strong><a href="https://semantify.co/">Semantify</a></strong> — after a decade in open research infrastructure at DataCite, CERN, and the wider open science community. I help architect and implement practical open sharing workflows across the full research project lifecycle, with equal care for domain specificity and metadata interoperability. Through June 2026, wrapping up the <a href="https://doi.org/10.54224/20568">FAIR Workflows project</a> at DataCite.
    </p>
```

Note the structure:
- `<strong><a href="https://semantify.co/">Semantify</a></strong>` — both bold and linked
- `<a href="https://doi.org/10.54224/20568">FAIR Workflows project</a>` — linked, not bolded

- [ ] **Step 3: Verify edit applied**

Read `_includes/hero.html` lines 9–13 (the paragraph now spans more lines because the content is longer). Confirm:
- Opening `<p class="hero-bio">` and closing `</p>` are intact
- Both anchor tags are present
- The `<strong>` wraps the `<a>` for Semantify (not the other way round, though both work — the spec specified `<strong><a>` ordering)

---

### Task 3: `_includes/hero.html` — credential pills

**Files:**
- Modify: `_includes/hero.html:13-20` (credential-pills div)

- [ ] **Step 1: Read current state**

Read `_includes/hero.html`. Confirm lines 13–20:
```html
    <div class="credential-pills">
      <span class="pill">MLIS</span>
      <span class="pill">DataCite</span>
      <span class="pill">CERN alum</span>
      <span class="pill">ADHD</span>
      <span class="pill">ENFP</span>
      <span class="pill">TRYING MY BEST</span>
    </div>
```

(Line numbers may have shifted slightly after Task 2's edit — locate by content, not by line number.)

- [ ] **Step 2: Replace pills list**

Edit `_includes/hero.html`:

`old_string`:
```
    <div class="credential-pills">
      <span class="pill">MLIS</span>
      <span class="pill">DataCite</span>
      <span class="pill">CERN alum</span>
      <span class="pill">ADHD</span>
      <span class="pill">ENFP</span>
      <span class="pill">TRYING MY BEST</span>
    </div>
```

`new_string`:
```
    <div class="credential-pills">
      <span class="pill">SEMANTIFY</span>
      <span class="pill">MLIS</span>
      <span class="pill">DATACITE</span>
      <span class="pill">CERN ALUM</span>
    </div>
```

Casing note: `assets/css/style.css:396-406` applies `text-transform: uppercase` to `.pill`, so the rendered output will be all-caps regardless of source casing. Writing the source in caps anyway, for source-readability consistency with the existing `MLIS` pill — no behavioural change.

- [ ] **Step 3: Verify edit applied**

Read `_includes/hero.html`. Confirm `credential-pills` div now has exactly four `<span class="pill">` children in this order: SEMANTIFY, MLIS, DATACITE, CERN ALUM.

---

### Task 4: `_includes/experience.html` — DataCite entry date and location

**Files:**
- Modify: `_includes/experience.html:13` (date) and `_includes/experience.html:14` (location)

- [ ] **Step 1: Read current state**

Read `_includes/experience.html`. Confirm lines 12–14:
```html
      <div class="timeline-date-main">Oct 2021 —</div>
      <div class="timeline-date-main">Present</div>
      <div class="timeline-location">Remote · Edinburgh UK / Munich DE</div>
```

If different, **stop and report**.

- [ ] **Step 2: Change "Present" to "Jun 2026"**

Edit `_includes/experience.html`:

`old_string`:
```
      <div class="timeline-date-main">Oct 2021 —</div>
      <div class="timeline-date-main">Present</div>
      <div class="timeline-location">Remote · Edinburgh UK / Munich DE</div>
```

`new_string`:
```
      <div class="timeline-date-main">Oct 2021 —</div>
      <div class="timeline-date-main">Jun 2026</div>
      <div class="timeline-location">Remote · Edinburgh, UK</div>
```

Two changes in one edit: `Present` → `Jun 2026`, and `Remote · Edinburgh UK / Munich DE` → `Remote · Edinburgh, UK` (note the new comma after Edinburgh, matching the rest of the codebase's "City, Country" convention; Munich removed entirely).

The DataCite entry's three `<dl class="timeline-highlights">` sections (Grant leadership / Community engagement / Service development) **stay untouched**. They are Phase 2 work.

- [ ] **Step 3: Verify edit applied**

Read `_includes/experience.html`. Confirm:
- The DataCite entry's date now reads `Oct 2021 — Jun 2026`
- The location now reads `Remote · Edinburgh, UK`
- No occurrence of "Munich" remains anywhere in the file (search for "Munich" across the file)
- The three highlight `<dl>` blocks are unchanged

- [ ] **Step 4: Confirm no other "Munich" references in the codebase**

Search the whole repo for the literal string `Munich` (case-insensitive). Expected: zero hits in source files (`_config.yml`, `_includes/*`, `_layouts/*`, `_posts/*`, `_data/*.yml`). The string can legitimately appear in the design brief or generated `_site/` output (gitignored), but not in source.

---

## Verification

### Task 5: Local preview with jekyll serve

**Files:** none (runs the local server)

- [ ] **Step 1: Start jekyll serve**

Run (in a background-friendly shell — Bash with `run_in_background: true` is right):

`jekyll serve --livereload`

Expected: server starts on `http://127.0.0.1:4000`. If it errors with missing dependencies, surface to user.

- [ ] **Step 2: User loads `http://127.0.0.1:4000` and visually checks**

Provide the user with this checklist:

1. **Hero eyebrow**: should read "Co-founder, Semantify · Project Lead, DataCite". Does it fit on one line at desktop width without awkward wrap? (If it wraps awkwardly, Task 6 applies.)
2. **Hero bio**: paragraph contains "Co-founder of **Semantify**" with Semantify in bold and linked (hover should show `https://semantify.co/`). The phrase "FAIR Workflows project" is linked (hover should show `https://doi.org/10.54224/20568`).
3. **Credential pills**: exactly four pills in this order: SEMANTIFY, MLIS, DATACITE, CERN ALUM. No "TRYING MY BEST" / "ADHD" / "ENFP" pills remain.
4. **Experience timeline**: the top entry (DataCite) shows date `Oct 2021 — Jun 2026` and location `Remote · Edinburgh, UK`. No "Munich" anywhere on page.
5. **Page header `<title>` and meta description** (view source / inspect): meta description starts with "Co-founder of Semantify".

- [ ] **Step 3: Stop the dev server when verified**

Kill the background jekyll process (Ctrl+C in its terminal, or `KillShell` on the background shell).

---

### Task 6 (conditional): Eyebrow fallback if it wraps awkwardly

**When to apply:** Only if Task 5 step 2 item 1 reports that the eyebrow wraps awkwardly at desktop width or looks visually too cramped. The role string is 47 characters; depending on font metrics it may or may not fit. If it looks fine, **skip this task entirely**.

**Files:**
- Modify: `_includes/hero.html:7` (eyebrow div)

- [ ] **Step 1: Replace eyebrow markup with hardcoded two-line structure**

The current line:
```html
    <div class="hero-eyebrow">{{ site.author.role }}</div>
```

Change to:
```html
    <div class="hero-eyebrow">Co-founder, Semantify<br>Project Lead, DataCite</div>
```

This hardcodes the role text in the include and bypasses `site.author.role`. The `_config.yml` value is preserved for SEO/RSS use; only the visual rendering changes.

Alternatively, if the user prefers to keep using `site.author.role`: change `_config.yml` line 9 to `role: "Co-founder, Semantify<br>Project Lead, DataCite"` and use `{{ site.author.role | escape: false }}`-style raw output in the include. This is more brittle (HTML in YAML); prefer the hardcoded approach unless the user has a reason to keep templating.

- [ ] **Step 2: Reload the live preview and re-verify**

If the dev server was stopped in Task 5 step 3, restart it. Confirm eyebrow now renders on two lines and looks intentional.

---

## Ship

### Task 7: Single commit covering all changes

**Files:** none (commits the staged work)

- [ ] **Step 1: Stage the modified files**

Run:
```
git add _config.yml _includes/hero.html _includes/experience.html
```

(Do not use `git add -A` — keep the untracked `img/DSC_*.JPG` photos out of this commit; they belong in a separate "publish photo" commit.)

- [ ] **Step 2: Confirm only the three files are staged**

Run: `git status --short`

Expected: three lines starting with `M` for `_config.yml`, `_includes/experience.html`, `_includes/hero.html`. The `?? img/DSC_*.JPG` files should still be unstaged.

- [ ] **Step 3: Commit**

Run:
```
git commit -m "$(cat <<'EOF'
site: introduce Semantify co-founder identity, close DataCite role

Phase 1 of post-DataCite transition. Hero eyebrow now shows the composite
role (Co-founder, Semantify · Project Lead, DataCite); bio leads with
Semantify and links to semantify.co plus the FAIR Workflows DOI. Credential
pills tightened to four professional markers (SEMANTIFY · MLIS · DATACITE
· CERN ALUM). DataCite timeline entry now ends Jun 2026 and drops Munich
from the location string. DataCite role highlights and a Semantify timeline
entry are deferred to Phase 2, after Semantify positioning copy is final.

See docs/superpowers/specs/2026-05-08-site-transition-rewrite-design.md.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

- [ ] **Step 4: Verify commit landed**

Run: `git log -1 --stat`

Expected: one commit, exactly three files in the diff (`_config.yml`, `_includes/experience.html`, `_includes/hero.html`).

---

### Task 8: Push to master

**Files:** none

- [ ] **Step 1: Confirm with user before push**

Push is the irreversible-on-public-internet step. Surface to the user: "Local preview looked good. Ready to push to master? GitHub Pages will rebuild and the changes will be live in ~1–2 minutes."

Wait for explicit confirmation. Do not push without it.

- [ ] **Step 2: Push**

Run: `git push origin master`

Expected: success message, no rejected non-fast-forward (master is the working branch).

- [ ] **Step 3: Tell the user to spot-check live site after ~2 minutes**

GitHub Pages takes ~30–120 seconds to rebuild. Ask the user to visit `https://xchen101.github.io` after that and re-run the same visual checklist from Task 5 step 2 against the live site.

If anything looks wrong on live (e.g., browser cache showing old version, or build error), the user can hard-refresh (Ctrl+Shift+R) or check the GitHub Pages build status at `https://github.com/xchen101/xchen101.github.io/actions`.

---

## Done

Phase 1 complete. The site no longer claims active DataCite Project Lead beyond what's true (it shows the role ending Jun 2026), introduces Semantify, drops Munich, and reads more professionally for client-backcheck.

**Phase 2 trigger**: When user has Semantify's final positioning copy ready (tagline, three service lines, timeline summary), revisit `docs/superpowers/specs/2026-05-08-site-transition-rewrite-design.md` Phase 2 section and write a new implementation plan. Phase 2 will:

- Add `_includes/services.html` and slot into `_layouts/landing.html`
- Insert real Semantify entry at top of experience timeline
- Rewrite DataCite three highlights into challenge/action/outcome microformat
