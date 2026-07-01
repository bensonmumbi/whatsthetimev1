## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-07-01 - Optimizing High-Frequency Clock Loops
**Learning:** In a 1Hz clock loop, `document.getElementById` and redundant `new Date()` allocations add up. Using `Intl.DateTimeFormat` with `timeZoneName: 'longOffset'` combined with regex is faster and more accurate for UTC offsets than manual string manipulation of date components.
**Action:** Implement lazy DOM caching (`getEl`), hoist static arrays (days/months), and pass the `Date` object through throttled updates to minimize GC pressure and main-thread execution time.
