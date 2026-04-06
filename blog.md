---
layout: page
title: All Posts
permalink: /blog/
---

<div class="archive-list">
  {% for post in site.posts %}
  <article class="post-entry">
    <div class="post-text">
      <span class="post-date">{{ post.date | date: "%B %-d, %Y" }}</span>
      <h2 class="post-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      {% if post.excerpt %}
      <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
      {% endif %}
    </div>
    {% if post.image %}
    <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="post-thumb">
    {% endif %}
  </article>
  {% unless forloop.last %}<div class="post-rule"></div>{% endunless %}
  {% endfor %}
</div>
