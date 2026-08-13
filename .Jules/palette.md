## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-08-13 - Focus Styles and Form Association in Modals
**Learning:** For elements with custom onclick-driven navigation (like header/footer navigation <a> links), adding `href="javascript:void(0)"` enables native keyboard focus and activation without adding custom focus-handling logic. Adding a global `*:focus-visible` outline ensures a clear, high-contrast visual focus indicator for keyboard navigators, keeping form controls accessible.
**Action:** Always verify custom navigational links are natively focusable and style them with robust `:focus-visible` outlines. Ensure modal inputs are properly associated with `<label>` tags via the `for` attribute for screen reader compatibility.
