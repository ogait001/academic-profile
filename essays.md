---
layout: default
title: Essays
permalink: /essays/
---

# Essays

A complete archive of philosophical essays by Oscar Gaitan.

<ul>
{% for post in site.posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <small>— {{ post.date | date: "%B %d, %Y" }}</small>
  </li>
{% endfor %}
</ul>
