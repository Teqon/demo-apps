# Claude Code Instructions for Ami Ta Prepará

## Audience & Accessibility

**Senior citizens are a primary audience for this site.** The Curaçao government's crisis preparedness initiative reaches people across all age groups, with a significant portion being 55+. This affects all design and development decisions:

### Accessibility Rule: Font Sizes for Legibility

- **Minimum body text: 1rem (16px)** — no smaller. Senior users have reduced visual acuity; small text is not accessible.
- **Small UI text (labels, tags, captions): minimum 0.85rem (13.6px)** — avoid cramped controls.
- **Line height: 1.5 or greater** — improves readability. Maintain current values; don't reduce.
- **Contrast: AA minimum (4.5:1 for text)** — text and background must have sufficient contrast.

**Why:** Many seniors experience presbyopia (age-related vision changes). Text at 0.9rem or smaller becomes unreadable. Increasing from 0.92rem to 1.05rem+ improves usability dramatically without changing layout or breaking design.

**When to apply:**
- Never reduce font sizes, even for mobile or constrained spaces
- When adding new text, default to body: 1.1rem, labels: 0.92rem
- If space is tight, use `clamp()` for responsive scaling instead of fixed small sizes
- If you must use a smaller size, justify it (e.g., fine-print disclaimers 0.85rem is acceptable)

**Example:**
```css
/* Good: accessible, no layout change */
.text { font-size: 1.1rem; }
.label { font-size: 0.92rem; }

/* Avoid: too small for senior users */
.text { font-size: 0.9rem; }  /* Too small */
```

## Design Rules

See [DESIGN_RULES.md](./DESIGN_RULES.md) for project-specific design patterns to avoid (AI-generator clichés) and principles to follow.

---

**Last updated:** 2026-07-01  
**Audience context:** Senior citizens, government transparency site
