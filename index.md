---
layout: default
title: Philosophy & Catholic Thought
author: Oscar Gaitan
description: Oscar Gaitan is a Nicaraguan American philosopher and independent researcher in ontology, temporality, phenomenology, metaphysical anthropology, and Catholic theology.
---

<div class="medieval-theme-marker" aria-hidden="true"></div>


<h1>Philosophy & Catholic Thought</h1>

<p style="
  font-size:1.55rem;
  font-weight:600;
  color:#111;
  margin-top:0.35rem;
  margin-bottom:1.25rem;
">
  Oscar Gaitan
</p>

<p style="
  color:#374151;
  font-size:1.1rem;
  margin:0.4rem 0 1.2rem 0;
">
  Independent research in ontology, temporality, phenomenology, and Catholic theology.
</p>
<div class="homepage-epigraph">
  <p class="epigraph-text">
    Converso con el hombre que siempre va conmigo<br>
    —quien habla solo espera hablar a Dios un día—
  </p>
  <p class="epigraph-author">
    — Antonio Machado, <em>&#8220;Retrato&#8221;</em>, <em>Campos de Castilla</em> (1912)
  </p>
</div>
<div class="hero-buttons">
  <a href="/library/">Library</a>
  <a href="/biblioteca/">Biblioteca</a>
  <a href="https://philpeople.org/profiles/oscar-gaitan">PhilPeople</a>
  <a href="https://scholar.google.com/citations?user=huV-MLsAAAAJ">Google Scholar</a>
</div>


<style>
.recent-pubs {
  margin-top: 1.5rem;
}

.pub-item {
  border: 1px solid #d1d5db;
  border-radius: 10px;
  padding: 0.9rem 1rem;
  margin-bottom: 1rem;
  background: #ffffff;
}

.pub-item summary {
  cursor: pointer;
  list-style: none;
  outline: none;
}

.pub-item summary::-webkit-details-marker {
  display: none;
}

.pub-item summary::before {
  content: "▸ ";
  color: #6b7280;
  font-weight: bold;
  margin-right: 4px;
}

.pub-item[open] summary::before {
  content: "▾ ";
}

.pub-item a {
  text-decoration: none;
}

.pub-item a strong {
  font-size: 1.05rem;
}

.pub-abstract {
  margin-top: 1rem;
  line-height: 1.65;
  color: #374151;
}

  .about-card{
  display:flex;
  gap:2rem;
  align-items:flex-start;
  margin-top:1rem;
}

.about-photo img{
  width:190px;
  border-radius:10px;
  display:block;
  border:1px solid #d1d5db;
}

.about-content{
  flex:1;
}

.about-content h2{
  margin-top:0;
}

.about-content h3{
  margin-top:1.75rem;
  margin-bottom:0.75rem;
  font-size:1.35rem;
}

.about-content p{
  line-height:1.7;
  color:#374151;
}

.about-content a{
  color:#2563eb;
  text-decoration:none;
}

.about-content a:hover{
  text-decoration:underline;
}

@media(max-width:700px){
  .about-card{
    flex-direction:column;
  }

  .about-photo img{
    width:180px;
  }
}
/* HOMEPAGE HERO REFINEMENT */
.hero-buttons {
  margin-top: 1.2rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}

.hero-buttons a {
  background: #faf7f2;
  border: 1px solid #e5ded5;
  color: #7b5e3b;
  display: inline-block;
  padding: 0.45rem 0.9rem;
  border-radius: 999px;
  text-decoration: none;
  font-size: 0.9rem;
  transition: all 0.15s ease;
}

.hero-buttons a:hover {
  background: #f3ede6;
  border-color: #d6c8b8;
  color: #5c452c;
}

/* Tighten hero spacing */
#top + h1,
h1 {
  margin-top: 3rem;
  margin-bottom: 0.4rem;
  line-height: 1.2;
}

.hero-audience {
  display: block;
  width: 100%;
  max-width: 760px;
  margin: 0 auto 1rem auto;
  text-align: center;
}

/* MOBILE HERO REFINEMENT */
@media (max-width: 640px) {
  .hero-buttons {
    gap: 0.5rem;
  }

  .hero-buttons a {
    padding: 0.4rem 0.8rem;
    font-size: 0.85rem;
  }

  h1 {
    font-size: 1.65rem;
    margin-top: 0.3rem;
    margin-bottom: 0.3rem;
  }

  h1 + em,
  h1 + p {
    font-size: 0.95rem;
    margin-bottom: 0.7rem;
  }
}
/* FEATURED ESSAYS GRID */
.featured-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem 1.25rem;
  margin-top: 1rem;
}

