## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-08-12 - Semantic Modal Selection Elements & Selection States
**Learning:** Using `<div>` wrappers with custom click handlers for choice/selection elements inside modals blocks keyboard navigation and screen readers entirely. Refactoring these options into semantic `<button type="button">` components paired with `aria-pressed` states ensures fully accessible keyboard selection and screen reader navigation out-of-the-box.
**Action:** Always use `<button type="button">` instead of clickable `<div>` elements for custom cards/grids acting as choices, and pair them with standard focus styles and appropriate `aria-pressed` attributes.
