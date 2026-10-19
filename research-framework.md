---
layout: default
title: Research Framework
permalink: /research-framework/
description: "The Gaitan Topology — an interactive reference of key terms and structural propositions in Oscar Gaitan's philosophy of time, ontology, and Catholic thought."
---

<style id="research-framework-cover-theme">
/* Page-scoped cover design. All site-wide overrides apply only while .rf-wrap exists. */
html { scroll-behavior: smooth; }
body:has(.rf-wrap) {
  background:
    radial-gradient(ellipse 70% 50% at 30% 20%, rgba(80,35,10,.6) 0%, transparent 65%),
    radial-gradient(ellipse 60% 70% at 70% 75%, rgba(40,15,5,.7) 0%, transparent 60%),
    linear-gradient(170deg,#1e0c04 0%,#2a1108 20%,#1a0a03 40%,#241008 60%,#1c0b05 80%,#1e0c04 100%);
  color: #e8d4a8;
}
body:has(.rf-wrap) .site-header {
  background: linear-gradient(180deg,#1c0b05 0%,#2a1108 100%);
  border-bottom: 1px solid rgba(120,72,32,.78);
}
body:has(.rf-wrap) .site-header .wrapper {
  max-width: 1100px; margin: 0 auto; padding: 22px 48px !important;
}
body:has(.rf-wrap) .site-header nav { text-align: center; line-height: 1.9; }
body:has(.rf-wrap) .site-header nav a {
  display: inline-block; margin: 2px 10px; color: #c5a36d;
  font: 600 12px/1.8 system-ui,-apple-system,sans-serif;
  letter-spacing: .06em; text-transform: uppercase; text-decoration: none;
}
body:has(.rf-wrap) .site-header nav a:hover { color: #e8d4a8; text-decoration: underline; }
body:has(.rf-wrap) .page-content { max-width: none; width: 100%; margin: 0; padding: 0; background: transparent; }
body:has(.rf-wrap) .page-content > .wrapper { max-width: none; width: 100%; margin: 0; padding: 0; }
body:has(.rf-wrap) .back-to-top {
  background: #2a1108; color: #e8d4a8; border: 1px solid rgba(120,72,32,.9);
  box-shadow: 0 3px 15px rgba(0,0,0,.38);
}
body:has(.rf-wrap) .back-to-top:hover { background: #4a210c; }
body:has(.rf-wrap) .site-footer {
  margin-top: 0; padding: 28px 24px; background: #170903;
  border-top: 1px solid rgba(120,72,32,.75); color: #ad8955;
}
body:has(.rf-wrap) .site-footer p { color: #ad8955; }
body:has(.rf-wrap) .site-footer a { color: #d7ab58; }
body:has(.rf-wrap) .site-footer a:hover { color: #f1dca9; }
body:has(.rf-wrap) .footer-inner { max-width: 850px; margin: 0 auto; }

.rf-wrap, .rf-wrap * { box-sizing: border-box; }
.rf-wrap {
  --ink:#e8d4a8; --soft:#c7aa78; --faint:#a17b4b;
  --line:rgba(120,72,32,.72); --paper:#1e0c04; --panel:#241008;
  --gold:#c89b37; --gold-soft:rgba(120,68,25,.7);
  position:relative; isolation:isolate; overflow:hidden;
  width:100%; max-width:1100px; margin:0 auto;
  padding:76px 64px 72px; color:var(--ink);
  font-family:"EB Garamond", "Palatino Linotype", Palatino, Garamond, Georgia, serif;
  background-image:
    radial-gradient(ellipse 70% 50% at 30% 20%,rgba(80,35,10,.44) 0%,transparent 65%),
    radial-gradient(ellipse 60% 70% at 70% 75%,rgba(40,15,5,.52) 0%,transparent 60%),
    linear-gradient(170deg,#1e0c04 0%,#2a1108 20%,#1a0a03 40%,#241008 60%,#1c0b05 80%,#1e0c04 100%),
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.75' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='.12'/%3E%3C/svg%3E");
  background-blend-mode:screen,screen,normal,overlay;
}
.rf-wrap::before { content:""; position:absolute; inset:20px; border:2px solid rgba(120,72,32,.78); pointer-events:none; z-index:0; }
.rf-wrap::after { content:""; position:absolute; inset:36px; border:1px solid rgba(100,55,22,.56); pointer-events:none; z-index:0; }
.rf-ornaments { position:absolute; inset:0; pointer-events:none; z-index:1; color:rgba(140,80,30,.88); }
.rf-ornaments .corner { position:absolute; font-size:26px; line-height:1; }
.corner-tl { top:10px; left:10px; } .corner-tr { top:10px; right:10px; transform:scaleX(-1); }
.corner-bl { bottom:10px; left:10px; transform:scaleY(-1); } .corner-br { bottom:10px; right:10px; transform:scale(-1,-1); }
.rf-wrap > *:not(.rf-ornaments) { position:relative; z-index:2; }
.rf-header { position:relative; text-align:center; padding:0 10px 30px; border-bottom:1px solid rgba(120,72,32,.72); margin-bottom:34px; }
.rf-header::after { content:"✦"; position:absolute; bottom:-11px; left:50%; transform:translateX(-50%); padding:0 14px; background:#211006; color:#c89b37; font-size:15px; letter-spacing:.35em; }
.header-emblem { margin:0 auto 7px; width:132px; height:62px; filter:drop-shadow(0 0 14px rgba(150,80,10,.15)); }
.rf-wrap .eyebrow, .rf-wrap .section-kicker, .rf-wrap .field-label, .rf-wrap .history-label {
  color:#b47b30; font-family:system-ui,-apple-system,sans-serif; font-size:10px;
  letter-spacing:.2em; font-weight:650; text-transform:uppercase;
}
.rf-wrap .eyebrow { margin:0 0 14px; }
.rf-wrap h1, .rf-wrap h2, .rf-wrap h3, .rf-wrap .term-name, .rf-wrap .prop-name, .rf-wrap .dek, .rf-wrap .flow-title { font-family:"EB Garamond", "Palatino Linotype", Palatino, Garamond, Georgia, serif; font-weight:500; }
.rf-wrap h1 { color:#e8d4a8; font-size:clamp(36px,4.7vw,52px); line-height:1.12; letter-spacing:.012em; text-shadow:0 3px 12px rgba(0,0,0,.8),0 0 44px rgba(100,50,10,.22); margin:0 0 15px; }
.rf-wrap .dek { font-size:21px; font-style:italic; color:rgba(200,160,95,.9); line-height:1.48; max-width:700px; margin:0 auto 15px; }
.rf-wrap .intro { max-width:690px; margin:0 auto; color:#d1b88a; font-size:14px; line-height:1.85; }
.rf-wrap a { color:#e0b55d; }
.rf-wrap .intro a { text-decoration-color:rgba(200,155,55,.45); }
.rf-wrap .header-links { display:flex; justify-content:center; gap:10px; flex-wrap:wrap; margin-top:22px; }
.rf-wrap .action-link { display:inline-flex; align-items:center; gap:8px; font-family:system-ui,-apple-system,sans-serif; background:rgba(33,16,6,.88); border:1px solid rgba(120,68,25,.82); border-radius:2px; color:#d7af61; padding:9px 13px; letter-spacing:.02em; font-size:12px; text-decoration:none; }
.rf-wrap .action-link:hover { background:#32180a; border-color:#b67e31; color:#f1dca9; }
.rf-wrap .section { margin-top:42px; }
.rf-wrap .section-kicker { margin:0 0 7px; }
.rf-wrap .section h2 { color:#e8d4a8; font-size:31px; letter-spacing:.01em; line-height:1.18; margin:0 0 9px; }
.rf-wrap .section h2::after { content:""; display:block; width:64px; margin-top:10px; border-top:1.5px solid rgba(160,95,35,.85); }
.rf-wrap .section-intro { color:#c5a675; max-width:720px; font-size:13px; line-height:1.8; margin:0 0 19px; }
.rf-wrap .dependency { padding:22px; border:1px solid rgba(120,72,32,.75); border-radius:2px; background:rgba(22,9,3,.6); box-shadow:inset 0 0 0 3px rgba(100,55,22,.12); }
.rf-wrap .flow { display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:13px; align-items:stretch; }
.rf-wrap .flow-step { position:relative; min-width:0; min-height:138px; padding:15px 12px; border:1px solid rgba(120,72,32,.78); border-radius:2px; background:linear-gradient(165deg,rgba(48,22,8,.94),rgba(25,10,3,.97)); box-shadow:inset 0 0 0 2px rgba(160,100,35,.04); display:flex; flex-direction:column; align-items:flex-start; gap:8px; }
.rf-wrap .flow-step:not(:last-child)::after { content:"→"; position:absolute; right:-13px; top:43%; transform:translate(50%,-50%); color:#d49d44; font-size:18px; z-index:2; background:#1d0b04; width:18px; text-align:center; }
.rf-wrap .flow-step:nth-child(1), .rf-wrap .flow-step:nth-child(4) { border-top:2px solid #9c642c; }
.rf-wrap .flow-step:nth-child(2) { border-top:2px solid #bf8e39; } .rf-wrap .flow-step:nth-child(3) { border-top:2px solid #b47b30; } .rf-wrap .flow-step:nth-child(5) { border-top:2px solid #80502a; }
.rf-wrap .flow-n { font-family:system-ui,-apple-system,sans-serif; font-size:10px; color:#b98542; font-weight:750; letter-spacing:.12em; }
.rf-wrap .flow-title { color:#e8d4a8; font-size:18px; line-height:1.1; }
.rf-wrap .flow-sub, .rf-wrap .flow-note { color:#c3a678; }
.rf-wrap .flow-sub { font-family:system-ui,-apple-system,sans-serif; font-size:11px; line-height:1.4; }
.rf-wrap .flow-join { display:flex; flex-wrap:wrap; gap:4px; margin-top:auto; }
.rf-wrap .flow-join span { font:9px/1.3 system-ui,-apple-system,sans-serif; border-radius:2px; padding:4px 6px; background:#2b1508; color:#d7b66d; border:1px solid rgba(120,68,25,.82); }
.rf-wrap .confluence-callout { display:grid; grid-template-columns:max-content minmax(0,1fr) max-content; align-items:center; gap:16px; margin-top:17px; padding:15px 13px; border:1px solid rgba(184,125,49,.62); border-left:3px solid #b47b30; background:linear-gradient(100deg,rgba(68,31,9,.64),rgba(25,10,3,.54)); }
.rf-wrap .confluence-mark { font:650 9px/1.5 system-ui,-apple-system,sans-serif; letter-spacing:.14em; color:#b98542; text-transform:uppercase; max-width:94px; }
.rf-wrap .confluence-copy h3 { margin:0 0 4px; color:#ead8b1; font-size:21px; line-height:1.1; }
.rf-wrap .confluence-copy p { margin:0; color:#cbb084; font-size:12px; line-height:1.7; }
.rf-wrap .confluence-link { font:10px/1.4 system-ui,-apple-system,sans-serif; white-space:nowrap; text-decoration:none; color:#dfb354; border-bottom:1px solid rgba(200,155,55,.45); padding-bottom:3px; }
.rf-wrap .confluence-link:hover { color:#fff0c5; border-color:#c89b37; }
.rf-wrap .flow-note { border-top:1px solid rgba(120,72,32,.7); margin:18px 0 0; padding-top:13px; font:12px/1.75 system-ui,-apple-system,sans-serif; }
.rf-wrap .flow-note strong { color:#e3c88b; }
.rf-wrap .term-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:11px; }
.rf-wrap .term-card, .rf-wrap .prop-card { border:1px solid rgba(120,72,32,.8); border-radius:2px; background:linear-gradient(160deg,rgba(43,19,7,.96),rgba(26,10,3,.98)); box-shadow:inset 0 0 0 2px rgba(160,100,35,.035); overflow:hidden; scroll-margin-top:90px; transition:border-color .15s,box-shadow .15s; }
.rf-wrap .term-card:hover, .rf-wrap .prop-card:hover { border-color:#986126; box-shadow:0 4px 14px rgba(0,0,0,.22); }
.rf-wrap .term-card.open, .rf-wrap .prop-card.open { border-color:#b17b36; box-shadow:0 4px 18px rgba(0,0,0,.28); }
.rf-wrap .term-toggle, .rf-wrap .prop-toggle { appearance:none; width:100%; border:0; background:transparent; text-align:left; display:flex; align-items:flex-start; gap:11px; padding:15px; cursor:pointer; color:#e8d4a8; font:inherit; }
.rf-wrap .term-toggle:focus-visible, .rf-wrap .prop-toggle:focus-visible { outline:2px solid #d8a745; outline-offset:-4px; }
.rf-wrap .term-number, .rf-wrap .prop-number { font:750 10px/1.4 system-ui,-apple-system,sans-serif; color:#b47b30; letter-spacing:.04em; min-width:21px; padding-top:3px; }
.rf-wrap .term-heading { min-width:0; flex:1; display:flex; flex-direction:column; gap:5px; }
.rf-wrap .term-name, .rf-wrap .prop-name { color:#ead8b1; }
.rf-wrap .term-name { font-size:20px; line-height:1.1; letter-spacing:-.01em; }
.rf-wrap .term-summary { font:12px/1.6 system-ui,-apple-system,sans-serif; color:#c4a87b; }
.rf-wrap .term-kind { flex-shrink:0; font:9px/1.3 system-ui,-apple-system,sans-serif; text-transform:uppercase; letter-spacing:.06em; color:#d5ad61; background:#271205; border:1px solid rgba(120,68,25,.8); border-radius:2px; padding:4px 7px; margin-top:1px; }
.rf-wrap .chevron { color:#b58a4c; font-size:16px; line-height:1; transition:transform .18s; flex-shrink:0; margin:3px 0 0; }
.rf-wrap .open .chevron { transform:rotate(180deg); }
.rf-wrap .term-detail, .rf-wrap .prop-body { border-top:1px solid rgba(120,72,32,.65); background:rgba(18,7,2,.88); }
.rf-wrap [hidden] { display:none !important; }
.rf-wrap .detail-inner { padding:16px 18px 18px; }
.rf-wrap .detail-inner p { margin:0 0 11px; color:#dcc69d; font:13px/1.85 system-ui,-apple-system,sans-serif; }
.rf-wrap .detail-inner p.field-label { margin:1px 0 6px; color:#c18a3a; font-size:10px; }
.rf-wrap .field-label { color:#c18a3a; }
.rf-wrap .function-text { padding-left:10px; border-left:2px solid #976128; color:#c7ab7e !important; }
.rf-wrap .entry-link { display:inline-flex; gap:7px; text-decoration:none; font:700 11px/1.4 system-ui,-apple-system,sans-serif; margin-top:4px; color:#dfb354; }
.rf-wrap .entry-link:hover { text-decoration:underline; }
.rf-wrap .history-note { margin-top:21px; border-left:2px solid #9b5a20; background:rgba(90,43,9,.15); padding:11px 0 11px 16px; }
.rf-wrap .history-label { margin:0 0 6px; }
.rf-wrap .history-note p { font:12px/1.8 system-ui,-apple-system,sans-serif; color:#cbb084; margin:0; max-width:750px; }
.rf-wrap .history-note strong { color:#ecd6a4; }
.rf-wrap .props { display:flex; flex-direction:column; gap:8px; }
.rf-wrap .prop-toggle { align-items:center; padding:15px 17px; }
.rf-wrap .prop-number { font-size:11px; color:#d1a04b; min-width:25px; }
.rf-wrap .prop-name { font-size:19px; line-height:1.2; flex:1; }
.rf-wrap .prop-body .detail-inner { padding-left:59px; }
.rf-wrap .prop-body .detail-inner p { font-size:13px; }
.rf-wrap .rel-pills { display:flex; flex-wrap:wrap; gap:6px; }
.rf-wrap .rel-pill { background:#281306; border:1px solid rgba(120,68,25,.82); border-radius:2px; color:#d5ad61; text-decoration:none; padding:4px 9px; font:10px/1.4 system-ui,-apple-system,sans-serif; }
.rf-wrap .rel-pill:hover { background:#3a1b08; }
.rf-wrap .rf-foot { margin-top:42px; padding-top:19px; border-top:1px solid rgba(120,72,32,.72); display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; color:#a88351; font:10px/1.5 system-ui,-apple-system,sans-serif; letter-spacing:.04em; }
.rf-wrap .rf-foot a { color:#d7ab58; text-decoration:none; }
.rf-wrap .rf-foot a:hover { text-decoration:underline; }
@media (max-width: 900px) {
  .rf-wrap { padding:70px 45px 60px; }
  .rf-wrap .flow { grid-template-columns:1fr; gap:10px; }
  .rf-wrap .flow-step { min-height:0; padding:13px 14px; display:grid; grid-template-columns:32px minmax(0,1fr); column-gap:9px; row-gap:4px; }
  .rf-wrap .flow-n { grid-row:1 / span 2; }
  .rf-wrap .flow-title { grid-column:2; }
  .rf-wrap .flow-sub, .rf-wrap .flow-join { grid-column:2; }
  .rf-wrap .flow-join { margin-top:3px; }
  .rf-wrap .flow-step:not(:last-child)::after { content:"↓"; right:50%; top:auto; bottom:-17px; transform:translate(50%,50%); font-size:15px; }
}
@media (max-width: 700px) {
  body:has(.rf-wrap) .site-header .wrapper { padding:16px 18px !important; }
  body:has(.rf-wrap) .site-header nav a { font-size:10px; margin:2px 7px; }
  .rf-wrap { padding:64px 28px 54px; }
  .rf-wrap::before { inset:12px; border-width:1.5px; }
  .rf-wrap::after { inset:21px; }
  .rf-wrap .rf-header { padding:0 4px 26px; }
  .rf-wrap .header-emblem { transform:scale(.9); transform-origin:center bottom; margin-bottom:2px; }
  .rf-wrap h1 { font-size:34px; }
  .rf-wrap .dek { font-size:18px; }
  .rf-wrap .section { margin-top:34px; }
  .rf-wrap .section h2 { font-size:27px; }
  .rf-wrap .dependency { padding:14px; }
  .rf-wrap .term-grid { grid-template-columns:1fr; }
  .rf-wrap .corner { font-size:20px; }
  .rf-wrap .confluence-callout { grid-template-columns:1fr; gap:7px; padding:13px; }
  .rf-wrap .confluence-mark { max-width:none; }
  .rf-wrap .confluence-link { justify-self:start; margin-top:3px; }
  .rf-wrap .term-toggle { padding:13px 11px; gap:8px; }
  .rf-wrap .term-name { font-size:19px; }
  .rf-wrap .term-kind { font-size:8px; padding:3px 5px; }
  .rf-wrap .prop-toggle { padding:13px 12px; }
  .rf-wrap .prop-name { font-size:17px; }
  .rf-wrap .prop-body .detail-inner { padding-left:14px; }
  .rf-wrap .rf-foot { display:block; }
  .rf-wrap .rf-foot span { display:block; margin-bottom:8px; }
}
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior:auto; }
  .rf-wrap *, .rf-wrap *::before, .rf-wrap *::after { transition:none !important; }
}
</style>

<div class="rf-wrap">
<div aria-hidden="true" class="rf-ornaments">
<span class="corner corner-tl">❧</span><span class="corner corner-tr">❧</span>
<span class="corner corner-bl">❧</span><span class="corner corner-br">❧</span>
</div>
<header class="rf-header">
<div aria-hidden="true" class="header-emblem">
<svg height="62" viewbox="-70 -34 140 68" width="132" xmlns="http://www.w3.org/2000/svg">
<defs><radialgradient id="rfGlow"><stop offset="0" stop-color="#d4900a" stop-opacity=".95"></stop><stop offset=".45" stop-color="#a06010" stop-opacity=".5"></stop><stop offset="1" stop-color="#7a3510" stop-opacity="0"></stop></radialgradient></defs>
<path d="M 0,0 C 14,-26 43,-28 57,0 C 43,28 14,26 0,0 C -14,-26 -43,-28 -57,0 C -43,28 -14,26 0,0 Z" fill="none" stroke="rgba(200,155,55,.86)" stroke-dasharray="1.8 4" stroke-linecap="round" stroke-width="1.1"></path>
<circle cx="0" cy="0" fill="url(#rfGlow)" r="20"></circle><circle cx="0" cy="0" fill="rgba(220,160,40,.98)" r="3.4"></circle><circle cx="0" cy="0" fill="#fff5cc" r="1.5"></circle>
</svg>
</div>
<p class="eyebrow">Gaitan Topology · Research Framework</p>
<h1>Key terms &amp; structural propositions</h1>
<p class="dek">A concise orientation to the mature Gaitan Topology.</p>
<p class="intro">The terms below trace the core dependency from ground to actualization and temporal constitution. The <a href="/lexicon/">full Lexicon</a> presents the complete conceptual network.</p>
<div class="header-links"><a class="action-link" href="/lexicon/">Explore the full Lexicon <span aria-hidden="true">↗</span></a><a class="action-link" href="/lexico/">Leer en español <span aria-hidden="true">↗</span></a></div>
</header>
<section aria-labelledby="dependency-title" class="section">
<p class="section-kicker">01 · At a glance</p><h2 id="dependency-title">The core dependency</h2>
<p class="section-intro">A compact map of the framework's central relations before the individual terms are opened below.</p>
<section aria-labelledby="dependency-title" class="section">
  <p class="section-kicker">01 · At a glance</p>
  <h2 id="dependency-title">The core dependency</h2>

  <p class="section-intro">
    A compact map of the framework's central relations before the individual terms are opened below.
  </p>

  <p class="dependency-label">
    Explanatory dependence <span aria-hidden="true">·</span> Not temporal sequence
  </p>

  <div class="dependency">
    <div aria-label="Explanatory dependency map" class="flow">
<div class="flow-step"><span class="flow-n">01</span><span class="flow-title">Non-Derivative</span><span class="flow-sub">Ground</span></div>
<div class="flow-step"><span class="flow-n">02</span><span class="flow-title">Invariant Now</span><span class="flow-sub">Condition of actualization</span></div>
<div class="flow-step"><span class="flow-n">03</span><span class="flow-title">Condensation</span><span class="flow-sub">Constitution at the Now</span><span class="flow-join"><span>Inheritance</span><span>Reception</span></span></div>
<div class="flow-step"><span class="flow-n">04</span><span class="flow-title">Present</span><span class="flow-sub">Constituted actuality</span></div>
<div class="flow-step"><span class="flow-n">05</span><span class="flow-title">Temporal order</span><span class="flow-sub">Irreversible relations among actualities</span></div>
</div>
<div aria-label="Confluence as a relational principle" class="confluence-callout">
<div class="confluence-mark">RELATIONAL PRINCIPLE</div>
<div class="confluence-copy"><h3>Confluence</h3><p>Distinct trajectories gather into one actuality at the Now without erasing their differences. Confluence names their relational unity; it is not another stage in the sequence.</p></div>
<a class="confluence-link" href="/lexicon/#confluence">Open Lexicon entry ↗</a>
</div>
<p class="flow-note"><strong>How to read this map:</strong> the arrows express explanatory dependence, not a succession of events inside the Now. Inheritance and reception are co-constitutive dimensions of condensation. Confluence names the unity of distinct trajectories within the actuality they jointly constitute; it is not a temporal stage.</p>
</div>
</section>
<section aria-labelledby="terms-title" class="section">
<p class="section-kicker">02 · Conceptual vocabulary</p><h2 id="terms-title">Nine orientation terms</h2>
<p class="section-intro">Open a term for its definition and function. Each entry also links to its place in the full Lexicon.</p>
<div class="term-grid">
<article class="term-card" id="non-derivative">
<button aria-controls="detail-non-derivative" aria-expanded="false" class="term-toggle" type="button">
<span class="term-number">01</span>
<span class="term-heading"><span class="term-name">Non-derivative</span><span class="term-summary">That whose being depends on nothing else and upon which derivative actuality depends.</span></span>
<span class="term-kind">Ontological</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="term-detail" hidden="" id="detail-non-derivative">
<div class="detail-inner"><p class="field-label">Definition</p><p>That whose being depends on nothing else in order to exist. It does not receive actuality from another; derivative actuality depends upon it. It is the Non-Derivative Ground on which the invariant Now depends.</p>
<p class="field-label">Function</p><p class="function-text">Prevents the invariant Now from being treated as self-grounding or as the ultimate explanation of actuality.</p>
<a class="entry-link" href="/lexicon/#non-derivative">Open full Lexicon entry <span aria-hidden="true">↗</span></a>
</div>
</div>
</article>
<article class="term-card" id="now">
<button aria-controls="detail-now" aria-expanded="false" class="term-toggle" type="button">
<span class="term-number">02</span>
<span class="term-heading"><span class="term-name">Now (ontological)</span><span class="term-summary">The invariant zero-thickness condition of actualization; succession does not occur within it.</span></span>
<span class="term-kind">Ontological</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="term-detail" hidden="" id="detail-now">
<div class="detail-inner"><p class="field-label">Definition</p><p>The invariant zero-thickness condition at which every created actuality becomes actual. The Now does not flow, elapse, or contain succession. A present is actualized at it; succession belongs to the irreversible order among constituted actualities.</p>
<p class="field-label">Function</p><p class="function-text">The crossing of the lemniscate: the invariant condition at which a present is constituted through inheritance and reception; in rational agents, it is where free response and reorientation become effective.</p>
<a class="entry-link" href="/lexicon/#now">Open full Lexicon entry <span aria-hidden="true">↗</span></a>
</div>
</div>
</article>
<article class="term-card" id="condensation">
<button aria-controls="detail-condensation" aria-expanded="false" class="term-toggle" type="button">
<span class="term-number">03</span>
<span class="term-heading"><span class="term-name">Condensation</span><span class="term-summary">The constitution of a present from inheritance and reception at the invariant Now.</span></span>
<span class="term-kind">Structural</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="term-detail" hidden="" id="detail-condensation">
<div class="detail-inner"><p class="field-label">Definition</p><p>The constitution by which what is inherited from the past and what is newly received are gathered into one present actuality at the invariant Now. Inheritance and reception are not successive phases inside the Now.</p>
<p class="field-label">Function</p><p class="function-text">Explains continuity without reducing becoming to replacement: the past is carried, novelty is received, and the constituted present can leave a trace.</p>
<a class="entry-link" href="/lexicon/#condensation">Open full Lexicon entry <span aria-hidden="true">↗</span></a>
</div>
</div>
</article>
<article class="term-card" id="inheritance">
<button aria-controls="detail-inheritance" aria-expanded="false" class="term-toggle" type="button">
<span class="term-number">04</span>
<span class="term-heading"><span class="term-name">Inheritance</span><span class="term-summary">The past insofar as it is carried constitutively into a present actuality.</span></span>
<span class="term-kind">Structural</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="term-detail" hidden="" id="detail-inheritance">
<div class="detail-inner"><p class="field-label">Definition</p><p>What already constituted actuality contributes to the present: continuity of history, trace, structural inertia, and inherited determination. It is the past insofar as it is carried constitutively into the present.</p>
<p class="field-label">Function</p><p class="function-text">Makes continuity and historical legibility intelligible without treating inherited content as the source of the subject’s numerical identity or placing a temporal “before” inside the Now.</p>
<a class="entry-link" href="/lexicon/#inheritance">Open full Lexicon entry <span aria-hidden="true">↗</span></a>
</div>
</div>
</article>
<article class="term-card" id="reception">
<button aria-controls="detail-reception" aria-expanded="false" class="term-toggle" type="button">
<span class="term-number">05</span>
<span class="term-heading"><span class="term-name">Reception</span><span class="term-summary">What is newly given and cannot be derived from inheritance alone.</span></span>
<span class="term-kind">Structural</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="term-detail" hidden="" id="detail-reception">
<div class="detail-inner"><p class="field-label">Definition</p><p>What is newly given in the constitution of the present and cannot be derived from inheritance alone. Reception is co-constitutive with inheritance rather than a later phase within the crossing.</p>
<p class="field-label">Function</p><p class="function-text">Prevents inheritance from exhausting present actuality, thereby preserving structural openness to genuine novelty, free response, transformation, and, in the theological register, grace.</p>
<a class="entry-link" href="/lexicon/#reception">Open full Lexicon entry <span aria-hidden="true">↗</span></a>
</div>
</div>
</article>
<article class="term-card" id="confluence">
<button aria-controls="detail-confluence" aria-expanded="false" class="term-toggle" type="button">
<span class="term-number">06</span>
<span class="term-heading"><span class="term-name">Confluence</span><span class="term-summary">Distinct trajectories gather into one actuality at the Now without losing their differences.</span></span>
<span class="term-kind">Relational</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="term-detail" hidden="" id="detail-confluence">
<div class="detail-inner"><p class="field-label">Definition</p><p>The gathering of distinct trajectories into a single actuality at the Now, without erasing their differences.</p>
<p class="field-label">Function</p><p class="function-text">Confluence names the relational unity through which multiple inheritances, receptions, and conditions become jointly constitutive of one actuality. It is not merger: what gathers remains distinct even as it becomes one in the actuality it helps constitute.</p>
<a class="entry-link" href="/lexicon/#confluence">Open full Lexicon entry <span aria-hidden="true">↗</span></a>
</div>
</div>
</article>
<article class="term-card" id="present">
<button aria-controls="detail-present" aria-expanded="false" class="term-toggle" type="button">
<span class="term-number">07</span>
<span class="term-heading"><span class="term-name">Present</span><span class="term-summary">The temporal actuality constituted at the Now; it is not the Now itself.</span></span>
<span class="term-kind">Ontological</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="term-detail" hidden="" id="detail-present">
<div class="detail-inner"><p class="field-label">Definition</p><p>The actuality constituted at the Now through the condensation of inheritance and reception. The Now is the invariant condition of actualization; the present is what becomes actually constituted.</p>
<p class="field-label">Function</p><p class="function-text">Provides the constituted temporal actuality from which irreversible temporal relations arise and within which, for agents, action becomes effective; once constituted, it can enter the inherited past.</p>
<a class="entry-link" href="/lexicon/#present">Open full Lexicon entry <span aria-hidden="true">↗</span></a>
</div>
</div>
</article>
<article class="term-card" id="temporal-density">
<button aria-controls="detail-temporal-density" aria-expanded="false" class="term-toggle" type="button">
<span class="term-number">08</span>
<span class="term-heading"><span class="term-name">Temporal density</span><span class="term-summary">The referential scope disclosed by a crossing without adding thickness to the Now.</span></span>
<span class="term-kind">Ontological</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="term-detail" hidden="" id="detail-temporal-density">
<div class="detail-inner"><p class="field-label">Definition</p><p>The extent of a trajectory structurally implicated in a single actuality constituted at the zero-thickness Now, and therefore capable of being disclosed from that crossing, without adding duration or thickness to the Now itself.</p>
<p class="field-label">Function</p><p class="function-text">Explains why one crossing may disclose or reorient more of a life than a much longer span of repetition.</p>
<a class="entry-link" href="/lexicon/#temporal-density">Open full Lexicon entry <span aria-hidden="true">↗</span></a>
</div>
</div>
</article>
<article class="term-card" id="structural-inertia">
<button aria-controls="detail-structural-inertia" aria-expanded="false" class="term-toggle" type="button">
<span class="term-number">09</span>
<span class="term-heading"><span class="term-name">Structural inertia</span><span class="term-summary">The resistance to change produced by traces carried across constituted presents.</span></span>
<span class="term-kind">Structural</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="term-detail" hidden="" id="detail-structural-inertia">
<div class="detail-inner"><p class="field-label">Definition</p><p>The structural persistence produced by traces carried across constituted presents. In agents, repeated acts can deepen that persistence, making subsequent reorientation easier or harder.</p>
<p class="field-label">Function</p><p class="function-text">Explains habit, fixation, and why repeated acts can make later reorientation easier or harder.</p>
<a class="entry-link" href="/lexicon/#structural-inertia">Open full Lexicon entry <span aria-hidden="true">↗</span></a>
</div>
</div>
</article>
</div>
<aside class="history-note"><p class="history-label">A note on conceptual development</p><p>Earlier essays use <strong>temporal density</strong> in a phenomenological sense—the felt depth or weight of a moment. In the developed framework, the term is defined ontologically as the referential scope of a zero-thickness crossing. The two senses are related but not identical.</p></aside>
</section>
<section aria-labelledby="props-title" class="section">
<p class="section-kicker">03 · Foundational layer</p><h2 id="props-title">Foundational propositions</h2>
<p class="section-intro">Five propositions state the framework's structural commitments. Open one to read its formulation and the terms it draws on.</p>
<div class="props"><article class="prop-card" id="p1">
<button aria-controls="body-p1" aria-expanded="false" class="prop-toggle" type="button">
<span class="prop-number">P1</span><span class="prop-name">Actuality and the invariant Now</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="prop-body" hidden="" id="body-p1"><div class="detail-inner"><p>Every created actuality is actualized only at the invariant Now. The Now is not itself an event or duration, but the zero-thickness condition at which a present is constituted.</p><p class="field-label">Draws on</p><div class="rel-pills"><a class="rel-pill" href="/lexicon/#now">Now (ontological)</a><a class="rel-pill" href="/lexicon/#non-derivative">Non-derivative</a><a class="rel-pill" href="/lexicon/#present">Present</a></div></div></div>
</article>
<article class="prop-card" id="p2">
<button aria-controls="body-p2" aria-expanded="false" class="prop-toggle" type="button">
<span class="prop-number">P2</span><span class="prop-name">Condensation</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="prop-body" hidden="" id="body-p2"><div class="detail-inner"><p>A present is constituted through condensation from inheritance and reception. These are co-constitutive dimensions of the present, not successive stages within the Now. Confluence names the relational unity through which distinct trajectories jointly contribute to one actuality without erasing their differences; it is not a further temporal stage.</p><p class="field-label">Draws on</p><div class="rel-pills"><a class="rel-pill" href="/lexicon/#condensation">Condensation</a><a class="rel-pill" href="/lexicon/#inheritance">Inheritance</a><a class="rel-pill" href="/lexicon/#reception">Reception</a><a class="rel-pill" href="/lexicon/#confluence">Confluence</a></div></div></div>
</article>
<article class="prop-card" id="p3">
<button aria-controls="body-p3" aria-expanded="false" class="prop-toggle" type="button">
<span class="prop-number">P3</span><span class="prop-name">Temporal order</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="prop-body" hidden="" id="body-p3"><div class="detail-inner"><p>Created time is the irreversible order of relations among constituted actualities. Succession belongs to this temporal order, not to the invariant Now itself.</p><p class="field-label">Draws on</p><div class="rel-pills"><a class="rel-pill" href="/lexicon/#present">Present</a><a class="rel-pill" href="/lexicon/#condensation">Condensation</a><a class="rel-pill" href="/lexicon/#inheritance">Inheritance</a></div></div></div>
</article>
<article class="prop-card" id="p4">
<button aria-controls="body-p4" aria-expanded="false" class="prop-toggle" type="button">
<span class="prop-number">P4</span><span class="prop-name">Eternal Presence</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="prop-body" hidden="" id="body-p4"><div class="detail-inner"><p>The Non-Derivative Ground sustains the invariant Now and created actuality without entering temporal succession. It is present as Ground of actuality, not as an event, term, or constituent within the temporal series.</p><p class="field-label">Draws on</p><div class="rel-pills"><a class="rel-pill" href="/lexicon/#non-derivative">Non-derivative</a><a class="rel-pill" href="/lexicon/#now">Now (ontological)</a></div></div></div>
</article>
<article class="prop-card" id="p5">
<button aria-controls="body-p5" aria-expanded="false" class="prop-toggle" type="button">
<span class="prop-number">P5</span><span class="prop-name">Lemniscatic structure</span><span aria-hidden="true" class="chevron">⌄</span>
</button>
<div class="prop-body" hidden="" id="body-p5"><div class="detail-inner"><p>The topology is lemniscatic because continuity and openness coexist at every crossing: inheritance carries forward what has been constituted while reception leaves genuine novelty open.</p><p class="field-label">Draws on</p><div class="rel-pills"><a class="rel-pill" href="/lexicon/#inheritance">Inheritance</a><a class="rel-pill" href="/lexicon/#reception">Reception</a><a class="rel-pill" href="/lexicon/#now">Now (ontological)</a></div></div></div>
</article></div>
</section>
<footer class="rf-foot"><span>Gaitan Topology · Research Framework</span><span><a href="/lexicon/">Full Lexicon</a> · <a href="/lexico/">Léxico</a></span></footer>
</div>

<script>
(function () {
  function initFramework() {
    const root = document.querySelector('.rf-wrap');
    if (!root) return;
    const termButtons = Array.from(root.querySelectorAll('.term-toggle'));
    const propButtons = Array.from(root.querySelectorAll('.prop-toggle'));

    function setExpanded(button, open, group) {
      const panelId = button.getAttribute('aria-controls');
      const panel = document.getElementById(panelId);
      if (!panel) return;
      group.forEach(other => {
        const otherPanel = document.getElementById(other.getAttribute('aria-controls'));
        const isCurrent = other === button;
        other.setAttribute('aria-expanded', String(isCurrent && open));
        if (otherPanel) otherPanel.hidden = !(isCurrent && open);
        const card = other.closest('.term-card, .prop-card');
        if (card) card.classList.toggle('open', isCurrent && open);
      });
    }

    termButtons.forEach(button => button.addEventListener('click', () => {
      setExpanded(button, button.getAttribute('aria-expanded') !== 'true', termButtons);
    }));
    propButtons.forEach(button => button.addEventListener('click', () => {
      setExpanded(button, button.getAttribute('aria-expanded') !== 'true', propButtons);
    }));

    function openTargetFromHash() {
      const hash = decodeURIComponent(window.location.hash.slice(1));
      if (!hash) return;
      const target = document.getElementById(hash);
      if (!target) return;
      const termButton = target.matches('.term-card') ? target.querySelector('.term-toggle') : null;
      const propButton = target.matches('.prop-card') ? target.querySelector('.prop-toggle') : null;
      if (termButton) setExpanded(termButton, true, termButtons);
      if (propButton) setExpanded(propButton, true, propButtons);
      if (termButton || propButton) {
        window.setTimeout(() => target.scrollIntoView({
          behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth',
          block: 'center'
        }), 40);
      }
    }
    openTargetFromHash();
    window.addEventListener('hashchange', openTargetFromHash);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initFramework);
  else initFramework();
})();
</script>
