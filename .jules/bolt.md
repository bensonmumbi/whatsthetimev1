## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-04 - Extreme Optimization of Clock Loop
**Learning:** Combining lazy DOM caching with minute-based throttling for non-second data reduces the `tick()` loop execution time by over 90%. Passing the same `Date` object to all sub-calculations further reduces garbage collection pressure.
**Action:** For high-frequency (1s) UI loops, strictly separate second-precision updates from minute-precision updates and use a centralized element cache to avoid repeated `document.getElementById` calls.
