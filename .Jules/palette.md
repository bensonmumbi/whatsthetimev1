## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-11 - Focus Visibility and Clipboard Feedback
**Learning:** Global `:focus-visible` styles are a low-effort, high-impact accessibility win that avoids visual noise for mouse users. For clipboard operations, providing a clear "Copied!" state with a color shift (e.g., to a success green) significantly improves user confidence.
**Action:** Implement `:focus-visible` early in projects. Always include visual feedback for "Copy" buttons, and use `clearTimeout` to handle overlapping interaction timers.
