## 2026-08-27 - Accordion Header Accessibility & Focus States
**Learning:** Accordion headers implemented as `<div>` elements with `onclick` handlers lack built-in keyboard navigation (Tab/Enter/Space) and fail to communicate open/closed state to assistive technologies.
**Action:** Always use `<button type="button">` for accordion toggle headers with CSS button resets (`background: none; border: none; width: 100%; text-align: left;`) and dynamically update `aria-expanded="true|false"`.

## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.