.featured-grid a {
  display: block;
  padding: 0.6rem 0.8rem;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  background: #ffffff;
  text-decoration: none;
  color: #1f2937;
  font-size: 0.95rem;
  line-height: 1.35;
  transition: background 0.15s ease, border-color 0.15s ease;
}

.featured-grid a:hover {
  background: #f9fafb;
  border-color: #9ca3af;
}

/* MOBILE: switch to single column */
@media (max-width: 640px) {
  .featured-grid {
    grid-template-columns: 1fr;
    gap: 0.65rem;
  }

  .featured-grid a {
    padding: 0.55rem 0.75rem;
    font-size: 0.95rem;
  }
}
/* RESEARCH FRAMEWORK GRID */
.framework-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.6rem 1.2rem;
  margin: 1.2rem 0 1.8rem 0;
}

.framework-grid div {
  padding: 0.55rem 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  background: #ffffff;
  font-size: 0.95rem;
  color: #1f2937;
  line-height: 1.4;
}

/* MOBILE: single column */
@media (max-width: 640px) {
  .framework-grid {
    grid-template-columns: 1fr;
    gap: 0.55rem;
  }

  .framework-grid div {
    font-size: 0.95rem;
    padding: 0.5rem 0.7rem;
  }
}
.framework-grid a.framework-pill {
  display: block;
  padding: 0.55rem 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  background: #ffffff;
  text-decoration: none;
  color: #1f2937;
  font-size: 0.95rem;
  line-height: 1.35;
  transition: background 0.15s ease, border-color 0.15s ease;
}

.framework-grid a.framework-pill:hover {
  background: #f9fafb;
  border-color: #9ca3af;
}
/* === TYPOGRAPHIC PILL STYLE (A) === */

.pill-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 10px;
  margin: 1.2rem 0;
}

.pill {
  font-family: var(--body-font, system-ui, sans-serif);
  font-size: 0.9rem;
  font-weight: 500;
  letter-spacing: 0.1px;

  padding: 6px 14px;
  border-radius: 18px;

  background: #f7f7f7;
  border: 1px solid #e0e0e0;
  color: #111;

  text-decoration: none;
  white-space: nowrap;

  transition: background 0.15s ease, border-color 0.15s ease;
}

.pill,
.pill:link,
.pill:visited {
  color: #111 !important;
  text-decoration: none;
}
.pill:hover {
  background: #ececec;
  border-color: #c8c8c8;
}
/* === PILL ICONS (B) === */

.pill svg {
  width: 14px;
  height: 14px;
  margin-right: 6px;
  stroke-width: 1.8;
  stroke: currentColor;
  fill: none;
  flex-shrink: 0;
}

.pill {
  display: inline-flex;
  align-items: center;
}
/* === RESEARCH AREAS SPACING IMPROVEMENT === */

.research-areas h3 {
  margin-top: 1.8rem;
  margin-bottom: 0.4rem;
}

.research-areas p {
  margin-bottom: 1.2rem;
  line-height: 1.6;
  border-left: 2px solid #e5e7eb;
  padding-left: 0.75rem;
}
/* === RESEARCH AREAS — PHILOSOPHICAL GLOSS STYLE === */

.research-areas-gloss {
  margin-top: 1.2rem;
  display: flex;
  flex-direction: column;
  gap: 1.6rem;
}

.research-areas-gloss .area {
  padding-left: 0.9rem;
  border-left: 2px solid #e5e7eb;
}

.research-areas-gloss .area h3 {
  margin: 0 0 0.35rem 0;
  font-size: 1.05rem;
  color: #111;
}

.research-areas-gloss .area p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.55;
  color: #374151;
}

/* Mobile refinement */
@media (max-width: 640px) {
  .research-areas-gloss {
    gap: 1.4rem;
  }
}
.section-divider {
  width: 60%;
  margin: 3rem auto;
  border-top: 1px solid #e5e7eb;
  opacity: 0.7;
}
.pub-item {
  padding-top: 1rem;
  margin-top: 1.4rem;
  border-top: 1px solid #e5e7eb;
}
.pub-item a strong {
  font-size: 1.12rem;
  color: #111;
}

.pub-item small {
  display: block;
  margin-top: 0.25rem;
  color: #6b7280;
}
/* === RECENT PUBLICATIONS — GLOSS STYLE (EXCERPTS PRESERVED) === */

.pub-gloss {
  margin-top: 1.2rem;
  display: flex;
  flex-direction: column;
  gap: 1.8rem;
}

.pub-item {
  padding-left: 0.9rem;
  border-left: 2px solid #e5e7eb;
}

