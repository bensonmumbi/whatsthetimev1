## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-19 - Semantic Navigation Buttons & Focus Visibility
**Learning:** Using `<a>` tags without `href` for JS actions breaks keyboard navigation as they aren't focusable by default. Converting them to `<button type="button">` with a CSS reset maintains the design while fixing accessibility. Global `:focus-visible` styles are essential for keyboard users to track their position.
**Action:** Replace all non-link interactive elements with `<button>`. Use a CSS reset selector to match the visual design of surrounding text/links while ensuring accessibility. Always include a global `:focus-visible` ring.
