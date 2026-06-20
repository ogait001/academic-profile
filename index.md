---
layout: default
title: Oscar Gaitan — Philosophy & Catholic Thought
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
</style>

# Oscar Gaitan — Philosophy & Catholic Thought

*Independent philosophical research in ontology, temporality, phenomenology, metaphysical anthropology and Catholic theology.*

Essays written for both scholarly readers and the philosophically curious.

<div class="hero-buttons">
  <a href="/essays/">Read Essays</a>
  <a href="https://philpeople.org/profiles/oscar-gaitan">PhilPeople</a>
  <a href="https://scholar.google.com/citations?user=huV-MLsAAAAJ">Google Scholar</a>
</div>

<div style="margin: 3rem 0;"></div>

---

## Language Accessibility

Nearly all essays are available in both  **English and Spanish**.

<div style="margin: 3rem 0;"></div>

---

## Featured Essays - Ensayos Destacados
<table>
<tr>
<td><a href="/philosophy-of-time/ontology/catholic-theology/2026/05/12/on-happiness.html">On Happiness: Its Duration, its Name, and what Endures</a></td>
<td><a href="/catholic-theology/philosophy-of-time/ontology/2026/05/21/eves-algorithm.html">Eve's Algorithm: The Industrialization of the Original Temptation</a></td>
</tr>
<tr>
<td><a href="/ontology/philosophy-of-time/catholic-theology/2026/04/20/the-am-that-remains.html">The Am that Remains:
A Critique of Descartes and a Metaphysics of the Soul</a></td>
<td><a href="/philosophy-of-time/ontology/2026/05/16/non-te-egeo.html">Non te egeo: When We Stopped Asking</a></td>
</tr>
<tr>
<td><a href="/philosophy-of-time/catholic-theology/ontology/2026/05/09/de-roling-god.html">De-Roling God:
On Community, Multitude, and the Displacement of the Self from the Now</a></td>
<td><a href="/philosophy-of-time/ontology/2026/04/10/does-time-need-me-or-do-i-need-time.html">Does Time Need Me, or Do I Need Time?</a></td>
</tr>
<tr>
<td><a href="/catholic-theology/ontology/philosophy-of-time/2026/05/18/the-mercy-of-time.html">The Mercy of Time:
Condemnatio in continenti and the Preservation of Moral Plasticity</a></td>
<td><a href="/philosophy-of-time/catholic-theology/ontology/2026/04/20/you-cannot-add-one-hour.html">You Cannot Add One Hour</a></td>
</tr>
<tr>
<td><a href="/philosophy-of-time/catholic-theology/ontology/2026/06/12/consummatum-est.html">Consummatum Est:
Temporal Density, Topological Relativity, and the Consummation of the Now</a></td>
<td><a href="/philosophy-of-time/catholic-theology/ontology/2026/06/09/the-grammar-of-displacement.html">The Grammar of Displacement:
From, Anytime, Then</a></td>
</tr>  
<tr>
<td><a href="/catholic-theology/philosophy-of-time/ontology/2026/05/28/the-corridor.html">The Corridor:
On the Ground that does not withdraw</a></td>
<td><a href="/philosophy-of-time/ontology/catholic-theology/2026/04/29/the-artificial-selection.html">The Artificial Selection:
On Endurance, Identity, and the Engineering of an Uninhabited Now</a></td>
</tr>
</table>

---

## Research Framework

The essays collected here develop an original philosophical framework at the intersection of ontology, philosophy of time, metaphysics, phenomenology, and Catholic theology.

### Original Concepts & Structural Propositions

- The Gaitan Topology
- The Ontological Now
- Structural Inertia
- Harmonic Echo
- The Ghost Zone
- The Alternate Lemniscate
- Topological Relativity
- Temporal Density
- Flat Sight
- Artificial Selection

[Explore the full Research Framework →](/research-framework/)

---

## Research Areas

### Ontology
Questions of being, identity, continuity, and persistence.

### Philosophy of Time
Presence, temporality, memory, and the structure of the Now.

### Catholic Theology
Grace, suffering, divine action, eternity, and the metaphysics of faith.

### Phenomenology
Experience, selfhood, and first-person existence.

### Metaphysical Anthropology
Human identity, moral agency, responsibility, and personhood.

### Philosophy of Mathematics
Symbolic structures, abstraction, number, and ontological interpretation.

<div style="margin: 3rem 0;"></div>

---

## Recent Publications

<div class="recent-pubs">
{% for post in site.posts limit: 6 %}
  <details class="pub-item">
    <summary>
      <a href="{{ post.url | relative_url }}">
        <strong>{{ post.title }}</strong>
      </a><br>
      <small>{{ post.date | date: "%B %d, %Y" }}</small>
    </summary>

    <div class="pub-abstract">
      {% if post.excerpt %}
        {{ post.excerpt }}
      {% else %}
        {{ post.content | strip_html | truncatewords: 35 }}
      {% endif %}
    </div>
  </details>
{% endfor %}

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
