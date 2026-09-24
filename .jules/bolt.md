## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-09-24 - Efficient UTC Offset Formatting via longOffset
**Learning:** Formatting date strings and instantiating double `Date` objects to calculate time offsets (e.g. `(new Date(localStr) - new Date(utcStr)) / 3600000`) incurs unnecessary string parsing overhead. Using `Intl.DateTimeFormat` with `{ timeZoneName: 'longOffset' }` and `formatToParts()` directly retrieves offset strings (like `GMT-04:00` / `UTC-04:00`) ~2x faster without string parsing or double `Date` allocation.
**Action:** Prefer `Intl.DateTimeFormat({ timeZoneName: 'longOffset' })` over manual date string arithmetic when displaying timezone offsets.
