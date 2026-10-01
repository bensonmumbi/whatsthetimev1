## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-10-01 - Extracting UTC Offset via Intl.DateTimeFormat longOffset
**Learning:** Calculating UTC offsets by formatting date strings for UTC and target timezones then parsing them back into `Date` objects creates heavy object instantiation and parsing overhead. Using `Intl.DateTimeFormat` with `timeZoneName: 'longOffset'` provides offset strings directly (~1.2x - 3.5x faster).
**Action:** Use `getFormatter({timeZone: tz, timeZoneName: 'longOffset'}).formatToParts(d)` to extract timezone offset strings directly instead of parsing formatted date strings.
