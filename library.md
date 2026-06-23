---
layout: default
title: The Library
permalink: /library/
description: Collection of  philosophical essays by Oscar Gaitan exploring ontology, temporality, phenomenology, metaphysical anthropology, and philosophical theology.
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
.cover-grid{
display:grid;
grid-template-columns:repeat(auto-fill,minmax(220px,1fr));
gap:1.5rem;
margin-top:2rem;
}

.cover-card{
display:block;
transition:transform .15s ease;
}

.cover-card:hover{
transform:translateY(-4px);
}

.cover-card img{
width:100%;
height:auto;
display:block;
border-radius:8px;
box-shadow:0 4px 12px rgba(0,0,0,.15);
}
/* MOBILE GRID (required) */
@media (max-width: 640px) {
  .cover-grid {
    grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
    gap: 1rem;
  }
}
@media (max-width: 640px) {

  /* Reduce card height for a Kindle-like feel */
  .cover-card {
    aspect-ratio: 3 / 4;
  }

  /* Make images fill the new aspect ratio cleanly */
  .cover-card img {
    object-fit: cover;
    height: 100%;
  }

  /* Tighten spacing between rows */
  .cover-grid {
    gap: 0.75rem;
    margin-top: 1.2rem;
  }
}
@media (max-width: 640px) {

  /* Reduce top spacing for a more app-like feel */
  h1 {
    margin-top: 0.4rem;
    margin-bottom: 0.4rem;
    line-height: 1.2;
  }

  /* Tighten the description paragraph */
  #top + h1 + p,
  h1 + p {
    margin-top: 0.2rem;
    margin-bottom: 0.8rem;
    line-height: 1.45;
  }

  /* Reduce spacing above the grid */
  .sort-container {
    margin: 1rem 0 1.2rem 0;
  }
}
</style>

<div id="top"></div>

# The Library

A collection of philosophical essays in ontology, philosophy of time, metaphysics, phenomenology, and Catholic theology.

<div id="continueReading"
     style="margin:1rem 0 1.5rem 0;
            padding:1rem;
            border:1px solid #d1d5db;
            border-radius:8px;
            display:none;">
</div>

<div class="sort-container">
  <label for="sortPosts"><strong>Sort by:</strong></label>

  <select id="sortPosts">
    <option value="newest">Newest First</option>
    <option value="oldest">Oldest First</option>
    <option value="az">Title A–Z</option>
    <option value="za">Title Z–A</option>
  </select>
</div>


<div id="essayList" class="cover-grid">

{% assign english_posts = site.posts | where: "lang", "en" %}

{% for post in english_posts %}

<a href="{{ post.url | relative_url }}"
   class="cover-card essay-link"
   data-title="{{ post.title | downcase }}"
   data-date="{{ post.date | date: '%Y%m%d' }}">

  <img
    src="{{ '/assets/covers/' | append: post.slug | append: '.png' | relative_url }}"
    alt="{{ post.title }}"
    loading="lazy">

</a>

{% endfor %}

</div>

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
document.querySelectorAll(".essay-link").forEach(link => {

  link.addEventListener("click", function() {

    const essayTitle = this.textContent.trim();

    localStorage.setItem("lastEssayTitle", essayTitle);
    localStorage.setItem("lastEssayUrl", this.href);

    
  });

});

const lastEssayTitle = localStorage.getItem("lastEssayTitle");
const lastEssayUrl = localStorage.getItem("lastEssayUrl");

if (lastEssayTitle && lastEssayUrl) {

  const box = document.getElementById("continueReading");

  box.style.display = "block";

  box.innerHTML =
    '<strong>Continue Reading</strong><br><br>' +
    '<a href="' + lastEssayUrl + '">' +
    lastEssayTitle +
    '</a>';
}

});
</script>

