#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
patch_shelves.py — add `shelf:` (and series fields) to every post's front matter.

Run from the repository root:   python3 patch_shelves.py          (dry run, default)
                                python3 patch_shelves.py --write  (apply changes)

Design (per repo conventions):
  * Key is the normalized DOI from each post's `doi:` field — never the filename
    or title. Posts whose DOI is not in the map are REPORTED and left untouched;
    they will appear in the library's visible "Unshelved" section.
  * Idempotent: re-running updates existing shelf/series lines in place.
  * Front matter = the FIRST two exact `---` lines; body `---` dividers in
    older posts are left untouched. Safety: the file's total delimiter count
    must be unchanged by the patch; any anomaly aborts that file with no write.
  * UTF-8 read/write throughout (Spanish posts).
"""

import io, os, re, sys, glob

WRITE = "--write" in sys.argv
POSTS_DIR = "_posts"

# ---------------------------------------------------------------------------
# DOI -> (shelf, series, series_order, series_label)
# Both language editions of an essay share the same classification.
# ---------------------------------------------------------------------------
def pair(en, es, shelf, series=None, order=None, label=None):
    out = {en: (shelf, series, order, label)}
    if es:
        out[es] = (shelf, series, order, label)
    return out

M = {}

# GT-A1 · The Lemniscate
M.update(pair("19121110", "19121592", "gt-a1"))   # A Topology of Memory, Possibility, and Grace
M.update(pair("20479112", "20479198", "gt-a1"))   # The Lemniscate Model of Time
M.update(pair("19339347", "19358491", "gt-a1"))   # The Topology of Presence
M.update(pair("19410632", "19410726", "gt-a1"))   # The Alternate Lemniscate

# GT-A2 · The Now and Temporal Structure
M.update(pair("21178454", "21178245", "gt-a2"))   # When Is the Present?
M.update(pair("21177683", "21178047", "gt-a2"))   # The Weight of the Present
M.update(pair("19581285", "19581332", "gt-a2"))   # Where Does Time End? The Three Nows
M.update(pair("20681867", "20681996", "gt-a2"))   # Consummatum Est
M.update(pair("19502525", "19513936", "gt-a2"))   # Does Time Need Me, or Do I Need Time?
M.update(pair("19599170", "19599225", "gt-a2"))   # You Cannot Add One Hour
M.update(pair("19475979", "19476198", "gt-a2"))   # One Day
M.update(pair("20112294", "20112562", "gt-a2"))   # Alpha and Omega
M.update(pair("20584730", "20584786", "gt-a2"))   # God, the Universe, and the Now

# GT-B1 · The Ground Itself
M.update(pair("19654743", "19655047", "gt-b1"))   # The Is and the AM
M.update(pair("19842987", "19843193", "gt-b1"))   # The Am That Remains
M.update(pair("20710961", "20711078", "gt-b1"))   # The Ground That Does Not Appear
M.update(pair("20369064", "20369087", "gt-b1"))   # Zero and One: Dust and Ashes
M.update(pair("19893877", "19894007", "gt-b1"))   # Zero Returned
M.update(pair("21313368", "21313477", "gt-b1"))   # The Chicken, the Egg...
M.update(pair("21610192", "21610466", "gt-b1"))   # Relative to What?
M.update(pair("21209972", "21210203", "gt-b1"))   # The Rose and the Stone

# GT-B2 · The God Who Is Not
M.update(pair("20435134", "20435149", "gt-b2"))   # The Corridor
M.update(pair("20044781", "20044903", "gt-b2"))   # Where Is God?
M.update(pair("21459842", "21459972", "gt-b2"))   # Not Gepetto
M.update(pair("19702597", "19702737", "gt-b2"))   # The Debt Collector at the Center

# GT-C1 · The Ghost Zone Series  (Ghost Zone & Heroic Illusion: English only)
M.update(pair("19100268", None,       "gt-c1", "ghost-zone", 1))  # The Ghost Zone
M.update(pair("19224539", None,       "gt-c1", "ghost-zone", 2))  # The Heroic Illusion
M.update(pair("19685642", "19685712", "gt-c1", "ghost-zone", 3))  # Das Man and the First Person Singular

# GT-C2 · Interiority and Identity
M.update(pair("20032817", "20032897", "gt-c2"))   # The Infinite Interior
M.update(pair("20087687", "20088406", "gt-c2"))   # Against You Alone
M.update(pair("20450355", "20450398", "gt-c2"))   # Jenny Curran

# GT-C3 · Heidegger Dialogues
M.update(pair("19684052", "19684135", "gt-c3"))   # Two Meanings of 'is'

# GT-D · The Monadology (ordered trilogy)
M.update(pair("21419392", "21419441", "gt-d", "monadology", 1))   # The Monad That Receives
M.update(pair("21433024", "21433054", "gt-d", "monadology", 2))   # Legion of Monads
M.update(pair("21444690", "21444762", "gt-d", "monadology", 3))   # The Family of Crossing Points

# GT-E · Divine Knowledge: The Fig Tree Line (ordered; Presence is the Coda)
M.update(pair("21565530", "21566015", "gt-e", "fig-tree", 1))     # Under the Fig Tree
M.update(pair("21609182", "21609515", "gt-e", "fig-tree", 2))     # The Merchants of Teman
M.update(pair("21628894", "21629099", "gt-e", "fig-tree", 3))     # No One Under the Fig Tree
M.update(pair("21633618", "21633686", "gt-e", "fig-tree", 4))     # The Eyes He Does Not Need
M.update(pair("21633809", "21633875", "gt-e", "fig-tree", 5))     # The Ground That Knows
M.update(pair("21635777", "21635822", "gt-e", "fig-tree", 6))     # The Ground We Leave
M.update(pair("21639305", "21639415", "gt-e", "fig-tree", 7, "Coda"))  # Presence

# GT-F1 · Thresholds
M.update(pair("21516022", "21516066", "gt-f1"))   # Born from Above
M.update(pair("20724404", "20724427", "gt-f1"))   # The Two Entrances
M.update(pair("20708609", "20708633", "gt-f1"))   # The Topology of Absolution

# GT-F2 · Eucharist
M.update(pair("21514025", "21514225", "gt-f2"))   # Trace and Presence
M.update(pair("21208903", "21208989", "gt-f2"))   # The Condensed Cross

# GT-F3 · Mercy
M.update(pair("20385950", "20386008", "gt-f3"))   # Where Mercy Lives
M.update(pair("20277539", "20277874", "gt-f3"))   # The Mercy of Time
M.update(pair("19558895", "19559034", "gt-f3"))   # Where Are You?
M.update(pair("19476335", "19476451", "gt-f3"))   # Why the Center Does Not Run Out

# GT-G · Temptation and the Will
M.update(pair("21046187", "21046390", "gt-g"))    # Eating Stones
M.update(pair("21079828", "21080024", "gt-g"))    # The Inverse Miracle
M.update(pair("21464865", "21464947", "gt-g"))    # Not the Root

# GT-H · Moral Topology
M.update(pair("20738126", "20738167", "gt-h"))    # The Servant of Servants
M.update(pair("20801344", "20801435", "gt-h"))    # The Place That Is Given
M.update(pair("20146258", "20146381", "gt-h"))    # On Happiness

# GT-I · Displacement and the Algorithmic Age
M.update(pair("19379289", "19389347", "gt-i"))    # The Serpent, the Self, and the Collapse of the "I"
M.update(pair("19870770", "19870865", "gt-i"))    # The Artificial Selection
M.update(pair("20100162", "20100210", "gt-i"))    # De-Roling God
M.update(pair("20330645", "20330711", "gt-i"))    # Eve's Algorithm
M.update(pair("20242868", "20243460", "gt-i"))    # Non te egeo
M.update(pair("20385839", "20385891", "gt-i"))    # God On-Demand
M.update(pair("20599987", "20600045", "gt-i"))    # Are We Not Entertained?
M.update(pair("20618207", "20618272", "gt-i"))    # The Grammar of Displacement
M.update(pair("21226541", "21226761", "gt-i"))    # Wisdom, Artificial Intelligence, Another Seduction

# GT-J · Letters
M.update(pair("19870600", "19871019", "gt-j"))    # A Letter to an Atheist
M.update(pair("20497560", "20497624", "gt-j"))    # An Open Letter to the Professional Modern Philosopher

# NOTE: the monograph (zenodo 18684516 / 18867864) is deliberately absent —
# it is a book, not a website post.

DOI_RE = re.compile(r"10\.5281/zenodo\.(\d+)")
FIELD_RE = {f: re.compile(r"^%s:.*$" % f, re.M)
            for f in ("shelf", "series", "series_order", "series_label")}

def delimiter_count(text):
    return sum(1 for line in text.splitlines() if line.strip() == "---" and line.startswith("---"))

def front_matter_bounds(lines):
    """Return (open_idx, close_idx) of the two front-matter delimiter lines."""
    idx = [i for i, ln in enumerate(lines) if ln.rstrip("\n").strip() == "---"]
    assert len(idx) >= 2, "fewer than two --- delimiters"
    assert idx[0] == 0, "front matter does not start at line 1"
    return idx[0], idx[1]

patched, skipped, unmapped, errors = [], [], [], []

files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))
assert files, "no files found in _posts/ — run from the repository root"

for path in files:
    try:
        with io.open(path, encoding="utf-8") as fh:
            text = fh.read()

        before_count = delimiter_count(text)
        assert before_count >= 2, "fewer than 2 --- delimiters (%d)" % before_count

        lines = text.splitlines(True)
        o, c = front_matter_bounds(lines)
        fm = "".join(lines[o + 1:c])

        m = DOI_RE.search(fm)
        if not m:
            unmapped.append((path, "no doi: field"))
            continue
        rec_id = m.group(1)
        if rec_id not in M:
            unmapped.append((path, "doi 10.5281/zenodo.%s not in map" % rec_id))
            continue

        shelf, series, order, label = M[rec_id]
        new_fields = [("shelf", shelf)]
        if series:
            new_fields += [("series", series), ("series_order", str(order))]
            if label:
                new_fields += [("series_label", label)]

        # Remove any existing occurrences of the managed fields (idempotence),
        # then insert the fresh block just before the closing delimiter.
        for f, rx in FIELD_RE.items():
            fm = rx.sub("", fm)
        fm = fm.rstrip("\n") + "\n\n"
        fm += "".join("%s: %s\n" % (f, v) for f, v in new_fields)

        new_text = "".join(lines[:o + 1]) + fm + "".join(lines[c:])

        after_count = delimiter_count(new_text)
        assert after_count == before_count, (
            "delimiter count changed: %d -> %d" % (before_count, after_count))
        assert DOI_RE.search(new_text), "doi lost during patch"
        assert ("shelf: %s\n" % shelf) in new_text, "shelf line missing after patch"

        if new_text == text:
            skipped.append(path)
            continue

        if WRITE:
            with io.open(path, "w", encoding="utf-8", newline="") as fh:
                fh.write(new_text)
        patched.append((path, shelf, series or "-", order or "-"))

    except AssertionError as e:
        errors.append((path, str(e)))

mode = "WROTE" if WRITE else "DRY RUN (use --write to apply)"
print("== patch_shelves.py — %s ==" % mode)
print("mapped essays in table: %d DOIs" % len(M))
print("files found: %d | patched: %d | already correct: %d | unmapped: %d | errors: %d"
      % (len(files), len(patched), len(skipped), len(unmapped), len(errors)))
for p, shelf, series, order in patched:
    print("  PATCH  %-70s -> %s %s %s" % (p, shelf, series, order))
for p, why in unmapped:
    print("  UNSHELVED  %-64s (%s)" % (p, why))
for p, why in errors:
    print("  ERROR  %-70s (%s)" % (p, why))

if errors:
    sys.exit(1)
