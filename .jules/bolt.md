## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-07-07 - Optimizing UTC Offsets with Intl.DateTimeFormat
**Learning:** Manual date arithmetic and string parsing for UTC offsets is significantly slower (~10x) than using `Intl.DateTimeFormat` with `timeZoneName: 'longOffset'`. Combining this with lazy DOM element caching provides a massive boost (~80% reduction) in high-frequency update loops like `tick()`.
**Action:** Use `Intl.DateTimeFormat`'s `longOffset` to retrieve timezone offsets directly. Pair with a global `Map` for formatter caching and a simple DOM reference cache to minimize main-thread overhead in every `setInterval` or `requestAnimationFrame` cycle.
