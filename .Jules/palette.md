## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-07-20 - Embedded Code Copy Button & Keyboard Focus Visibility
**Learning:** An absolutely positioned 'Copy' button overlay inside a readonly `<textarea>` makes sharing widgets extremely easy. To prevent the layout from breaking when users try to resize, the textarea must be styled with `resize: none`. Additionally, styling global `:focus-visible` ensures keyboard accessibility without affecting standard mouse focus outlines.
**Action:** Always apply `resize: none` to textareas containing absolutely positioned copy overlays, and use a global `*:focus-visible` rule to guarantee focus outline clarity for keyboard navigators.
