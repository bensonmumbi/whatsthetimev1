## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-08-08 - Persisting Visual State Feedback Colors Under Active CSS Hover States
**Learning:** CSS rules with pseudo-classes like `:hover` in style sheets will override regular JS inline styling (e.g. `element.style.background = '#059669'`) because the `:hover` pseudo-class applies specifically to the hovered state, whereas general inline styles only define the base state.
**Action:** When providing temporary visual feedback (like 'Copied!' success green) on elements that are likely to be actively hovered, use `element.style.setProperty('background', '#059669', 'important')` and clear it using `element.style.removeProperty('background')` once the feedback duration completes.
