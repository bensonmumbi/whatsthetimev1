## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-05-25 - DOM Caching and Constant Hoisting in High-Frequency Loops
**Learning:** In a 1Hz `tick()` loop, `document.getElementById` and array re-allocations (`D = [...]`, `M = [...]`) add significant overhead. Lazy DOM caching via a global object and hoisting static constants reduced `tick()` execution time by over 90% when combined with throttling.
**Action:** Use a `getEl(id)` helper with a central `ELS` cache for all high-frequency DOM access. Move static strings and arrays out of loop scopes to the global level.
