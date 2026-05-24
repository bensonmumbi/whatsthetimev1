## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-05-24 - Keyboard Focusability for Custom Navigation
**Learning:** Using `<a>` tags with `onclick` but without `href` removes them from the document's tab order, making them inaccessible to keyboard users. Combining `href="javascript:void(0)"` with a global `:focus-visible` style ensures accessibility while maintaining the SPA's navigation logic.
**Action:** Audit all interactive elements for inclusion in the tab order. Use `href="javascript:void(0)"` for non-link anchors and always provide a high-contrast `:focus-visible` indicator.