.pub-item summary {
  cursor: pointer;
  font-size: 1.05rem;
  color: #111;
}

.pub-item summary strong {
  font-size: 1.05rem;
}

.pub-item summary small {
  margin-left: 0.4rem;
  color: #6b7280;
  font-size: 0.85rem;
}

.pub-item p {
  margin-top: 0.6rem;
  font-size: 0.95rem;
  line-height: 1.55;
  color: #374151;
}
/* Reduce top spacing of the whole section */
#recent-publications {
  margin-top: 1.2rem;
}

/* Reduce spacing between publication items */
.pub-gloss {
  gap: 1.1rem;
}

/* Gloss block spacing refinements */
.pub-item p {
  margin-top: 0.4rem;
}

.pub-item summary small {
  margin-bottom: 0.2rem;
}

/* Prevent double spacing at the bottom */
.pub-item:last-child {
  margin-bottom: 0.4rem;
}
.pub-gloss {
  margin-top: 0.8rem;     /* tighter top spacing */
  display: flex;
  flex-direction: column;
  gap: 0.4rem;            /* THIS is the key: very small gap */
}

.pub-item {
  padding-left: 0.7rem;   /* slightly smaller gloss indent */
  border-left: 2px solid #e5e7eb;
  padding-top: 0.2rem;    /* minimal vertical padding */
  padding-bottom: 0.2rem;
}

.pub-item summary {
  font-size: 1rem;
  cursor: pointer;
}

.pub-item p {
  margin-top: 0.3rem;     /* tighter paragraph spacing */
  margin-bottom: 0.2rem;
  line-height: 1.45;      /* slightly tighter line height */
}
.site-title {
  font-size: 2rem;
  font-weight: 600;
  text-align: center;
  margin-bottom: 0.2rem;
  letter-spacing: 0.2px;
}
.site-author {
  text-align: center;
  font-size: 1.15rem;
  color: #6b7280;
  margin-top: 0;
  margin-bottom: 0.8rem;
}

.hero-description {
  text-align: center;
  max-width: 760px;
  margin: 0 auto 0.75rem auto;
  line-height: 1.6;
  color: #4b5563;
}

.hero-audience {
  text-align: center;
  margin-bottom: 1.2rem;
  color: #374151;
}

.site-subtitle {
  font-size: 1.2rem;
  font-weight: 300;
  text-align: center;
  margin-top: 0;
  margin-bottom: 1rem;
  color: #4b5563;
}
.homepage-epigraph {
  margin: 1.6rem 0 1.8rem 0;
  max-width: 520px;
  text-align: left;
  padding: 0;
}

.epigraph-text {
  font-size: 0.97rem;
  font-style: italic;
  line-height: 1.65;
  color: #374151;
  margin: 0;
}

.epigraph-author {
  font-size: 0.82rem;
  margin-top: 0.5rem;
  color: #6b7280;
}

@media (max-width: 640px) {
  .homepage-epigraph {
    margin: 1rem auto 1.2rem auto;
    padding: 0 0.5rem;
  }
  .epigraph-text {
    font-size: 0.92rem;
  }
}
/* FEATURED ESSAY HOVER EXCERPTS */
.featured-grid a {
  position: relative;
}

.featured-grid a[data-excerpt]::after {
  content: attr(data-excerpt);
  position: absolute;
  left: 0;
  right: 0;
  bottom: calc(100% + 8px);
  z-index: 20;

  background: #1f2937;
  color: #f9fafb;
  font-size: 0.85rem;
  line-height: 1.45;
  padding: 0.6rem 0.75rem;
  border-radius: 8px;

  opacity: 0;
  visibility: hidden;
  transform: translateY(4px);
  transition: opacity 0.18s ease, transform 0.18s ease;

  pointer-events: none;
  box-shadow: 0 6px 18px rgba(0,0,0,0.18);
}

