## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-22 - Semantic Refactoring and CSS Selectors
**Learning:** When refactoring non-semantic tags (like `<a>` or `<div>`) to semantic `<button>` elements, it is critical to perform a global search for CSS selectors targeting the old tags. Failure to update CSS selectors leads to immediate visual regressions (e.g., lost active/hover states).
**Action:** Always update associated CSS rules and JS selectors simultaneously when changing element types. Use `:focus-visible` for a cleaner UX that respects both keyboard and mouse users.
