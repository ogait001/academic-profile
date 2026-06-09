---
layout: default
title: Essays
permalink: /essays/
---

<style>
.lang-links{
  margin-top: 1rem;
  display: flex;
  gap: 0.5rem;
}

.lang-pill{
  display: inline-block;
  padding: 0.35rem 0.8rem;
  border: 1px solid #d1d5db;
  border-radius: 999px;
  text-decoration: none;
  font-size: 0.85rem;
  color: #374151;
  background: #ffffff;
  transition: all 0.15s ease;
}

.lang-pill:hover{
  background: #f9fafb;
  border-color: #9ca3af;
}

.lang-pill.active{
  background: #2563eb;
  color: white;
  border-color: #2563eb;
}

.sort-container{
  margin: 1.5rem 0 2rem 0;
}

.sort-container select{
  padding: 0.35rem 0.6rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  background: white;
}
</style>

<div id="top"></div>

# Essays

A bilingual archive of philosophical essays in ontology, philosophy of time, metaphysics, phenomenology, and Catholic theology.

<div class="sort-container">
  <label for="sortPosts"><strong>Sort by:</strong></label>

  <select id="sortPosts">
    <option value="newest">Newest First</option>
    <option value="oldest">Oldest First</option>
    <option value="az">Title A–Z</option>
    <option value="za">Title Z–A</option>
  </select>
</div>

<ul id="essayList" style="list-style: none; padding-left: 0;">
{% for post in site.posts %}
  {% if post.lang == "en" %}
  <li
    data-title="{{ post.title | downcase }}"
    data-date="{{ post.date | date: '%Y%m%d' }}"
    style="margin-bottom: 2.5rem; padding-bottom: 1.5rem; border-bottom: 1px solid #ddd;"
  >


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

{% if post.translation_url %}
  <div class="lang-links">
    {% if post.lang == "en" %}
      <a href="{{ post.url | relative_url }}" class="lang-pill active">English</a>
      <a href="{{ post.translation_url }}" class="lang-pill">Español</a>
    {% elsif post.lang == "es" %}
      <a href="{{ post.translation_url }}" class="lang-pill">English</a>
      <a href="{{ post.url | relative_url }}" class="lang-pill active">Español</a>
    {% endif %}
  </div>
{% endif %}


  </li>
  {% endif %}
{% endfor %}
</ul>

<script>
document.addEventListener("DOMContentLoaded", function () {

  const sortSelect = document.getElementById("sortPosts");
  const list = document.getElementById("essayList");

  sortSelect.addEventListener("change", function () {

    const items = Array.from(list.children);

    items.sort((a, b) => {

      const titleA = a.dataset.title;
      const titleB = b.dataset.title;

      const dateA = a.dataset.date;
      const dateB = b.dataset.date;

      switch (sortSelect.value) {

        case "oldest":
          return dateA.localeCompare(dateB);

        case "az":
          return titleA.localeCompare(titleB);

        case "za":
          return titleB.localeCompare(titleA);

        default:
          return dateB.localeCompare(dateA);
      }
    });

    items.forEach(item => list.appendChild(item));
    localStorage.setItem("essaySort", sortSelect.value);
  });
 const savedSort = localStorage.getItem("essaySort");

if (savedSort) {
  sortSelect.value = savedSort;
}

sortSelect.dispatchEvent(new Event("change"));

});
</script>

