# Plan: Restructure to Single-Page Scrolling Site



## Context



Transform Xiaoli's multi-page Jekyll site into a single-page portfolio/CV site. The current site has separate pages (Blog, About, Projects) — these become vertically-stacked sections on one scrollable page. Individual post pages and the blog archive remain accessible via links.



**Missing content**: The draft plan references `source/XChenCV.md` and `source/Purpose & context.txt` — these files do not exist in the repo. All CV-related content (Experience, Education, Publications, Community) will use well-structured placeholder text marked with `<!-- TODO -->` comments for the user to fill in. The hero bio is adapted from the existing `about.md`.



---



## Architecture



```

┌──────────────────────────────────────────────────────┐

│  default.html                                        │

│  ┌──────────────────────────────────────────────────┐│

│  │ <nav> — globally updated:                        ││

│  │   anchor links (/#about, /#projects, /#experience││

│  │   /#publications) + /blog/ link                  ││

│  │   Sticky: position sticky, z-index 100           ││

│  └──────────────────────────────────────────────────┘│

│  ┌──────────────────────────────────────────────────┐│

│  │ <main>{{ content }}</main>                        ││

│  └──────────────────────────────────────────────────┘│

│  ┌──────────────────────────────────────────────────┐│

│  │ {% include footer.html %}                        ││

│  └──────────────────────────────────────────────────┘│

│  <script src="/assets/js/main.js">                   │

└──────────────────────────────────────────────────────┘



landing.html (extends default) — used by index.md

├── <section id="about">    {% include hero.html %}

├── <section id="posts">    {% include recent-posts.html %}

├── <section id="projects"> {% include projects.html %}

├── <section id="experience">{% include experience.html %}

├── <section id="education">{% include education.html %}

├── <section id="publications">{% include publications.html %}

└── <section id="community">{% include community.html %}



Shared includes (reused across layouts):

  social-icons.html — extracted from default.html, used in hero + footer

  footer.html — extracted from default.html, uses social-icons.html

```



**Nav strategy**: All nav links use absolute anchors (`/#about`, `/#projects`, etc.) globally. On the landing page, JS intercepts these for smooth scrolling. From other pages (blog posts, archive), clicking navigates to the homepage and the browser handles the fragment. No conditional logic needed in the nav.



---



## Implementation Steps (in dependency order)



### Step 1: Create data file



**`_data/publications.yml`** (new) — 3-5 placeholder entries:

```yaml

- title: "TODO: Publication title"

  year: 2024

  venue: "TODO: Journal or Conference"

  doi: "https://doi.org/10.xxxxx/TODO"

```



### Step 2: Extract shared includes from `_layouts/default.html`



**`_includes/social-icons.html`** (new) — Move the SVG icon block (lines 29–48 of `default.html`, the `{% if site.bluesky_username %}...{% endif %}` blocks for Bluesky, Instagram, GitHub, LinkedIn) into this file. Identical markup, just extracted.



**`_includes/footer.html`** (new) — Move the `<footer class="site-footer">` element (lines 27–51 of `default.html`) into this file. Replace the inline social icons div with `{% include social-icons.html %}`. Add a back-to-top anchor link: `<a href="#" class="back-to-top">Back to top</a>`.



### Step 3: Update `_layouts/default.html`



Three targeted changes:



1. **Nav links** — Replace the three page links (Blog, About, Projects) with:

   - `About` → `/#about`

   - `Projects` → `/#projects`

   - `Experience` → `/#experience`

   - `Publications` → `/#publications`

   - `Blog` → `/blog/`

   

   Remove the `{% if page.url == ... %}active{% endif %}` conditionals (JS handles active state on landing page; on other pages, no nav item is active except Blog when on `/blog/`).



2. **Sticky nav** — Add `id="site-nav"` to the `<nav>` element.



3. **Footer** — Replace the inline `<footer>...</footer>` block with `{% include footer.html %}`.



4. **Script** — Add `<script src="{{ '/assets/js/main.js' | relative_url }}"></script>` before `</body>`.



