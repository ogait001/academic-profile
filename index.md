---
layout: default
---

# Oscar Gaitan

## Independent Catholic Philosophical Research

This site collects philosophical essays in **Catholic theology, metaphysics, ontology, philosophy of time, phenomenology, and metaphysical anthropology**, including works associated with **The Lemniscate of Time**.

## Philosophical Essays

<ul class="post-list">
{% assign sorted_posts = site.posts %}
{% for post in sorted_posts %}
  <li>
    <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>
    <h3>
      <a class="post-link" href="{{ post.url | relative_url }}">
        {{ post.title }}
      </a>
    </h3>
  </li>
{% endfor %}
</ul>
