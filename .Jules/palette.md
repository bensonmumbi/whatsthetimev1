## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-27 - Absolute Position Copy Button with Direct DOM Reset
**Learning:** Providing a "Copy" button directly adjacent or positioned absolutely inside a readonly text container improves copy-paste flows significantly. Immersive feedback like changing color/text to "Copied!" for 2 seconds should reset background styles directly back to default without using `!important` in order to preserve hover effects correctly.
**Action:** Always wrap copyable text areas in a relative container when implementing inline copy buttons. Apply an `aria-label` to the copyable area and the button to ensure clear screen-reader feedback, and handle timeouts gracefully by clearing previous timers and resetting style variables directly.
