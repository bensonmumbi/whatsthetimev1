## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-02 - Code Snippet Copy Button with Feedback
**Learning:** For embeddable widgets or code snippets, a dedicated "Copy" button with immediate visual feedback ("Copied!") reduces friction and provides clear confirmation. Using absolute positioning over a non-resizable textarea ensures the button remains accessible and visually consistent regardless of content length.
**Action:** Always include a copy-to-clipboard action for any user-facing code or configuration strings. Implement visual feedback that reverts after a short delay (e.g., 2 seconds).
