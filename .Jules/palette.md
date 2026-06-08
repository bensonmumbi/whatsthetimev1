## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-08 - Semantic Buttons & Focus Visibility
**Learning:** Using semantic `<button>` elements instead of `<div>` or `<a>` for JavaScript-driven actions is essential for keyboard accessibility. A global `:focus-visible` style ensures that users can navigate predictably without degrading the experience for mouse users.
**Action:** Audit all interactive elements to ensure they use proper semantic tags. Implement a consistent `:focus-visible` outline across the application.
