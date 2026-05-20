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
</style>

# Oscar Gaitan — Philosophy & Catholic Thought

*Independent philosophical researcher exploring ontology, philosophy of time, metaphysics, phenomenology, and Catholic theology.*

Essays written for both scholarly readers and the philosophically curious.

<div class="hero-buttons">
  <a href="/essays/">Read Essays</a>
  <a href="https://philpeople.org/profiles/oscar-gaitan">PhilPeople</a>
  <a href="https://scholar.google.com/citations?user=huV-MLsAAAAJ">Google Scholar</a>
</div>

---

## Featured Essays

<table>
<tr>
<td><a href="/philosophy-of-time/ontology/catholic-theology/2026/05/12/on-happiness.html">On Happiness</a></td>
<td><a href="/catholic-theology/philosophy-of-time/ontology/2026/05/05/where-is-god.html">Where Is God?</a></td>
</tr>

<tr>
<td><a href="/ontology/philosophy-of-time/catholic-theology/2026/04/20/the-am-that-remains.html">The Am That Remains</a></td>
<td><a href="/philosophy-of-time/ontology/2026/05/16/non-te-egeo.html">Non te egeo: When We Stopped Asking</a></td>
</tr>

<tr>
<td><a href="/philosophy-of-time/catholic-theology/ontology/2026/05/09/de-roling-god.html">De-Roling God</a></td>
<td><a href="/philosophy-of-time/ontology/2026/04/22/does-time-need-me-or-do-i-need-time.html">Does Time Need Me, or Do I Need Time?</a></td>
</tr>

<tr>
<td><a href="/catholic-theology/ontology/philosophy-of-time/2026/05/18/the-mercy-of-time.html">The Mercy of Time</a></td>
<td><a href="/philosophy-of-time/catholic-theology/ontology/2026/04/20/you-cannot-add-one-hour.html">You Cannot Add One Hour</a></td>
</tr>

<tr>
<td><a href="/ontology/philosophy-of-time/2026/04/28/a-letter-to-an-atheist.html">A Letter to an Atheist</a></td>
<td><a href="/philosophy-of-time/ontology/catholic-theology/2026/04/29/the-artificial-selection.html">The Artificial Selection</a></td>
</tr>
</table>

---

## Research Framework

My work develops an original philosophical framework at the intersection of ontology, philosophy of time, metaphysics, phenomenology, and Catholic theology.

### Original Concepts & Structural Propositions

- The Gaitan Topology
- The Ontological Now
- Structural Inertia
- Harmonic Echo
- The Ghost Zone
- Alternate Lemniscates
- Topological Relativity
- Temporal Density
- The Uninhabited Now
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

---

## Language Accessibility

Many essays are available in both **English and Spanish**.

---

## Recent Publications

<div class="recent-pubs">
{% for post in site.posts limit: 10 %}
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

<h2 style="margin-top: 0.5rem;">About</h2>

Oscar Gaitan is a Nicaraguan-American independent philosophical researcher whose work explores ontology, temporality, metaphysical anthropology, phenomenology, and Catholic thought through publicly accessible scholarship.
---

## Contact

For scholarly correspondence, citation inquiries, or collaboration, please contact:

ogaitan.research@gmail.com
