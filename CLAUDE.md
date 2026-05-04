# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal website for Xiaoli Chen — a Jekyll-based static site hosted on GitHub Pages at https://xchen101.github.io. Photography-focused, minimalist dark theme with no JavaScript.

## Local Development

```bash
# Serve locally (requires Ruby + Jekyll gem installed)
jekyll serve

# Build without serving
jekyll build
```

No Gemfile exists — the site relies on GitHub Pages' bundled Jekyll and minima theme. Deploy by pushing to the `master` branch; GitHub Pages builds automatically.

## Architecture

- **Theme**: Declares `minima` in `_config.yml` but fully overrides it with custom layouts and CSS
- **Layouts** (`_layouts/`): `default.html` (base with nav/footer) → `landing.html` (single-page home), `post.html`, `page.html`
- **Includes** (`_includes/`): landing-page sections — `hero.html`, `recent-posts.html`, `projects.html`, `experience.html`, `education.html`, `publications.html`, `community.html`, `now.html`, `footer.html`, `social-icons.html`
- **Single CSS file**: `assets/css/style.css` — no SCSS, no preprocessor
- **No JavaScript** anywhere in the site

## Content

- **Posts**: `_posts/` — standard Jekyll naming (`YYYY-MM-DD-title.md`), frontmatter includes `layout`, `title`, `date`, optional `image`
- **Pages**: `index.md` (single-page landing) and `blog.md` (archive at `/blog/`)
- **Data** (`_data/`): landing-page sections are populated from YAML — `projects.yml` (repo cards), `publications.yml`, `now.yml`. Edit these to change site content; do not look for `_projects/` collection (removed).
- **Images**: `/img/` — high-quality JPGs used in posts, hero, and about section

## Design System

The file `personal-website-design-brief.md` documents the full design system. Key constraints:

- **Dark theme**: background `#141418`, primary text `#E0E0E0`, headings `#F0F0F0`
- **Typography**: Space Grotesk (headings, 300–700), IBM Plex Sans (body, 300–600) via Google Fonts
- **Image treatment**: CSS filters `saturate(0.7–0.8)` and `brightness(0.75)` for muted film aesthetic
- **Responsive breakpoints**: 1024px and 768px — grid layouts collapse from 2-column to 1-column at 768px
- **Social links**: Inline SVG icons in footer (GitHub, LinkedIn, Instagram, Bluesky) — configured in `_config.yml`
