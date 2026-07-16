# Design Rules

House rules for this project's UI. These come from direct design review — the
goal is to avoid patterns that read as "generic AI-generated" and keep the work
looking intentional and professional. Apply them to every page and component.

---

## 1. No decorative accent dash before labels

Don't put a small decorative line/dash before eyebrows, kickers, or section
labels (e.g. a `::before` rendering a short colored bar).

- **Why:** it's a stock AI-generator flourish that adds no meaning.
- **Instead:** let the label stand on its own, or use an existing brand element
  (e.g. the honeycomb dot) if a marker is genuinely needed.

```css
/* Avoid */
.eyebrow::before { content: ""; width: 26px; height: 2px; background: var(--yellow); }
```

## 2. Never use the em-dash (—)

Do not use the long dash `—` anywhere in visible copy (headings, body, titles,
footers, alt text). It's one of the clearest tells of AI-written text.

- **Instead**, pick the punctuation that actually fits the sentence:
  - **Colon** when a clause introduces detail — `"...nos komunidat: riesgonan ku..."`
  - **Parentheses** for an aside — `"...vulnerabel (hende grandi, mucha...) i esnan afektá"`
  - **Comma** for a light pause, or a **period** to split into two sentences
  - **`·` (middot)** or **`/`** as a separator in titles, tags, and lists
- Hyphens `-` in compound words (e.g. `EHBO-kit`) are fine — this rule is only
  about the long dash `—`.

## 3. No left-accent-border callout boxes

Don't build callouts/notes as a box with a colored left border and rounded
corners (the classic `border-left: 4px solid; border-radius:` alert card).

- **Why:** it's a default AI-generator/Bootstrap-era pattern.
- **Instead:** use a clean card — a full 1px border **or** a solid fill — with
  uniform corner radius. Emphasis comes from the content, not an accent bar.

```css
/* Avoid */
.note { background: var(--paper); border-left: 5px solid var(--yellow); border-radius: 0 8px 8px 0; }

/* Prefer */
.note { background: var(--paper); border: 1px solid var(--gray-line); border-radius: 12px; }
```

*Exception:* only use a colored accent bar if there's a deliberate reason
(e.g. a system that maps colors to severity levels) — not as default decoration.

## 4. No emoji / emoticons — use flat SVG icons

Never use chat- or social-media-style emoji (🔥 ❄ 🌐 📞 🏛 etc.) as UI icons.

- **Why:** emoji render inconsistently across platforms and look unprofessional.
- **Instead:** use flat, stroke-based inline SVG icons that match the project's
  icon style: `viewBox="0 0 24 24"`, `fill: none`, `stroke: currentColor`
  (or a brand color), `stroke-width` ~1.8–2, rounded line caps/joins. Size the
  icon to sit inline with its label.

```html
<!-- Avoid -->
<span class="tag">🔥 Fase kayente</span>

<!-- Prefer -->
<span class="tag"><svg viewBox="0 0 24 24"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3..."/></svg> Fase kayente</span>
```

## 5. Calm, simple headers

Headings use **Archivo (Bold, ~700)** in **sentence case**, not Archivo Black in ALL CAPS.
Keep them powerful and professional, but slightly smaller and subtler.

- **Why:** heavy uppercase display type across every heading reads as loud and
  restless. A single bold weight in sentence case is calmer and more legible.
- Numeric/stat display elements (big "3", stat counters) may keep Archivo Black.
- Small UI labels (kickers, tags, nav, buttons) may stay in caps — this rule is
  about the section/content **headers**.

## 6. Restrained accent color

Yellow is an accent, not a texture. Use it for the primary CTA, the logo, the
brand word, and section kickers. Avoid sprinkling it on every hover, underline,
border and arrow.

- Neutralize repetitive micro-accents (nav hover underline, icon hover swaps) to
  black/gray. Keep the palette calm and consistent.

## 7. Provided content first; mark placeholders

Use the client's supplied content (`Website Content uitwerking.docx`) as the
source of truth. Where the design needs text/media that wasn't supplied:

- Use **Lorem ipsum** for filler copy, and
- Add a visible **`.content-todo`** marker (e.g. "⚠ … aan te leveren") so it's
  obvious what the client still needs to deliver. Never present invented facts
  (kit lists, phone numbers, document links) as final.

---

### Quick checklist before shipping a component
- [ ] No decorative accent dash before labels
- [ ] Zero `—` em-dashes in visible text
- [ ] No left-border rounded callout boxes
- [ ] No emoji in the UI — flat SVG icons only
- [ ] Headers in Archivo Bold, sentence case (not Black caps)
- [ ] Yellow reserved for CTAs / brand / kickers, not every accent
- [ ] Invented content uses Lorem ipsum + a `.content-todo` marker
