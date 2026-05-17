---
layout: default
title: Oscar Gaitan — Philosophy & Catholic Thought
---

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
</table>

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

<ul>
{% for post in site.posts limit: 10 %}
  <li style="margin-bottom: 2rem;">
    <a href="{{ post.url | relative_url }}">
      <strong>{{ post.title }}</strong>
    </a><br>
    <small>{{ post.date | date: "%B %d, %Y" }}</small>

    {% if post.excerpt %}
      <p style="margin-top: 0.5rem; line-height: 1.5; color: #555;">
        {{ post.excerpt }}
      </p>
    {% else %}
      <p style="margin-top: 0.5rem; line-height: 1.5; color: #555;">
        {{ post.content | strip_html | truncatewords: 35 }}
      </p>
    {% endif %}
  </li>
{% endfor %}
</ul>

## About

Oscar Gaitan is a Nicaraguan-American independent philosophical researcher whose work explores ontology, temporality, metaphysical anthropology, phenomenology, and Catholic thought through publicly accessible scholarly essays.
