## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-05-25 - [Accessible Buttons and Page-Aware Navigation]
**Learning:** Using semantic `<button>` instead of `<div>` for selection grids ensures keyboard accessibility without styling regressions when combined with proper CSS resets. Dynamic page-aware navigation functions (like `scrollTo2`) improve robustness and eliminate hardcoded page-switching logic flaws in SPAs.
**Action:** Always prefer `<button>` for clickable grid items and ensure internal link helpers dynamically detect and switch to target page containers.
