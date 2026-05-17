## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-05-17 - Keyboard Accessibility and Focus States in Static SPAs
**Learning:** Using `href="javascript:void(0)"` on navigation elements in a static SPA ensures they are part of the tab order without requiring tag changes that might conflict with existing CSS. A global `:focus-visible` rule using existing accent variables ensures consistent keyboard navigation feedback.
**Action:** Apply `href="javascript:void(0)"` to any `<a>` tags used for SPA navigation and include a global `:focus-visible` rule in the site's base styles.
