## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-05-26 - Optimized tick() with DOM Caching and Throttling
**Learning:** Combining lazy DOM element caching with throttling non-critical updates in a high-frequency loop (1s) can reduce function execution time by over 80%. Specifically, moving date and detail updates to a minute-precision check avoids hundreds of unnecessary DOM writes per minute.
**Action:** Implement lazy caching (ELS object) and throttle any non-second precision UI updates within a tick loop.
