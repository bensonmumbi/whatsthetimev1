## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-09 - Semantic Buttons & Keyboard Focus
**Learning:** Using `<a>` tags without `href` for JS-driven actions breaks keyboard accessibility by default. Converting these to semantic `<button>` elements restores tab-index and "Enter" key support. Adding `:focus-visible` styles ensures a clear focus indicator for keyboard users without affecting mouse users.
**Action:** Replace pseudo-links (a[onclick]) with `<button>` and apply `:focus-visible` rings consistent with the brand's accent color.
