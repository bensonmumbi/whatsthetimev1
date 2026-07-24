## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-24 - Interactive Clipboard Copy Button Styling State Overrides
**Learning:** When using visual feedback states (like changing background color to success green on copy button click), CSS hover rules using `!important` will override inline JavaScript style overrides when the mouse is still hovering over the button.
**Action:** Avoid using `!important` on general stylesheet hover states like `:hover` for copy buttons. This lets inline JavaScript style overrides (like success state coloring) take natural precedence, and we can revert them on timer timeout simply by clearing the style background property (`element.style.background = ''`).
