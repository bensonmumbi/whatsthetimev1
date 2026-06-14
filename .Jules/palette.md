## 2025-05-15 - Timezone Converter Swap Button & Accessibility Baseline
**Learning:** Adding a "Swap" button between bidirectional inputs (like "From" and "To" selectors) significantly reduces user friction. Accessibility for icon-only buttons is a common oversight in fast-paced projects.
**Action:** Always check for bidirectional workflows that can benefit from a swap action. Ensure all `<button>` elements have either text content or an `aria-label`. Use `for` attributes on `<label>` to link with input `id`.

## 2026-06-14 - Global Focus Visibility & Semantic Button Migration
**Learning:** Using a global :focus-visible rule combined with a semantic button reset allows for a consistent keyboard navigation experience without compromising the visual aesthetic. Removing 'outline: none' from inputs is critical to prevent focus suppression.
**Action:** Always prefer <button type="button"> over <a> for actions that don't navigate to a new URL. Ensure a focus reset is applied to maintain the UI's design when switching to semantic buttons.
