---
layout: default
title: Essays
permalink: /essays/
---

<div id="top"></div>

# Essays

A complete archive of philosophical essays by Oscar Gaitan.

<ul style="list-style: none; padding-left: 0;">
{% for post in site.posts %}
  <li style="margin-bottom: 2.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid #ddd;">

    <a href="{{ post.url | relative_url }}" style="font-size: 1.2rem; font-weight: bold; text-decoration: none;">
      {{ post.title }}
    </a>

    <br>

    <small style="color: #666;">
      {{ post.date | date: "%B %d, %Y" }}
    </small>

    {% if post.excerpt %}
      <p style="margin-top: 0.75rem; line-height: 1.6; color: #444;">
        {{ post.excerpt }}
      </p>
    {% else %}
      <p style="margin-top: 0.75rem; line-height: 1.6; color: #444;">
        {{ post.content | strip_html | truncatewords: 40 }}
      </p>
    {% endif %}

    {% if post.lang == "es" %}
      <small><em>Spanish edition</em></small>
    {% endif %}

  </li>
{% endfor %}
</ul>

<p style="text-align: right; margin-top: 2rem; font-size: 0.95rem;">
  <a href="#top">↑ Back to Top</a>
</p>
