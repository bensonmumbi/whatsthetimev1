## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-10-03 - Extracting UTC Offset via longOffset Format Parts
**Learning:** Computing UTC offsets by formatting UTC vs target timezone strings and parsing double `Date` objects is ~25-30% slower than using `Intl.DateTimeFormat` with `{ timeZoneName: 'longOffset' }` and `formatToParts()`.
**Action:** Use `formatToParts()` with `longOffset` to extract timezone offsets directly without intermediate Date parsing or string arithmetic.
