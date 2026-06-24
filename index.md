---
layout: default
title: Oscar Gaitan — Philosophy & Catholic Thought
description: Essays and research developing the Gaitan Topology, the Ontological Now, the Ghost Zone, and related philosophical concepts.
---

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
  margin-top: 0.5rem;
  margin-bottom: 0.4rem;
  line-height: 1.2;
}

h1 + em,
h1 + p {
  margin-top: 0.2rem;
  margin-bottom: 0.8rem;
  font-size: 1.05rem;
  line-height: 1.55;
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
/* === RECENT PUBLICATIONS — PHILOSOPHICAL GLOSS STYLE === */

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

.pub-item h3 {
  margin: 0;
  font-size: 1.05rem;
  color: #111;
}

.pub-item h3 a {
  text-decoration: none;
  color: inherit;
}

.pub-item small {
  display: block;
  margin-top: 0.25rem;
  margin-bottom: 0.4rem;
  color: #6b7280;
  font-size: 0.85rem;
}

.pub-item p {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.55;
  color: #374151;
}
</style>

# Oscar Gaitan — Philosophy & Catholic Thought

*Independent philosophical research in ontology, temporality, phenomenology, metaphysical anthropology and Catholic theology.*

Essays written for both scholarly readers and the philosophically curious.

<div class="hero-buttons">
  <a href="/library/">Library</a>
  <a href="/biblioteca/">Biblioteca</a>
  <a href="https://philpeople.org/profiles/oscar-gaitan">PhilPeople</a>
  <a href="https://scholar.google.com/citations?user=huV-MLsAAAAJ">Google Scholar</a>
</div>

<div class="section-divider"></div>



## Featured Essays - Destacados
<div class="featured-grid">

  <a href="/philosophy-of-time/ontology/catholic-theology/2026/05/12/on-happiness.html">On Happiness</a>

  <a href="/catholic-theology/philosophy-of-time/ontology/2026/05/21/eves-algorithm.html">Eve's Algorithm</a>

  <a href="/ontology/philosophy-of-time/catholic-theology/2026/04/20/the-am-that-remains.html">The Am that Remains</a>

  <a href="/philosophy-of-time/ontology/2026/05/16/non-te-egeo.html">Non te egeo: When We Stopped Asking</a>

  <a href="/philosophy-of-time/catholic-theology/ontology/2026/05/09/de-roling-god.html">De-Roling God</a>

  <a href="/philosophy-of-time/ontology/catholic-theology/2026/04/10/does-time-need-me-or-do-i-need-time.html">Does Time Need Me, or Do I Need Time?</a>

  <a href="/catholic-theology/ontology/2026/06/17/the-servant-of-servants.html">The Servant of Servants</a>

  <a href="/philosophy-of-time/ontology/catholic-theology/2026/04/29/the-artificial-selection.html">The Artificial Selection</a>

  <a href="/philosophy-of-time/catholic-theology/ontology/2026/06/12/consummatum-est.html">Consummatum Est</a>

  <a href="/philosophy-of-time/catholic-theology/ontology/2026/06/09/the-grammar-of-displacement.html">The Grammar of Displacement</a>

</div>



<div class="section-divider"></div>



## Research Framework

The essays collected here develop an original philosophical framework at the intersection of ontology, philosophy of time, metaphysics, phenomenology, and Catholic theology.

### Original Concepts & Structural Propositions
<div class="pill-grid">

  <a class="pill" href="/research-framework/#now"
     title="The invariant point of actualization where every being becomes actual.">
    The Ontological Now
  </a>

  <a class="pill" href="/research-framework/#non-derivative"
     title="That whose being depends on nothing else. It does not receive actualization — it gives it.">
    Non‑derivative
  </a>

  <a class="pill" href="/research-framework/#temporal-density"
     title="A moment's density depends on the breadth of the trajectory it renders visible.">
    Temporal Density
  </a>

  <a class="pill" href="/research-framework/#structural-inertia"
     title="The ontological resistance to change arising from repeated acts in the Now.">
    Structural Inertia
  </a>

  <a class="pill" href="/research-framework/#flat-sight"
     title="Perceiving content without perceiving position.">
    Flat Sight
  </a>

  <a class="pill" href="/research-framework/#topological-relativity"
     title="Meaning varies with position, not with subjective interpretation.">
    Topological Relativity
  </a>

  <a class="pill" href="/research-framework/#residency"
     title="The unfinished exerts a structural pull on the will.">
    Residency
  </a>

</div>


[Explore the full Research Framework →](/research-framework/)

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

  {% for post in site.posts limit:6 %}
  <div class="pub-item">
    <h3>
      <a href="{{ post.url }}"><strong>{{ post.title }}</strong></a>
    </h3>
    <small>{{ post.date | date: "%B %d, %Y" }}</small>
    <p>{{ post.content | strip_html | truncatewords: 22 }}</p>
  </div>
  {% endfor %}

</div>

<div class="section-divider"></div>


</div>

<hr style="margin: 3rem 0 0.75rem; border: 0; border-top: 1px solid #d1d5db;">

<hr style="margin: 3rem 0 0.75rem; border: 0; border-top: 1px solid #d1d5db;">

<div class="about-card">

  <div class="about-photo">
    <img src="/assets/images/oscar-gaitan.jpg" alt="Oscar Gaitan">
  </div>

  <div class="about-content">
    <h2>About</h2>

   <p>
  Oscar Gaitan is a Nicaraguan-born independent philosophical researcher based in Los Angeles, developing an original philosophical framework on temporality, ontology, and metaphysical anthropology through publicly accessible open scholarship.
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

</div>