### Step 4: Create section includes (7 files)



**`_includes/hero.html`** — Side-by-side flex layout:

- Left: `img/DSC_8740.JPG` (existing about photo)

- Right: Name heading ("Xiaoli Chen"), role line, 2-3 sentence bio (adapted from `about.md`: developer, photographer, interested in data systems and web dev), credential pills (ORCID, DataCite, RDA, FORCE11 as small pill/tag elements), `{% include social-icons.html %}`



**`_includes/recent-posts.html`** — Adapted from `_layouts/home.html` (lines 13–31):

- Section label "Recent Posts" with rule (reuse `.section-label` / `.section-rule` classes)

- Loop limited to 3 posts (not 5)

- Horizontal card layout instead of vertical list

- "View all posts →" link to `/blog/`



**`_includes/projects.html`** — GitHub API repos:

- Container `<div id="projects-container">` with a loading placeholder

- JS (in `main.js`) fetches `api.github.com/users/xchen101/repos?sort=updated&per_page=6`

- Renders cards showing: repo name, description, primary language, star count

- Reuses existing `.project-card` / `.project-info` CSS patterns where possible

- Fallback: "Visit GitHub profile" link if API fails



**`_includes/experience.html`** — Timeline layout:

- Section label "Experience"

- 3 entries: DataCite (Product Manager), CERN (Researcher), CERN (Research Assistant)

- Each entry: date range left column, role + org + 1-line description right column

- "Download full CV" link placeholder

- All text marked `<!-- TODO: Replace with actual content -->`



**`_includes/education.html`** — Compact rows:

- Section label "Education"

- 3 rows: Sheffield (PhD), Syracuse (MLIS), Beijing (BA)

- Each row: degree, institution, year range

- Placeholder text marked TODO



**`_includes/publications.html`** — Data-driven list:

- Section label "Publications"

- `{% for pub in site.data.publications %}` loop rendering title (as DOI link), venue, year

- "View all on ORCID →" link using `site.orcid` from config



**`_includes/community.html`** — 2-column card grid:

- Section label "Community & Leadership"

- Grid of role cards (RDA Chair, FORCE11 Instructor, APAC Expert, conference participation, RSP program, bilingual content)

- Placeholder text marked TODO



### Step 5: Create `_layouts/landing.html`



```liquid

---

layout: default

---

<section id="about" class="landing-section">

  {% include hero.html %}

</section>

<section id="posts" class="landing-section">

  {% include recent-posts.html %}

</section>

<section id="projects" class="landing-section">

  {% include projects.html %}

</section>

<section id="experience" class="landing-section">

  {% include experience.html %}

</section>

<section id="education" class="landing-section">

  {% include education.html %}

</section>

<section id="publications" class="landing-section">

  {% include publications.html %}

</section>

<section id="community" class="landing-section">

  {% include community.html %}

</section>

```



### Step 6: Update `index.md`



Change frontmatter from `layout: home` to `layout: landing`. Remove any body content (the layout handles everything).



### Step 7: Create `assets/js/main.js` (~80 lines)



Three responsibilities:

1. **Smooth scroll** — Intercept clicks on anchor links (`a[href^="/#"]` and `a[href^="#"]`) when on the landing page. Use `element.scrollIntoView({ behavior: 'smooth' })`.

2. **Active nav highlighting** — `IntersectionObserver` watches `.landing-section` elements, toggles `.active` on corresponding nav links.

3. **GitHub repos** — `fetch('https://api.github.com/users/xchen101/repos?sort=updated&per_page=6')` → build card HTML → inject into `#projects-container`. On error, show fallback link. Only runs if `#projects-container` exists.



No dependencies. Wrapped in `DOMContentLoaded`.



### Step 8: Update `assets/css/style.css`



Append ~150-200 new lines after the existing responsive block:



- **Sticky nav**: `.site-nav { position: sticky; top: 0; z-index: 100; background: #141418; }` + subtle bottom border on scroll (via JS class toggle or just always-on)

