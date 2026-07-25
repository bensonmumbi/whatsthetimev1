## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-07-25 - Timezone Offset Cache and Lazy DOM Caching
**Learning:** Retrieving UTC offset values by instantiating multiple Date objects and formatting them to strings for subtraction is extremely expensive (~491ms for 10k lookups). Using the native `Intl.DateTimeFormat` with `{timeZoneName: 'longOffset'}` and caching lookups hourly in a Map reduces the lookup time to ~21ms (a massive ~22x speedup). Throttling DOM updates to minute changes for static details further eliminates high-frequency DOM manipulation.
**Action:** For repeat high-frequency lookups of slow-changing metadata like timezone offsets, implement hourly-keyed memoization. Cache references to DOM elements in high-frequency loops using `getEl` helpers.
