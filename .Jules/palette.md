## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-23 - Semantic Buttons & Focus Visibility
**Learning:** Using `<div>` or `<a>` for JavaScript-driven actions prevents native keyboard focus and correct screen reader roles. `outline: none` without a `:focus-visible` alternative makes the site unusable for keyboard-only users.
**Action:** Always refactor JS-driven navigation and toggles to `<button type="button">`. Use `:focus-visible` for custom focus indicators and never use `outline: none` on interactive elements without providing an accessible alternative.
