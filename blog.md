---
layout: default
title: Field notes
permalink: /blog/
---

<div class="blog-archive">

  <header class="blog-header">
    <div class="blog-breadcrumb">
      <a href="{{ '/' | relative_url }}">← Back to home</a>
      <span class="blog-breadcrumb-sep">/</span>
      <span class="blog-breadcrumb-current">Field notes archive</span>
    </div>

    <div class="blog-header-body">
      <div class="blog-header-text">
        <h1 class="blog-title">Field notes</h1>
        <p class="blog-subtitle">Short essays on photography, the city, and the quiet rhythms of working in open science. Written irregularly, usually after a long walk.</p>
      </div>
      <div class="blog-count">
        <div class="blog-count-num">{{ site.posts | size | prepend: '0' | slice: -2, 2 }}</div>
        <div class="blog-count-label">posts · {{ site.time | date: '%Y' }}</div>
      </div>
    </div>
  </header>

  {% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
  {% for year in posts_by_year %}
  <div class="blog-year-group">
    <div class="year-divider">
      <div class="year-marker">{{ year.name }}</div>
      <div class="year-meta">
        <div class="year-label">{% if year.name == site.time | date: '%Y' %}This year{% else %}Archive{% endif %}</div>
        <div class="year-range">{{ year.items | size }} entries</div>
      </div>
    </div>

    <div class="blog-posts">
      {% for post in year.items %}
      <a class="blog-post-row" href="{{ post.url | relative_url }}">
        <div class="blog-post-date">
          <div class="blog-post-date-main">{{ post.date | date: "%d %b" }}</div>
          <div class="blog-post-read">{{ post.content | number_of_words | divided_by: 200 | plus: 1 }} min read</div>
        </div>
        <div class="blog-post-main">
          <h2 class="blog-post-title">{{ post.title }}</h2>
          <p class="blog-post-excerpt">{{ post.excerpt | strip_html | truncatewords: 40 }}</p>
          {% if post.tags %}
          <div class="blog-post-tags">
            {% for tag in post.tags %}<span class="blog-tag">{{ tag }}</span>{% endfor %}
          </div>
          {% endif %}
        </div>
        {% if post.image %}
        <div class="blog-post-thumb" style="background-image: url('{{ post.image | relative_url }}');"></div>
        {% else %}
        <div class="blog-post-thumb blog-post-thumb-empty"></div>
        {% endif %}
      </a>
      {% endfor %}
    </div>
  </div>
  {% endfor %}

  <div class="blog-end">
    <div class="blog-end-rule"></div>
    <span class="blog-end-label">End of archive · <a href="{{ site.substack_url }}">Subscribe on Substack →</a></span>
    <div class="blog-end-rule"></div>
  </div>

</div>
