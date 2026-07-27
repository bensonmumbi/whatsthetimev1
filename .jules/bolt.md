## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-07-27 - Hourly Timezone Offset Caching with longOffset
**Learning:** Formatting and parsing full date strings twice (once for UTC and once for the target timezone) to calculate offsets inside high-frequency clocks is extremely expensive. Leveraging `Intl.DateTimeFormat` with `{timeZoneName: 'longOffset'}` and caching computed offset strings using hourly cache keys (`timezone + '_' + Math.floor(time / 3600000)`) speeds up offset computation by over 25x while remaining safely DST-aware.
**Action:** Use memoized hourly timezone offsets when displaying offsets in live clocks or high-frequency loops.
