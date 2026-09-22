## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-09-22 - Direct longOffset Formatting & Offset Caching
**Learning:** Formatting date strings twice and re-parsing them via `new Date()` to compute UTC timezone offsets is extremely inefficient (~1ms per call batch). Leveraging `timeZoneName: 'longOffset'` with `Intl.DateTimeFormat` and caching offsets hourly per timezone yields a ~13x speedup.
**Action:** Use native `timeZoneName: 'longOffset'` in `Intl.DateTimeFormat` to retrieve timezone offset strings directly instead of manual Date arithmetic.
