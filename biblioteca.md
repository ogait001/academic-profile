---
layout: default
title: La Biblioteca
permalink: /biblioteca/
description: Colección de ensayos filosóficos de Oscar Gaitán que exploran la ontología, la temporalidad, la fenomenología, la antropología metafísica y teología filosófica.
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

/* AISLE INDEX (el catalogo) */
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

/* MOBILE KINDLE-STYLE GRID */
@media (max-width: 640px) {

  .cover-grid {
    grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
    gap: 1rem;
  }

  .cover-card {
    aspect-ratio: 3 / 4;
  }

  .cover-card img {
    object-fit: cover;
    height: 100%;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.12);
  }

  .series-badge{
    font-size:0.6rem;
    left:6px;
    bottom:6px;
  }

  .library-controls {
    margin: 0.8rem 0 1rem 0;
  }

  h1 {
    margin-top: 0.4rem;
    margin-bottom: 0.4rem;
    line-height: 1.2;
  }

  #top + h1 + p,
  h1 + p {
    margin-top: 0.2rem;
    margin-bottom: 0.8rem;
    line-height: 1.45;
  }
}


/* ==========================================================
   GAITAN TOPOLOGY — MEDIEVAL WALNUT & ANTIQUE-GOLD THEME
   Page-scoped: activates only when .medieval-theme-marker exists.
   ========================================================== */
body:has(.medieval-theme-marker) {
  --gt-walnut: #1e0c04;
  --gt-walnut-deep: #120701;
  --gt-walnut-mid: #2a1108;
  --gt-gold: #c99a4b;
  --gt-gold-bright: #e8d4a8;
  --gt-gold-muted: #b58a49;
  --gt-ink: #e2d0ad;
  --gt-line: rgba(140, 80, 30, 0.62);
  --gt-panel: rgba(20, 8, 3, 0.72);
}