.featured-grid a[data-excerpt]:hover::after {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

/* On touch devices, disable the hover tooltip (no real hover) */
@media (hover: none) {
  .featured-grid a[data-excerpt]::after {
    display: none;
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
body:has(.medieval-theme-marker) .cover-card img {
  border: 1px solid rgba(120,72,32,.5);
  box-shadow: 0 7px 20px rgba(0,0,0,.42), 0 0 0 1px rgba(185,133,54,.08);
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

<div class="section-divider"></div>

## Featured Essays · Ensayos destacados

<p class="featured-note">
  Spanish editions / Ediciones en español: <a href="/biblioteca/">Biblioteca</a>.
</p>

<div class="featured-grid">

  <a href="/ontology/philosophy-of-time/catholic-theology/2026/03/30/the-topology-of-presence.html"
     data-excerpt="The essay in which the Gaitan Topology was first introduced through a four-plane lemniscatic framework. Later work refines its account of the invariant Now, Ground, and constitutive relations.">
    Four Planes of Existence on the Lemniscate
  </a>

  <a href="/metaphysics/philosophical-theology/philosophy-of-god/2026/09/18/what-sustains-the-now-en.html"
     data-excerpt="A mature statement of the topology's grounding question: the invariant Now does not explain itself but depends upon the Non-Derivative Ground beneath the figure.">
    What Sustains the Now?
  </a>

  <a href="/philosophy/metaphysics/philosophy-of-science/2026/09/18/does-the-law-explain-itself-en.html"
     data-excerpt="An argument that physical law can describe the order of the figure without supplying the Ground upon which the actuality of that order depends.">
    Does the Law Explain Itself?
  </a>

  <a href="/philosophy-of-time/philosophy-of-physics/special-relativity/2026/09/20/does-relativity-divide-the-now-en.html"
     data-excerpt="A confrontation with relativity asking whether time dilation and relative simultaneity divide the invariant Now, and distinguishing physical crossings from the Now that is not a temporal slice.">
    Does Relativity Divide the Now?
  </a>

  <a href="/philosophy/metaphysics/philosophical-theology/2026/10/01/is-god-the-universe-or-everything-en.html"
     data-excerpt="A metaphysical distinction between God and the totality of created reality, arguing that no universe, sum, or everything within the figure can occupy the place of the Ground.">
    Is God the Universe, or Is God Everything?
  </a>

  <a href="/philosophy/metaphysics/philosophical-theology/2026/10/04/believe-in-god-and-have-faith-en.html"
     data-excerpt="An examination of the difference between reaching that God is by reason and receiving who God is through faith, assent, trust, and revelation.">
    Believe in God and Have Faith?
  </a>

  <a href="/philosophy-of-religion/moral-psychology/philosophy-of-perception/2026/09/27/the-angle-of-reception-en.html"
     data-excerpt="A study of reception as structurally conditioned by the interior orientation of the receiver: the world encountered is received through a history already curved.">
    The Angle of Reception
  </a>

  <a href="/philosophy-of-time/metaphysics-of-time/philosophical-theology/2026/10/11/the-path-through-which-i-walk-en.html"
     data-excerpt="A meditation on inheritance through Machado: the past is not merely behind us but the path through which we walk, while grace gives another step rather than another past.">
    The Path Through Which I Walk
  </a>

  <a href="/philosophy-of-time/philosophical-anthropology/philosophy-of-religion/2026/10/10/to-become-otherwise-en.html"
     data-excerpt="An account of interior change in which genuine novelty can be received without replacing the subject: one can become otherwise without becoming another.">
    To Become Otherwise
  </a>

  <a href="/philosophical-theology/philosophy-of-mind/thomas-aquinas/2026/10/17/who-was-before-me-or-myself-en.html"
     data-excerpt="A first-person inquiry into origin and inheritance: extending a subject's history backward cannot explain why there is a subject to inherit that history at all.">
    Who Was Before Me, or Myself?
  </a>

  <a href="/rene-descartes/metaphysical-grounding/divine-attributes/2026/10/15/the-conserved-cogito-en.html"
     data-excerpt="A return to Descartes through the mature topology, distinguishing self-presence from self-grounding and asking what sustains the subject whose cogito remains actual.">
    The Conserved Cogito
  </a>

  <a href="/metaphysics/ontology/philosophy-of-time/2026/10/18/quid-est-mutatio-en.html"
     data-excerpt="A metaphysics of change centered on continuity and numerical identity: change is the becoming-otherwise of one subject rather than replacement by another.">
    Quid est mutatio?
  </a>

</div>




<div class="section-divider"></div>



## Research Framework

The essays collected here develop an original philosophical framework at the intersection of ontology, philosophy of time, metaphysics, phenomenology, and Catholic theology.

### Original Concepts & Structural Propositions

<div class="pill-grid" markdown="0">

  <a class="pill" href="/lexicon/#non-derivative"
     title="That whose being depends on nothing else and upon which derivative actuality depends.">
    Non-Derivative
  </a>

  <a class="pill" href="/lexicon/#now"
     title="The invariant zero-thickness condition of actualization; succession does not occur within it.">
    Now (ontological)
  </a>

  <a class="pill" href="/lexicon/#condensation"
     title="The constitutive structure by which inheritance and reception are gathered into one present actuality at the invariant Now.">
    Condensation
  </a>

  <a class="pill" href="/lexicon/#inheritance"
     title="What already constituted actuality contributes to the present as carried history, trace, and acquired determination.">
    Inheritance
  </a>

  <a class="pill" href="/lexicon/#reception"
     title="What is newly given in the constitution of a present and cannot be derived from inheritance alone.">
    Reception
  </a>

  <a class="pill" href="/lexicon/#confluence"
     title="The relational unity by which distinct trajectories jointly constitute one actuality without losing their differences.">
    Confluence
  </a>

  <a class="pill" href="/lexicon/#present"
     title="The temporal actuality constituted at the Now through the condensation of inheritance and reception.">
    Present
  </a>

  <a class="pill" href="/lexicon/#trace"
     title="The structural mark left by a constituted actuality and carried into subsequent presents through inheritance.">
    Trace
  </a>

  <a class="pill" href="/lexicon/#structural-inertia"
     title="The structural persistence generated as traces are carried across constituted presents.">
    Structural Inertia
  </a>

  <a class="pill" href="/lexicon/#temporal-density"
     title="The referential scope of a crossing: how much of a trajectory is structurally implicated without adding thickness to the Now.">
    Temporal Density
  </a>

  <a class="pill" href="/lexicon/#infinite-interior"
     title="The unbroken structural continuity through which one subject can become otherwise without ceasing to be numerically the same subject.">
    Infinite Interior
  </a>

  <a class="pill" href="/lexicon/#topological-relativity"
     title="The variation of meaning and effect according to structural position and orientation, not subjective relativism.">
    Topological Relativity
  </a>

</div>


[Read the full Research Framework →](/research-framework/) · [Open the full Lexicon →](/lexicon/)

<div class="section-divider"></div>

## Research Areas

<div class="research-areas-gloss">

  <div class="area">
    <h3>Ontology</h3>
    <p>Questions of being, identity, continuity, and persistence.</p>
  </div>

  <div class="area">
    <h3>Philosophy of Time</h3>
    <p>Presence, temporality, memory, and the structure of the Now.</p>
  </div>

  <div class="area">
    <h3>Catholic Theology</h3>
    <p>Grace, suffering, divine action, eternity, and the metaphysics of faith.</p>
  </div>

  <div class="area">
    <h3>Phenomenology</h3>
    <p>Experience, selfhood, and first-person existence.</p>
  </div>

  <div class="area">
    <h3>Metaphysical Anthropology</h3>
    <p>Human identity, moral agency, responsibility, and personhood.</p>
  </div>

  <div class="area">
    <h3>Philosophy of Mathematics</h3>
    <p>Symbolic structures, abstraction, number, and ontological interpretation.</p>
  </div>

</div>

<div class="section-divider"></div>

## Recent Publications

<div class="pub-gloss">
  {% for post in site.posts limit:4 %}
    <div class="pub-item">

      <a class="pub-title" href="{{ post.url }}">
        <strong>{{ post.title }}</strong>
      </a>
      <small>{{ post.date | date: "%B %d, %Y" }}</small>

      <details>
        <summary>
          {% if post.lang == "es" %}
            Extracto
          {% else %}
            Excerpt
          {% endif %}
        </summary>
        <p>{{ post.excerpt }}</p>
      </details>

    </div>
  {% endfor %}
</div>

<div class="section-divider"></div>



<hr style="margin: 3rem 0 0.75rem; border: 0; border-top: 1px solid #d1d5db;">

<hr style="margin: 3rem 0 0.75rem; border: 0; border-top: 1px solid #d1d5db;">

<div class="about-card">

  <div class="about-photo">
    <img src="/assets/images/oscar-gaitan.jpg" alt="Oscar Gaitan">
  </div>

  <div class="about-content">
    <h2>About</h2>

   <p>
  Oscar Gaitan is a Nicaraguan American independent philosophical researcher based in Los Angeles, developing an original philosophical framework on temporality, ontology, and metaphysical anthropology through publicly accessible open scholarship.
</p>

<p>
  He is the author of <em>The Lemniscate of Time: A Geometric Meditation on Eternity and Temporal Succession</em> (2026), a monograph proposing the lemniscate (∞) as a contemplative framework for understanding the relationship between time and eternity.
</p>

<p>
  His essays explore philosophical theology, phenomenology, consciousness, and the structure of human existence.
</p>


    <h3>Contact</h3>

    <p>
      For scholarly correspondence, collaboration, or citation inquiries:
    </p>

    <p>
      <a href="mailto:ogaitan.research@gmail.com">ogaitan.research@gmail.com</a>
    </p>
  </div>


