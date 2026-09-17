## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-09-17 - Direct Long-Offset Formatting vs Double-Date Parsing
**Learning:** Formatting Date objects to string representations and then parsing them back via `new Date(getFormatter(...).format(d))` to calculate timezone offsets is highly inefficient (~30x slower than direct formatting) and creates unnecessary GC pressure. `Intl.DateTimeFormat` with `timeZoneName: 'longOffset'` returns the offset string directly in `formatToParts()`, and caching computed offsets by hour (`${tz}_${Math.floor(time / 3600000)}`) reduces lookup cost to $O(1)$.
**Action:** Avoid date string parsing math for timezone offset calculations; leverage `longOffset` with `formatToParts()` and cache hourly offset strings.
