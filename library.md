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
  margin: 0;
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
margin-top:1.2rem;
}

.cover-card{
display:block;
position:relative;
transition:transform .15s ease;
}

.cover-card:hover{
transform:translateY(-4px);
}

.cover-card img{
width:100%;
height:auto;
aspect-ratio:2/3;
object-fit:cover;
display:block;
border-radius:8px;
box-shadow:0 4px 12px rgba(0,0,0,.15);
}

/* SERIES BADGE — small pill over the cover foot */
.series-badge{
  position:absolute;
  left:8px;
  bottom:8px;
  padding:2px 8px;
  border-radius:999px;
  background:rgba(20,12,6,0.72);
  border:1px solid rgba(232,214,178,0.35);
  color:#e8d6b2;
  font-size:0.68rem;
  letter-spacing:0.3px;
  white-space:nowrap;
  pointer-events:none;
}

/* VIEW TOGGLE + CONTROLS ROW */
.library-controls{
  margin:1.2rem 0 1.6rem 0;
  display:flex;
  flex-wrap:wrap;
  align-items:center;
  gap:0.8rem;
}

.view-toggle{
  display:inline-flex;
  border:1px solid #d1d5db;
  border-radius:999px;
  overflow:hidden;
}

.view-toggle button{
  border:none;
  background:#ffffff;
  color:#374151;
  padding:0.35rem 0.9rem;
  font-size:0.85rem;
  cursor:pointer;
}

.view-toggle button.active{
  background:#2563eb;
  color:#ffffff;
}

/* AISLE INDEX (the card catalog) */
.aisle-index{
  margin:0 0 1.5rem 0;
  padding:0.9rem 1rem;
  border:1px solid #e5e7eb;
  border-radius:10px;
  background:#faf7f2;
}

.aisle-index a{
  display:inline-block;
  margin:0.15rem 0.6rem 0.15rem 0;
  font-size:0.9rem;
  color:#7b5e3b;
  text-decoration:none;
}

.aisle-index a:hover{
  color:#5c452c;
  text-decoration:underline;
}

.aisle-index .aisle-code{
  font-variant:small-caps;
  letter-spacing:0.5px;
  color:#9c8563;
  margin-right:0.25rem;
}

/* AISLE + SHELF HEADINGS */
.aisle-section{
  margin-top:2.6rem;
  scroll-margin-top:0.75rem;
}

.aisle-section h2{
  margin-bottom:0.2rem;
  line-height:1.25;
}

.aisle-section h2 .aisle-code{
  font-size:0.8em;
  color:#9c8563;
  letter-spacing:1px;
  margin-right:0.5rem;
}

.shelf-block h3{
  margin:1.6rem 0 0 0;
  font-size:1.02rem;
  color:#4b5563;
  font-weight:600;
}

