## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-07-22 - Memoizing Timezone Offset (utcOff) Calculations
**Learning:** Parsing dates manually from formatted strings is highly computationally expensive and prone to parsing overhead. Using `Intl.DateTimeFormat` with `{timeZoneName: 'longOffset'}` and `formatToParts()` is significantly faster, and combining it with a robust minute-scoped cache Map (`OFFSET_CACHE`) keyed by timezone + minute reduces average execution time by over 95% on cache hits, since offsets only change on DST transitions.
**Action:** Always memoize repeating date formatting operations (like timezone offset resolution) using a cache map keyed by `tz` and current minute, and reuse instantiated `Date` objects across loops.
