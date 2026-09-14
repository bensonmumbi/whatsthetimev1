## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-09-14 - Timezone Offset Extraction via longOffset vs Date Parsing
**Learning:** Calculating UTC offset by formatting two Date strings (`UTC` and target timezone) and re-parsing them back into `Date` objects (`new Date(...)`) adds significant CPU overhead (~15x-20x slower). Native `Intl.DateTimeFormat` with `timeZoneName: 'longOffset'` directly provides timezone offset strings like `GMT-05:00` or `GMT+05:30` via `formatToParts()`.
**Action:** Use `timeZoneName: 'longOffset'` on cached `Intl.DateTimeFormat` instances and cache the result by hourly keys to retrieve UTC offset strings with minimal CPU overhead.
