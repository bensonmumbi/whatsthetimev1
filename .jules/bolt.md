## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-21 - Throttling and DOM Caching in High-Frequency Loops
**Learning:** Throttling non-essential updates in a 1s clock loop (like date, timezone, and week number) and using lazy DOM element caching can reduce execution time by over 80%. This is often more impactful than micro-optimizing date formatting logic itself.
**Action:** Identify and throttle elements in `tick()` loops that don't require second-by-second updates. Use a `getEl` helper with a persistent cache object to avoid redundant `document.getElementById` calls.
