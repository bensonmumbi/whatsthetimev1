## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-05-23 - DOM Caching and Constant Hoisting in High-Frequency Loops
**Learning:** Repetitive `document.getElementById` calls and array allocations inside a 1s `setInterval` loop add unnecessary CPU overhead. Implementing a lazy DOM element cache and hoisting static arrays significantly improves execution efficiency.
**Action:** Use a global element cache object and a helper function for DOM lookups in high-frequency loops. Move static data structures (like day/month names) outside the loop to reduce GC pressure.
