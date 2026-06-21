## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-21 - Focus Visibility and Mobile Overlap
**Learning:** Suppressing focus outlines with `outline: none` is a common accessibility anti-pattern that breaks keyboard navigation. Floating elements like "Buy Me a Coffee" buttons can overlap with sticky advertisements on mobile viewports, creating a "cluttered" and inaccessible UI.
**Action:** Never use `outline: none` without providing a robust `:focus-visible` alternative. Always test floating UI elements against sticky bars (ads, cookie banners) on mobile viewports (e.g., 375px width).
