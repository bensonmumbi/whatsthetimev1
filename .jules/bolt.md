## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-09-28 - Fast Timezone Offsets with longOffset and Throttling Non-Second Elements
**Learning:** Using `Intl.DateTimeFormat` with `timeZoneName: 'longOffset'` extracts timezone offset strings (e.g., `GMT-05:00`) directly, avoiding the need to construct intermediate `Date` instances or parse formatted date strings. Additionally, moving non-second DOM elements (`datDisp`, `tzName`, `utcOff`, `weekNum`, `doy`, `qtr`) inside a minute-throttled block (`n.getMinutes() !== lastMin`) cuts `tick()` execution time by over 8x.
**Action:** Use `timeZoneName: 'longOffset'` with cached formatters for UTC offset strings instead of string date parsing, and move non-second clock DOM updates into minute-throttled blocks.