.aisle-divider{
  width:60%;
  margin:2.4rem auto 0 auto;
  border:0;
  border-top:1px solid #e5e7eb;
  opacity:0.7;
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
    margin-top: 1rem;
  }

  .series-badge{
    font-size:0.6rem;
    left:6px;
    bottom:6px;
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

  .library-controls {
    margin: 0.8rem 0 1rem 0;
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

<div class="library-controls">
  <div class="view-toggle" role="group" aria-label="View">
    <button id="viewAisles" type="button" class="active">Aisles</button>
    <button id="viewFlat" type="button">Flat view</button>
  </div>

  <div class="sort-container" id="sortContainer" style="display:none;">
    <label for="sortPosts"><strong>Sort by:</strong></label>
    <select id="sortPosts">
      <option value="newest">Newest First</option>
      <option value="oldest">Oldest First</option>
      <option value="az">Title A–Z</option>
      <option value="za">Title Z–A</option>
    </select>
  </div>
</div>

{% assign english_posts = site.posts | where: "lang", "en" %}

<nav class="aisle-index" id="aisleIndex" aria-label="Aisles">
  {% for aisle in site.data.shelves.aisles %}
    {% assign aisle_posts = english_posts | where: "shelf", aisle.id %}
    {% assign shelf_total = aisle_posts.size %}
    {% for shelf in aisle.shelves %}
      {% assign shelf_posts = english_posts | where: "shelf", shelf.id %}
      {% assign shelf_total = shelf_total | plus: shelf_posts.size %}
    {% endfor %}
    {% if shelf_total > 0 %}
      <a href="#{{ aisle.id }}"><span class="aisle-code">{{ aisle.code }}</span>{{ aisle.name_en }}</a>
    {% endif %}
  {% endfor %}
</nav>

<div id="groupedView">

{% for aisle in site.data.shelves.aisles %}

  {% assign direct_posts = english_posts | where: "shelf", aisle.id %}
  {% assign aisle_total = direct_posts.size %}
  {% for shelf in aisle.shelves %}
    {% assign shelf_posts = english_posts | where: "shelf", shelf.id %}
    {% assign aisle_total = aisle_total | plus: shelf_posts.size %}
  {% endfor %}

  {% if aisle_total > 0 %}
  <section class="aisle-section" id="{{ aisle.id }}">
    <h2><span class="aisle-code">{{ aisle.code }}</span>{{ aisle.name_en }}</h2>

    {% if direct_posts.size > 0 %}
      {% if direct_posts.first.series %}
        {% assign ordered = direct_posts | sort: "series_order" %}
      {% else %}
        {% assign ordered = direct_posts %}
      {% endif %}
      <div class="cover-grid" id="grid-{{ aisle.id }}">
        {% for post in ordered %}
          {% include cover-card.html post=post lang="en" home=aisle.id index=forloop.index %}
        {% endfor %}
      </div>
    {% endif %}

    {% for shelf in aisle.shelves %}
      {% assign shelf_posts = english_posts | where: "shelf", shelf.id %}
      {% if shelf_posts.size > 0 %}
        {% if shelf_posts.first.series %}
          {% assign ordered = shelf_posts | sort: "series_order" %}
        {% else %}
          {% assign ordered = shelf_posts %}
        {% endif %}
        <div class="shelf-block">
          <h3>{{ shelf.name_en }}</h3>
          <div class="cover-grid" id="grid-{{ shelf.id }}">
            {% for post in ordered %}
              {% include cover-card.html post=post lang="en" home=shelf.id index=forloop.index %}
            {% endfor %}
          </div>
        </div>
      {% endif %}
    {% endfor %}

  </section>
  <hr class="aisle-divider">
  {% endif %}

{% endfor %}

{% assign unshelved = english_posts | where_exp: "p", "p.shelf == nil" %}
{% if unshelved.size > 0 %}
  <section class="aisle-section" id="unshelved">
    <h2><span class="aisle-code">—</span>Unshelved</h2>
    <div class="cover-grid" id="grid-unshelved">
      {% for post in unshelved %}
        {% include cover-card.html post=post lang="en" home="unshelved" index=forloop.index %}
      {% endfor %}
    </div>
  </section>
{% endif %}

</div>

<div id="flatView" style="display:none;">
  <div id="essayList" class="cover-grid"></div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function () {

  const sortSelect    = document.getElementById("sortPosts");
  const sortContainer = document.getElementById("sortContainer");
  const grouped       = document.getElementById("groupedView");
  const flat          = document.getElementById("flatView");
  const flatGrid      = document.getElementById("essayList");
  const aisleIndex    = document.getElementById("aisleIndex");
  const btnAisles     = document.getElementById("viewAisles");
  const btnFlat       = document.getElementById("viewFlat");

  function allCards() {
    return Array.from(document.querySelectorAll(".cover-card"));
  }

  function sortFlat() {
    const items = Array.from(flatGrid.children);
    items.sort((a, b) => {
      const titleA = a.dataset.title, titleB = b.dataset.title;
      const dateA  = a.dataset.date,  dateB  = b.dataset.date;
      switch (sortSelect.value) {
        case "oldest": return dateA.localeCompare(dateB);
        case "az":     return titleA.localeCompare(titleB);
        case "za":     return titleB.localeCompare(titleA);
        default:       return dateB.localeCompare(dateA);
      }
    });
    items.forEach(item => flatGrid.appendChild(item));
  }

  function showFlat() {
    allCards().forEach(card => flatGrid.appendChild(card));
    sortFlat();
    grouped.style.display = "none";
    aisleIndex.style.display = "none";
    flat.style.display = "block";
    sortContainer.style.display = "block";
    btnFlat.classList.add("active");
    btnAisles.classList.remove("active");
    localStorage.setItem("libraryView", "flat");
  }

  function showAisles() {
    allCards()
      .sort((a, b) => Number(a.dataset.homeIndex) - Number(b.dataset.homeIndex))
      .forEach(card => {
        const home = document.getElementById("grid-" + card.dataset.home);
        if (home) home.appendChild(card);
      });
    flat.style.display = "none";
    sortContainer.style.display = "none";
    grouped.style.display = "block";
    aisleIndex.style.display = "block";
    btnAisles.classList.add("active");
    btnFlat.classList.remove("active");
    localStorage.setItem("libraryView", "aisles");
  }

  btnFlat.addEventListener("click", showFlat);
  btnAisles.addEventListener("click", showAisles);

  sortSelect.addEventListener("change", function () {
    sortFlat();
    localStorage.setItem("essaySort", sortSelect.value);
  });

  const savedSort = localStorage.getItem("essaySort");
  if (savedSort) { sortSelect.value = savedSort; }

  if (localStorage.getItem("libraryView") === "flat") { showFlat(); }

  document.querySelectorAll(".essay-link").forEach(link => {
    link.addEventListener("click", function () {
      const img = this.querySelector("img");
      const essayTitle = img ? img.alt : this.dataset.title;
      localStorage.setItem("lastEssayTitle", essayTitle);
      localStorage.setItem("lastEssayUrl", this.href);
    });
  });

  const lastEssayTitle = localStorage.getItem("lastEssayTitle");
  const lastEssayUrl   = localStorage.getItem("lastEssayUrl");
  if (lastEssayTitle && lastEssayUrl) {
    const box = document.getElementById("continueReading");
    box.style.display = "block";
    box.innerHTML =
      '<div style="display:flex;justify-content:space-between;align-items:baseline;gap:1rem;">' +
      '<strong>Continue Reading</strong>' +
      '<button id="dismissContinue" type="button" aria-label="Dismiss" ' +
      'style="border:none;background:none;color:#6b7280;cursor:pointer;font-size:1rem;padding:0;line-height:1;">&#10005;</button>' +
      '</div><br>' +
      '<a href="' + lastEssayUrl + '">' +
      lastEssayTitle +
      '</a>';
    document.getElementById("dismissContinue").addEventListener("click", function () {
      localStorage.removeItem("lastEssayTitle");
      localStorage.removeItem("lastEssayUrl");
      box.style.display = "none";
    });
  }

});
</script>