body:has(.medieval-theme-marker) .medieval-theme-marker { display: none !important; }
body:has(.medieval-theme-marker) {
  color: var(--gt-ink) !important;
  background:
    radial-gradient(ellipse 70% 42% at 25% 6%, rgba(80,35,10,.52) 0%, transparent 68%),
    radial-gradient(ellipse 62% 58% at 80% 78%, rgba(40,15,5,.62) 0%, transparent 70%),
    linear-gradient(170deg, #1e0c04 0%, #2a1108 22%, #1a0a03 53%, #241008 76%, #160802 100%) !important;
}
body:has(.medieval-theme-marker) .page-content {
  /* Minima's project stylesheet caps this outer element at 900px. Remove that cap
     on these themed pages so the inner frame and book-cover grids can use their
     intended responsive width without changing any other page. */
  width: 100%;
  max-width: none !important;
  margin-inline: auto;
  box-sizing: border-box;
  background: transparent !important;
  color: var(--gt-ink) !important;
}
body:has(.medieval-theme-marker) .page-content > .wrapper:has(.homepage-epigraph) {
  max-width: 1000px;
}
body:has(.medieval-theme-marker) .page-content > .wrapper {
  position: relative;
  box-sizing: border-box;
  width: 100%;
  max-width: 1320px;
  padding: 2rem clamp(1rem, 3.3vw, 2.6rem) 3.25rem;
  color: var(--gt-ink) !important;
  background: linear-gradient(180deg, rgba(18,7,1,.22), rgba(18,7,1,.04));
  border-left: 1px solid rgba(120,72,32,.30);
  border-right: 1px solid rgba(120,72,32,.30);
  font-family: 'EB Garamond', Garamond, Georgia, serif;
  font-size: 1.08rem;
}
body:has(.medieval-theme-marker) .page-content > .wrapper::before {
  content: '❧   ✦   ❧';
  display: block;
  text-align: center;
  color: rgba(180,127,55,.76);
  letter-spacing: .34em;
  font-size: .95rem;
  margin: 0 auto 1.2rem;
}
body:has(.medieval-theme-marker) .site-header,
body:has(.medieval-theme-marker) .site-footer {
  background: rgba(18,7,1,.97) !important;
  color: #cdb27d !important;
  border-color: rgba(120,72,32,.72) !important;
}
body:has(.medieval-theme-marker) .site-header {
  border-top: 4px solid rgba(120,72,32,.9) !important;
  border-bottom: 1px solid rgba(120,72,32,.62) !important;
}
body:has(.medieval-theme-marker) .site-header a,
body:has(.medieval-theme-marker) .site-footer a {
  color: #d8b56e !important;
  text-decoration-color: rgba(200,155,75,.55);
}
body:has(.medieval-theme-marker) .site-header a:hover,
body:has(.medieval-theme-marker) .site-footer a:hover {
  color: #fff0c5 !important;
}
body:has(.medieval-theme-marker) .site-footer .footer-inner {
  border-top: 1px solid rgba(120,72,32,.35);
}
body:has(.medieval-theme-marker) .back-to-top {
  background: #2a1108 !important;
  color: #e8d4a8 !important;
  border: 1px solid rgba(180,127,55,.8);
}
body:has(.medieval-theme-marker) .page-content .wrapper h1,
body:has(.medieval-theme-marker) .page-content .wrapper h2,
body:has(.medieval-theme-marker) .page-content .wrapper h3,
body:has(.medieval-theme-marker) .page-content .wrapper h4 {
  color: var(--gt-gold-bright) !important;
  font-family: 'EB Garamond', Garamond, Georgia, serif !important;
  font-weight: 500;
  text-shadow: 0 1px 8px rgba(0,0,0,.36);
}
body:has(.medieval-theme-marker) .page-content .wrapper h1 {
  font-size: clamp(2rem, 4vw, 3rem);
  line-height: 1.12;
  letter-spacing: .015em;
  margin-top: .4rem;
  margin-bottom: .8rem;
}
body:has(.medieval-theme-marker) .page-content .wrapper h2 {
  border-bottom: 1px solid rgba(120,72,32,.46);
  padding-bottom: .35rem;
  margin-top: 2rem;
}
body:has(.medieval-theme-marker) .page-content .wrapper h3 { color: #d8b56e !important; }
body:has(.medieval-theme-marker) .page-content .wrapper p,
body:has(.medieval-theme-marker) .page-content .wrapper li,
body:has(.medieval-theme-marker) .page-content .wrapper label,
body:has(.medieval-theme-marker) .page-content .wrapper small,
body:has(.medieval-theme-marker) .page-content .wrapper summary {
  color: var(--gt-ink) !important;
}
body:has(.medieval-theme-marker) .page-content .wrapper a {
  color: #d8b56e;
  text-decoration-color: rgba(200,155,75,.48);
  text-underline-offset: .18em;
}
body:has(.medieval-theme-marker) .page-content .wrapper a:hover {
  color: #fff0c5;
  text-decoration-color: #d8b56e;
}
body:has(.medieval-theme-marker) .page-content .wrapper hr,
body:has(.medieval-theme-marker) .section-divider,
body:has(.medieval-theme-marker) .aisle-divider {
  border-color: rgba(120,72,32,.62) !important;
}
body:has(.medieval-theme-marker) .section-divider {
  border-top: 1px solid rgba(120,72,32,.58) !important;
  opacity: .8;
}
body:has(.medieval-theme-marker) .hero-buttons a,
body:has(.medieval-theme-marker) .featured-grid a,
body:has(.medieval-theme-marker) .framework-grid div,
body:has(.medieval-theme-marker) .framework-grid a.framework-pill,
body:has(.medieval-theme-marker) .pill,
body:has(.medieval-theme-marker) .pub-item,
body:has(.medieval-theme-marker) #continueReading {
  background: linear-gradient(145deg, rgba(42,17,8,.96), rgba(20,8,3,.96)) !important;
  color: #e8d4a8 !important;
  border: 1px solid rgba(120,72,32,.72) !important;
  box-shadow: inset 0 0 0 1px rgba(185,133,54,.06), 0 4px 14px rgba(0,0,0,.14);
}
body:has(.medieval-theme-marker) .hero-buttons a:hover,
body:has(.medieval-theme-marker) .featured-grid a:hover,
body:has(.medieval-theme-marker) .framework-grid a.framework-pill:hover,
body:has(.medieval-theme-marker) .pill:hover {
  background: linear-gradient(145deg, #3a1b0c, #241008) !important;
  border-color: rgba(200,155,75,.9) !important;
}
body:has(.medieval-theme-marker) .pub-item,
body:has(.medieval-theme-marker) .pub-gloss .pub-item {
  border-left: 2px solid rgba(140,80,30,.82) !important;
  border-top-color: rgba(120,72,32,.4) !important;
}
body:has(.medieval-theme-marker) .pub-item a strong,
body:has(.medieval-theme-marker) .pub-item summary,
body:has(.medieval-theme-marker) .pub-title {
  color: #e8d4a8 !important;
}
body:has(.medieval-theme-marker) .pub-item summary::before { color: #c99a4b !important; }
body:has(.medieval-theme-marker) .pub-item p,
body:has(.medieval-theme-marker) .pub-abstract { color: #d6c19b !important; }
body:has(.medieval-theme-marker) .homepage-epigraph {
  border-left: 1px solid rgba(140,80,30,.8);
  padding-left: 1rem;
}
body:has(.medieval-theme-marker) .epigraph-text { color: #e2d0ad !important; }
body:has(.medieval-theme-marker) .epigraph-author { color: #bda16b !important; }
body:has(.medieval-theme-marker) .site-author,
body:has(.medieval-theme-marker) .hero-description,
body:has(.medieval-theme-marker) .hero-audience,
body:has(.medieval-theme-marker) .site-subtitle { color: #d2bd95 !important; }
body:has(.medieval-theme-marker) .about-photo img {
  border: 1px solid rgba(140,80,30,.72) !important;
  box-shadow: 0 5px 18px rgba(0,0,0,.35);
}
body:has(.medieval-theme-marker) .aisle-index {
  background: rgba(15,6,2,.78) !important;
  border: 1px solid rgba(120,72,32,.72) !important;
  border-radius: 8px;
  box-shadow: inset 0 0 0 1px rgba(185,133,54,.06);
}
body:has(.medieval-theme-marker) .aisle-index a,
body:has(.medieval-theme-marker) .aisle-index .aisle-code,
body:has(.medieval-theme-marker) .aisle-section h2 .aisle-code { color: #d0a35d !important; }
body:has(.medieval-theme-marker) .shelf-block h3 { color: #cfb581 !important; }
/* Four-column reading grid on wide screens; reduce columns as space narrows. */
body:has(.medieval-theme-marker) .cover-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
  gap: 1.4rem;
}
body:has(.medieval-theme-marker) .cover-card {
  position: relative;
  min-width: 0;
  aspect-ratio: auto !important;
  overflow: visible;
  transition: transform .18s ease;
}
body:has(.medieval-theme-marker) .cover-card:hover {
  transform: translateY(-3px);
}
body:has(.medieval-theme-marker) .cover-card-link {
  display: block;
  position: relative;
  z-index: 1;
  overflow: hidden;
  border-radius: 8px;
  line-height: 0;
}
body:has(.medieval-theme-marker) .cover-card-link img {
  display: block;
  width: 100%;
  height: auto !important;
  aspect-ratio: 2 / 3;
  object-fit: contain;
  border: 1px solid rgba(177,116,49,.84) !important;
  border-radius: 8px;
  box-shadow: 0 7px 20px rgba(0,0,0,.42), 0 0 0 1px rgba(201,154,75,.18);
  transition: border-color .18s ease, box-shadow .18s ease;
}
body:has(.medieval-theme-marker) .cover-card:hover .cover-card-link img,
body:has(.medieval-theme-marker) .cover-card-link:focus-visible img {
  border-color: rgba(215,162,77,.94) !important;
  box-shadow: 0 9px 22px rgba(0,0,0,.46), 0 0 0 1px rgba(201,154,75,.28);
}
body:has(.medieval-theme-marker) .cover-card .series-badge {
  z-index: 2;
}
body:has(.medieval-theme-marker) .cover-preview {
  position: absolute;
  z-index: 3;
  left: 1px;
  right: 1px;
  bottom: 1px;
  max-height: 65%;
  overflow-y: auto;
  padding: .95rem .95rem .85rem;
  background: linear-gradient(180deg, rgba(27,10,3,.97), rgba(12,4,1,.985));
  border-top: 1px solid rgba(215,162,77,.78);
  border-radius: 0 0 7px 7px;
  box-shadow: 0 -8px 22px rgba(0,0,0,.22);
  color: #e8d4a8;
  opacity: 0;
  visibility: hidden;
  transform: translateY(8px);
  transition: opacity .18s ease, transform .18s ease, visibility .18s ease;
}
body:has(.medieval-theme-marker) .cover-preview p {
  margin: 0 0 .72rem;
  color: #e8d9b8 !important;
  font-size: .91rem;
  line-height: 1.48;
  overflow-wrap: anywhere;
}
body:has(.medieval-theme-marker) .cover-preview-read {
  display: inline-block;
  color: #f0d293 !important;
  font-size: .82rem;
  font-weight: 600;
  line-height: 1.4;
  text-decoration: none;
  border-bottom: 1px solid rgba(215,162,77,.6);
  padding-bottom: .12rem;
}
body:has(.medieval-theme-marker) .cover-preview-read:hover,
body:has(.medieval-theme-marker) .cover-preview-read:focus-visible {
  color: #fff0c5 !important;
}
body:has(.medieval-theme-marker) .cover-preview-toggle {
  display: none;
  position: absolute;
  z-index: 5;
  top: .6rem;
  right: .6rem;
  padding: .4rem .66rem;
  border: 1px solid rgba(215,162,77,.82);
  border-radius: 999px;
  background: rgba(18,7,1,.96);
  color: #f0d293;
  font: 600 .75rem/1.25 system-ui, sans-serif;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0,0,0,.35);
}
@media (hover: hover) and (pointer: fine) {
  body:has(.medieval-theme-marker) .cover-card:hover .cover-preview,
  body:has(.medieval-theme-marker) .cover-card-link:focus-visible ~ .cover-preview,
  body:has(.medieval-theme-marker) .cover-preview:focus-within {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }
}
@media (hover: none), (pointer: coarse) {
  body:has(.medieval-theme-marker) .cover-preview-toggle {
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
  body:has(.medieval-theme-marker) .cover-card.preview-open .cover-preview {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }
}
body:has(.medieval-theme-marker) .cover-preview[aria-hidden="false"] {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}
@media (max-width: 1180px) {
  body:has(.medieval-theme-marker) .cover-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
    gap: 1.2rem;
  }
}
@media (max-width: 760px) {
  body:has(.medieval-theme-marker) .cover-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: .9rem;
  }
  body:has(.medieval-theme-marker) .cover-preview {
    padding: .7rem .7rem .65rem;
  }
  body:has(.medieval-theme-marker) .cover-preview p {
    font-size: .82rem;
    line-height: 1.4;
  }
}
@media (max-width: 420px) {
  body:has(.medieval-theme-marker) .cover-grid {
    grid-template-columns: minmax(0, 1fr) !important;
    gap: 1rem;
  }
  body:has(.medieval-theme-marker) .cover-preview p {
    font-size: .9rem;
  }
}
body:has(.medieval-theme-marker) .view-toggle { border-color: rgba(140,80,30,.8) !important; }
body:has(.medieval-theme-marker) .view-toggle button,
body:has(.medieval-theme-marker) .sort-container select {
  background: #1c0a03 !important;
  color: #e2d0ad !important;
  border-color: rgba(140,80,30,.72) !important;
}
body:has(.medieval-theme-marker) .view-toggle button.active {
  background: #5a2020 !important;
  color: #f3dfb1 !important;
}
body:has(.medieval-theme-marker) #continueReading button {
  color: #e8d4a8 !important;
}
body:has(.medieval-theme-marker) .featured-grid a[data-excerpt]::after {
  background: #170802 !important;
  color: #e8d4a8 !important;
  border: 1px solid rgba(140,80,30,.82);
}
@media (max-width: 640px) {
  body:has(.medieval-theme-marker) .page-content > .wrapper {
    padding: 1.35rem 1rem 2.2rem;
    border-left: 0;
    border-right: 0;
  }
  body:has(.medieval-theme-marker) .page-content > .wrapper::before {
    margin-bottom: .75rem;
    letter-spacing: .22em;
  }
  body:has(.medieval-theme-marker) .page-content .wrapper h1 { font-size: 1.9rem; }
}

</style>

<div class="medieval-theme-marker" aria-hidden="true"></div>

<div id="top"></div>

# La Biblioteca

Una colección de ensayos sobre ontología, filosofía del tiempo, metafísica, fenomenología y teología católica.

<div id="continueReading"
     style="margin:1rem 0 1.5rem 0;
            padding:1rem;
            border:1px solid #d1d5db;
            border-radius:8px;
            display:none;">
</div>

<div class="library-controls">
  <div class="view-toggle" role="group" aria-label="Vista">
    <button id="viewAisles" type="button" class="active">Pasillos</button>
    <button id="viewFlat" type="button">Vista plana</button>
  </div>

  <div class="sort-container" id="sortContainer" style="display:none;">
    <label for="sortPosts"><strong>Ordenar por:</strong></label>
    <select id="sortPosts">
      <option value="newest">Más recientes primero</option>
      <option value="oldest">Más antiguos primero</option>
      <option value="az">Título A–Z</option>
      <option value="za">Título Z–A</option>
    </select>
  </div>
</div>

{% assign spanish_posts = site.posts | where: "lang", "es" %}

<nav class="aisle-index" id="aisleIndex" aria-label="Pasillos">
  {% for aisle in site.data.shelves.aisles %}
    {% assign aisle_posts = spanish_posts | where: "shelf", aisle.id %}
    {% assign shelf_total = aisle_posts.size %}
    {% for shelf in aisle.shelves %}
      {% assign shelf_posts = spanish_posts | where: "shelf", shelf.id %}
      {% assign shelf_total = shelf_total | plus: shelf_posts.size %}
    {% endfor %}
    {% if shelf_total > 0 %}
      <a href="#{{ aisle.id }}"><span class="aisle-code">{{ aisle.code }}</span>{{ aisle.name_es }}</a>
    {% endif %}
  {% endfor %}
</nav>

<div id="groupedView">

{% for aisle in site.data.shelves.aisles %}

  {% assign direct_posts = spanish_posts | where: "shelf", aisle.id %}
  {% assign aisle_total = direct_posts.size %}
  {% for shelf in aisle.shelves %}
    {% assign shelf_posts = spanish_posts | where: "shelf", shelf.id %}
    {% assign aisle_total = aisle_total | plus: shelf_posts.size %}
  {% endfor %}

  {% if aisle_total > 0 %}
  <section class="aisle-section" id="{{ aisle.id }}">
    <h2><span class="aisle-code">{{ aisle.code }}</span>{{ aisle.name_es }}</h2>

    {% if direct_posts.size > 0 %}
      {% if direct_posts.first.series %}
        {% assign ordered = direct_posts | sort: "series_order" %}
      {% else %}
        {% assign ordered = direct_posts %}
      {% endif %}
      <div class="cover-grid" id="grid-{{ aisle.id }}">
        {% for post in ordered %}
          {% include cover-card.html post=post lang="es" home=aisle.id index=forloop.index %}
        {% endfor %}
      </div>
    {% endif %}

    {% for shelf in aisle.shelves %}
      {% assign shelf_posts = spanish_posts | where: "shelf", shelf.id %}
      {% if shelf_posts.size > 0 %}
        {% if shelf_posts.first.series %}
          {% assign ordered = shelf_posts | sort: "series_order" %}
        {% else %}
          {% assign ordered = shelf_posts %}
        {% endif %}
        <div class="shelf-block">
          <h3>{{ shelf.name_es }}</h3>
          <div class="cover-grid" id="grid-{{ shelf.id }}">
            {% for post in ordered %}
              {% include cover-card.html post=post lang="es" home=shelf.id index=forloop.index %}
            {% endfor %}
          </div>
        </div>
      {% endif %}
    {% endfor %}

  </section>
  <hr class="aisle-divider">
  {% endif %}

{% endfor %}

{% assign unshelved = spanish_posts | where_exp: "p", "p.shelf == nil" %}
{% if unshelved.size > 0 %}
  <section class="aisle-section" id="unshelved">
    <h2><span class="aisle-code">—</span>Sin clasificar</h2>
    <div class="cover-grid" id="grid-unshelved">
      {% for post in unshelved %}
        {% include cover-card.html post=post lang="es" home="unshelved" index=forloop.index %}
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
      '<strong>Continuar donde lo dejaste</strong>' +
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

<script>
/* Accessible excerpt previews: hover/focus on desktop, explicit toggle on touch. */
document.querySelectorAll(".cover-card").forEach(function (card) {
  const panel = card.querySelector(".cover-preview");
  const toggle = card.querySelector(".cover-preview-toggle");
  if (!panel || !toggle) return;

  const fineHover = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  const setOpenState = function (open) {
    panel.setAttribute("aria-hidden", String(!open));
    toggle.setAttribute("aria-expanded", String(open));
    toggle.textContent = open ? toggle.dataset.labelOpen : toggle.dataset.labelClosed;
  };

  toggle.addEventListener("click", function (event) {
    event.preventDefault();
    event.stopPropagation();
    const open = !card.classList.contains("preview-open");
    card.classList.toggle("preview-open", open);
    setOpenState(open);
  });

  if (fineHover) {
    card.addEventListener("pointerenter", function () { setOpenState(true); });
    card.addEventListener("pointerleave", function () {
      window.setTimeout(function () {
        if (!card.matches(":hover") && !card.contains(document.activeElement) && !card.classList.contains("preview-open")) {
          setOpenState(false);
        }
      }, 0);
    });
  }

  card.addEventListener("focusin", function (event) {
    /* On touchscreens, focusing the toggle should not open it before activation. */
    if (!fineHover && event.target === toggle && !card.classList.contains("preview-open")) return;
    setOpenState(true);
  });
  card.addEventListener("focusout", function () {
    window.setTimeout(function () {
      const focused = card.contains(document.activeElement);
      const hovered = fineHover && card.matches(":hover");
      const pinned = card.classList.contains("preview-open");
      setOpenState(focused || hovered || pinned);
    }, 0);
  });
});
</script>
