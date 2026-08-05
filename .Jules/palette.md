## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-08-05 - Semantic Interactive Elements & Focus Baselines
**Learning:** Overusing non-interactive HTML tags (like `<div>` or `<a>` without an `href`) for clickable triggers breaks basic keyboard accessibility and screen readers. Implementing a global focus-visible outline paired with semantic `<button>` tag conversions handles both keyboard focus traps and assistive tech compliance perfectly.
**Action:** Convert plain `div` click target wrappers to semantic `<button type="button">` with custom reset rules and ensure focus-visible styles are globally declared.