- **Section spacing**: `.landing-section { padding: 80px 80px; max-width: 1440px; margin: 0 auto; scroll-margin-top: 80px; }` — reuses existing content width and padding values

- **Hero**: `.hero-split` — flex row, gap 80px (mirrors existing `.about-split` pattern from line 223). Photo 400×520 (same as `.about-photo`). Credential `.pill` tags: small bordered capsules using existing `#2A2A2E` border color

- **Recent posts cards**: Horizontal 3-column grid for post cards (collapses at 768px)

- **Projects grid**: Reuse existing `.project-card`, `.project-info`, `.project-tag` classes. Add `.project-language-dot` for language color indicator

- **Experience timeline**: `.timeline-entry` flex row — `.timeline-date` (180px, right-aligned, `#6B6B6B`) + `.timeline-content` with left border (`#2A2A2E`)

- **Education**: Compact flex rows with degree, institution, year

- **Publications list**: Title links with venue/year metadata in `#6B6B6B`

- **Community grid**: 2-column grid, reuses `.project-card` border/background pattern

- **Back-to-top**: Small link in footer, `#6B6B6B` color

- **Responsive** (append to existing media queries):

  - `@media (max-width: 1024px)`: landing-section padding 56px 40px, hero gap 48px

  - `@media (max-width: 768px)`: all multi-column layouts → single column, hero stacks vertically (photo on top), timeline collapses to single column



### Step 9: Update `_config.yml`



Add: `orcid: "0000-0003-0207-2705"`



---



## Files Summary



| Action | File | Notes |

|--------|------|-------|

| Create | `_data/publications.yml` | Placeholder publication entries |

| Create | `_includes/social-icons.html` | Extracted from default.html |

| Create | `_includes/footer.html` | Extracted from default.html + back-to-top |

| Create | `_includes/hero.html` | Bio adapted from about.md, rest placeholder |

| Create | `_includes/recent-posts.html` | Adapted from home.html loop |

| Create | `_includes/projects.html` | GitHub API container |

| Create | `_includes/experience.html` | Placeholder content |

| Create | `_includes/education.html` | Placeholder content |

| Create | `_includes/publications.html` | Reads publications.yml |

| Create | `_includes/community.html` | Placeholder content |

| Create | `_layouts/landing.html` | Composes all section includes |

| Create | `assets/js/main.js` | Smooth scroll, observer, GitHub fetch |

| Modify | `_layouts/default.html` | Nav links, sticky nav, footer include, script tag |

| Modify | `index.md` | layout: home → layout: landing |

| Modify | `assets/css/style.css` | Append ~150-200 lines for new sections |

| Modify | `_config.yml` | Add orcid |



**Preserved (no changes)**: `blog.md`, `_posts/*`, `about.md`, `_layouts/home.html`, `_layouts/post.html`, `_layouts/page.html`, `_layouts/project.html`, `_projects/*`, `projects.md`



**No longer linked from nav** (but still accessible at their URLs): `about.md` (`/about/`), `projects.md` (`/projects/`)



---



## Verification



1. `bundle exec jekyll serve` → load `localhost:4000`

2. All 7 sections render in correct vertical order below the hero

3. Nav is sticky — stays visible on scroll

4. Click each nav anchor link — smooth scrolls to correct section

5. Scroll through page — active nav link updates via IntersectionObserver

6. Click a post card → navigates to individual post page (e.g. `/2026/04/06/rainy-evenings-and-bokeh-lights.html`)

7. Click "View all posts" → goes to `/blog/`

8. Projects section loads GitHub repo cards (check console for API errors; verify fallback if rate-limited)

9. Navigate to `/blog/`, click a nav anchor link (e.g. "Projects") → navigates to `/#projects` on homepage

10. Resize to 768px → all multi-column layouts collapse to single column, hero stacks vertically

11. Verify `/blog/` and individual post URLs still work unchanged

12. Verify `/about/` and `/projects/` still render (just not in nav)

