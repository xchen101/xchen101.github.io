---
layout: page
title: Projects
permalink: /projects/
---

<div class="projects-header">
  <h1>Projects</h1>
  <p>A selection of things I've built, explored, or contributed to.</p>
</div>

<div class="projects-grid">
  {% assign sorted_projects = site.projects | sort: "order" %}
  {% for project in sorted_projects %}
  <a href="{{ project.url | relative_url }}" class="project-card-link">
    <div class="project-card">
      <div class="project-thumb"><span>{{ project.order | prepend: '00' | slice: -2, 2 }}</span></div>
      <div class="project-info">
        <span class="project-category">{{ project.category }}</span>
        <span class="project-name">{{ project.title }}</span>
        <span class="project-desc">{{ project.excerpt | strip_html | truncatewords: 25 }}</span>
        {% if project.tags %}
        <div class="project-tags">
          {% for tag in project.tags %}
          <span class="project-tag">{{ tag }}</span>
          {% endfor %}
        </div>
        {% endif %}
      </div>
    </div>
  </a>
  {% endfor %}
</div>
