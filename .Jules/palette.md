## 2026-05-15 - Accessibility and Interactive Micro-UX Improvements
**Learning:** Adding ARIA labels to icon-only buttons and ensuring proper label-input associations significantly improves the experience for screen reader users without altering the visual design. Visual feedback for "copy to clipboard" actions (like changing button text to "Copied!") provides immediate reassurance to users that the action was successful.
**Action:** Always check for icon-only buttons and missing `for` attributes on labels. Implement visual feedback for all clipboard or async actions to confirm success.
