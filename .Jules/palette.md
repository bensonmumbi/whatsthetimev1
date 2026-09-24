## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-08-14 - Keyboard Navigation for In-Page SPA Navigation Anchors & Focus Outline Visibility
**Learning:** In single-page applications (SPAs), `<a>` tags without an `href` attribute (e.g. relying solely on `onclick`) are omitted from standard document tab order by default. Additionally, custom component styling can obscure default browser focus outlines.
**Action:** Always ensure interactive link elements include `href="javascript:void(0)"` or use semantic `<button>` elements to guarantee native keyboard focus and Enter key activation. Pair this with a high-contrast `:focus-visible` CSS rule to maintain visual feedback for keyboard users without affecting mouse clicks.
