## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-12 - Embed Code Copy Button & Feedback
**Learning:** Adding a "Copy" button for embed codes/snippets is a high-value micro-UX win. Providing immediate visual feedback ("Copied!") and handling Clipboard API feature detection ensures a smooth and robust experience.
**Action:** Implement "Copy" buttons for any user-facing code or configuration snippets. Always include visual feedback (color/text change) and a fallback/detection for the Clipboard API.
