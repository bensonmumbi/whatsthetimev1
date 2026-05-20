## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-05-20 - CSS Specificity and :focus-visible
**Learning:** Global `:focus-visible` styles can be easily overridden by more specific selectors (like `.class:focus`) that include `outline: none`. This silently breaks keyboard accessibility for those specific elements.
**Action:** Avoid using `outline: none` in specific focus selectors unless providing a high-contrast alternative. Always verify focus indicators on specific form elements after applying global accessibility styles.
