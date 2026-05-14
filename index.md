---
layout: default
---

## Independent Catholic Philosophical Research

<p class="site-intro">
This site collects philosophical essays in Catholic theology, metaphysics, ontology, philosophy of time, phenomenology, and metaphysical anthropology, including works associated with <em>The Lemniscate of Time: A Geometric Meditation on Eternity and Temporal Succession</em>.
</p>

<h2 class="essays-heading">Philosophical Essays</h2>

<ul class="post-list">
{% for post in site.posts %}
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
