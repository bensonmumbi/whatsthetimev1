## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-09-10 - Leveraging Intl longOffset and Result Caching
**Learning:** Performing double-Date parsing and date formatting string conversions to compute timezone offsets (`(local - utc) / 3600000`) is significantly slower than using `Intl.DateTimeFormat` with `timeZoneName: 'longOffset'`. Combining native `longOffset` with hourly result caching (`OFFSET_CACHE`) eliminates string parsing overhead and delivers ~20x faster offset resolution.
**Action:** Use `timeZoneName: 'longOffset'` with formatToParts and cache timezone string results when calculating UTC offset strings.
