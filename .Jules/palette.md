## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-13 - Semantic Buttons & Focus Visibility
**Learning:** In static HTML projects, interactive elements are often implemented as `<a>` or `<div>` tags, which breaks keyboard navigation. Replacing these with semantic `<button>` elements and restoring focus visibility via `:focus-visible` (after removing generic `outline: none`) is a high-impact, low-risk accessibility win.
**Action:** Audit for pseudo-links (`<a>` with `onclick` but no `href`) and interactive containers. Use a global `:focus-visible` rule with `outline-offset` to ensure high-contrast focus indicators across all components.
