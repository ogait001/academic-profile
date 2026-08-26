---
layout: default
title: Philosophy & Catholic Thought
author: Oscar Gaitan
description: Oscar Gaitan is a Nicaraguan American philosopher and independent researcher in ontology, temporality, phenomenology, metaphysical anthropology, and Catholic theology.
---

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
</style>

<div class="section-divider"></div>

## Featured Essays - Destacados

<div class="featured-grid">

  <a href="/philosophy-of-time/catholic-theology/ontology/2026/03/20/the-lemniscate-of-time.html"
     data-excerpt="A philosophical and theological exploration of time through the lemniscate as a topology of memory, possibility, freedom, grace, and providential return.">A Topology of Memory, Possibility, and Grace</a>

  <a href="/ontology/philosophy-of-time/catholic-theology/2026/03/30/the-topology-of-presence.html"
     data-excerpt="A theological-anthropological essay proposing the Gaitan Topology: a four-quadrant ontological framework organized around the crossing point of the Now, presence, grace, and existential displacement.">Four Planes of Existence on the Lemniscate</a>

  <a href="/philosophy-of-time/ontology/2026/04/10/does-time-need-me-or-do-i-need-time.html"
     data-excerpt="A philosophical and theological meditation on time and presence, arguing that the invariant Now is sustained by the ground of being named as I AM WHO I AM.">Does Time need Me or Do I need Time?</a>

  <a href="/ontology/philosophy-of-time/catholic-theology/2026/04/20/the-am-that-remains.html"
     data-excerpt="A metaphysical critique of Descartes, arguing not 'I think, therefore I am,' but that thought itself presupposes the prior reality of being.">A Critique of Descartes</a>

  <a href="/metaphysics/philosophy%20of%20mind/phenomenology/philosophical%20theology/moral%20psychology/2026/07/25/under-the-fig-tree.html"
     data-excerpt="A theological and metaphysical study of thought, conscience, and God's presence at the human Crossing Point.">Under the Fig Tree</a>

  <a href="philosophy/theology/trinity/christology/2026/08/01/distancia-mas-inmensa-en.html"
     data-excerpt="Can the Ground of all being become one of the grounded? A theological exploration of the Trinity, the Incarnation, and continuous divine sustaining.">Distancia Más Inmensa</a>

  <a href="/catholic-theology/philosophy-of-time/ontology/2026/05/21/eves-algorithm.html"
     data-excerpt="Algorithms industrialize the ancient temptation of Genesis: redefining reality, perception, and access to divine presence.">Eve's Algorithm</a>

  <a href="/philosophy-of-time/ontology/2026/05/16/non-te-egeo.html"
     data-excerpt="A reflection on digital culture's preemptive supply of answers, arguing that the deeper modern spiritual crisis is not rebellion against transcendence, but the erosion of the capacity to ask.">Non te egeo: When We Stopped Asking</a>

  <a href="/philosophy-of-time/catholic-theology/ontology/2026/04/20/you-cannot-add-one-hour.html"
     data-excerpt="A philosophical meditation on temporality, finitude, and the will, arguing that human life consists of finite crossings whose moments differ in ontological density.">You Cannot Add One Hour</a>

  <a href="/philosophy-of-time/catholic-theology/ontology/2026/05/10/alpha-and-omega.html"
     data-excerpt="A philosophical and theological meditation on the Now, the cosmos, and Alpha and Omega as the sustaining foundation of temporality and existence.">Alpha and Omega</a>

 <a href="/catholic-theology/ontology/philosophy-of-time/2026/06/15/the-topology-of-absolution.html"
     data-excerpt="Absolution restores communion with God while the work of temporal restoration continues. A topological meditation on confession, grace, and reconciliation.">The Topology of Absolution</a>

 <a href="/ontology/philosophy-of-time/2026/05/05/the-infinite-interior.html"
     data-excerpt="A philosophical meditation on identity, continuity, and change, proposing the infinite interior as the uninterrupted structure that preserves the self across transformation.">The Infinite Interior</a>
     
</div>




<div class="section-divider"></div>



## Research Framework

The essays collected here develop an original philosophical framework at the intersection of ontology, philosophy of time, metaphysics, phenomenology, and Catholic theology.

### Original Concepts & Structural Propositions

<div class="pill-grid" markdown="0">
  <a class="pill" href="/lexicon/#now"
     title="The invariant point of actualization where every being becomes actual.">
    The Ontological Now
  </a>
  <a class="pill" href="/lexicon/#non-derivative"
     title="That whose being depends on nothing else. It does not receive actualization — it gives it.">
    Non‑derivative
  </a>
  <a class="pill" href="/lexicon/#temporal-density"
     title="A moment's density depends on the breadth of the trajectory it renders visible.">
    Temporal Density
  </a>
  <a class="pill" href="/lexicon/#structural-inertia"
     title="The ontological resistance to change arising from repeated acts in the Now.">
    Structural Inertia
  </a>
  <a class="pill" href="/lexicon/#topological-relativity"
     title="Meaning varies with position, not with subjective interpretation.">
    Topological Relativity
  </a>
  <a class="pill" href="/lexicon/#infinite-interior"
     title="The continuous, asymptotic space that preserves identity across transformation.">
    Infinite Interior
  </a>
  <a class="pill" href="/lexicon/#condensation"
     title="Each Now gathers the preceding present rather than replacing it.">
    Condensation
  </a>
  <a class="pill" href="/lexicon/#inheritance"
     title="Everything the previous moment contributes to the new condensation.">
    Inheritance
  </a>
  <a class="pill" href="/lexicon/#reception"
     title="Everything newly given in the Now; the point of entry for grace.">
    Reception
  </a>
  <a class="pill" href="/lexicon/#trace"
     title="The structural deposit a condensation leaves in the Now.">
    Trace
  </a>
  <a class="pill" href="/lexicon/#confluence"
     title="The gathering of distinct trajectories into a single actuality at the Now, without erasing their differences.">
    Confluence
  </a>
</div>


[Open the full Lexicon →](/lexicon/)

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


