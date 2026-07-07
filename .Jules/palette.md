## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-07 - "Copy" Button for Embed Code & Visual Feedback
**Learning:** Providing a "Copy" button for code snippets is a critical UX improvement that prevents manual selection errors. Visual feedback ("Copied!") is essential to confirm the action to the user.
**Action:** Use `navigator.clipboard.writeText` for copying and implement a temporary state change on the button (e.g., text content or icon) to provide immediate feedback. Ensure the `textarea` is `readonly` and has an `aria-label`.
