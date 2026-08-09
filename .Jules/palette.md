## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-08-09 - Copy-to-Clipboard Micro-Feedback Pattern
**Learning:** Absolutely-positioned copy buttons on read-only textareas dramatically reduce user friction compared to simple text selection. Providing instant visual feedback (changing text to "Copied!" and shifting background to a success color like `#059669`) prevents repeated, uncertain clicks.
**Action:** When implementing copy-to-clipboard interactions, always pair them with clear visual transitions (such as green color flashes and text updates) that auto-revert after a 2-second timeout.
