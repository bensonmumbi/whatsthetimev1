## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-10 - Semantic Navigation & Clipboard Feedback
**Learning:** Using `<a>` tags for JavaScript-only triggers without `href` is an accessibility anti-pattern. Semantic `<button>` elements with `:focus-visible` styles provide superior keyboard and screen reader support. Providing immediate visual feedback (e.g., "Copied!") after clipboard actions significantly improves user confidence.
**Action:** Always use `<button>` for interactive elements that don't navigate to a new URL. Implement visual state changes for async or background actions like "Copy to clipboard".
