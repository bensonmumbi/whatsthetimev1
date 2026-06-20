## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-20 - Semantic Buttons and Global Focus Visibility
**Learning:** Refactoring non-semantic interactive elements (like `<a>` with only `onclick` or `<div>`) to `<button type="button">` is essential for screen reader support and native keyboard focus. A global `:focus-visible` rule using the brand accent color provides high-contrast feedback for keyboard users while remaining invisible to mouse users.
**Action:** Audit interfaces for "fake" buttons and replace them with semantic `<button>` elements. Always remove `outline: none` and replace it with a purposeful `:focus-visible` style.
