## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-08-11 - Anchor Links Keyboard Accessibility and Focus States
**Learning:** Anchor tags (`<a>`) used purely for JavaScript-driven interactive views or navigation must have `href="javascript:void(0)"` or a proper `tabindex` to remain in the browser's default keyboard focus tab order. Additionally, styling the focus indicator via `*:focus-visible` using the design system's accent color dramatically improves accessibility and guarantees visual feedback for keyboard-navigating users.
**Action:** Always ensure that any interactive link or anchor tag contains `href="javascript:void(0)"` to facilitate keyboard focus and standard Enter-key activation. Define clear global `focus-visible` styles to provide visible focus rings.
