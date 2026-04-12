# Xiaoli Chen's Personal Website

A minimalist, photography-focused personal website built with Jekyll and hosted on GitHub Pages. Dark theme with no JavaScript dependencies.

**Live at**: https://xchen101.github.io

## Features

- Single-page landing with modular component architecture
- Blog archive and project portfolio
- Responsive design (desktop, tablet, mobile)
- Photography-focused with custom image treatment (muted saturated aesthetic)
- Dark theme with carefully chosen typography
- Zero JavaScript (uses CSS for all styling and layout)

## Local Development

### Prerequisites
- Ruby (Jekyll is Ruby-based)
- Jekyll gem

### Running Locally

```bash
jekyll serve
```

The site will be available at `http://localhost:4000`.

To build without serving:
```bash
jekyll build
```

## Project Structure

```
├── _config.yml           # Jekyll configuration
├── _layouts/             # Layout templates
│   ├── default.html      # Base layout with nav/footer
│   ├── landing.html      # Single-page landing
│   ├── post.html         # Blog post template
│   └── project.html      # Project template
├── _includes/            # Reusable components
│   ├── hero.html         # Hero section
│   ├── projects.html     # Project grid
│   ├── footer.html       # Footer with social icons
│   └── ...               # Other sections
├── _data/                # YAML data files
│   ├── now.yml           # "Now" page content
│   ├── projects.yml      # Project metadata
│   └── publications.yml  # Publications list
├── _posts/               # Blog posts (Jekyll format: YYYY-MM-DD-title.md)
├── assets/
│   ├── css/style.css     # Single CSS file (no SCSS/preprocessor)
│   └── js/main.js        # Interactive functionality
├── img/                  # Images for posts and site
└── index.md              # Home page
```

## Design System

See `personal-website-design-brief.md` for complete design documentation.

**Key constraints**:
- Dark theme: `#141418` background, `#E0E0E0` body text, `#F0F0F0` headings
- Fonts: Space Grotesk (headings), IBM Plex Sans (body) via Google Fonts
- Image filters: `saturate(0.7-0.8)` and `brightness(0.75)` for muted aesthetic
- Breakpoints: 1024px and 768px

## Deployment

Push to the `master` branch and GitHub Pages will automatically build and deploy. No manual build step required.

## Content Management

### Blog Posts
Create new file in `_posts/` with format: `YYYY-MM-DD-title.md`
```yaml
---
layout: post
title: Post Title
date: YYYY-MM-DD
image: /img/optional-image.jpg
---
```

### Projects
Add entry to `_data/projects.yml` or create files in `_projects/` collection.

## License

© 2024 Xiaoli Chen. All rights reserved.
