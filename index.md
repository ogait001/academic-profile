---
layout: default
---

## Independent Catholic Philosophical Research

<p class="site-intro">
This site presents original research in Catholic theology, metaphysics, ontology, philosophy of time, phenomenology, and metaphysical anthropology, including works associated with <em>The Lemniscate of Time: A Geometric Meditation on Eternity and Temporal Succession</em>.
</p>

<h2 class="essays-heading">Philosophical Essays</h2>

<h2 class="essays-heading">English Essays</h2>

<ul class="post-list">
{% assign english_posts = site.posts | where: "lang", "en" | sort: "date" | reverse %}
{% for post in english_posts %}
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

<h2 class="essays-heading">Ensayos en Español</h2>

<ul class="post-list">
{% assign spanish_posts = site.posts | where: "lang", "es" | sort: "date" | reverse %}
{% for post in spanish_posts %}
  <li>
    <span class="post-meta">{{ post.date | date: "%-d %b %Y" }}</span>
    <h3>
      <a class="post-link" href="{{ post.url | relative_url }}">
        {{ post.title }}
      </a>
    </h3>
  </li>
{% endfor %}
</ul>
