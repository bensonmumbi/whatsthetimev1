## 2026-09-07 - Fast UTC Offset Lookup using longOffset and Hourly Caching
**Learning:** Formatting two dates to string representations and parsing them back into `Date` objects to compute UTC offsets is slow (~10x slower) and creates unnecessary garbage collection pressure. Using `Intl.DateTimeFormat` with `{ timeZoneName: 'longOffset' }` via `formatToParts()` retrieves the offset directly. Since UTC offsets for a given timezone rarely change within an hour, caching the result in a Map keyed by hour reduces execution time over 11x.
**Action:** Use `timeZoneName: 'longOffset'` and hourly key caching for UTC offset lookup instead of manual Date difference calculations.

## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).
