## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-09-16 - Fast UTC Offsets with longOffset and Hourly Caching
**Learning:** Formatting date strings for target and UTC timezones and parsing them back into `Date` objects to compute UTC offsets is ~20x slower than using `Intl.DateTimeFormat` with `timeZoneName: 'longOffset'`. Combined with hourly offset caching (`tz_hour`), offset lookups run almost instantly without GC overhead.
**Action:** Use `Intl.DateTimeFormat` with `longOffset` to retrieve GMT/UTC offsets directly, and cache results by hour to eliminate redundant formatting calls.
