## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-06-14 - Lazy DOM Caching and Constant Hoisting in Loops
**Learning:** In high-frequency loops (like a 1s clock tick), `document.getElementById` and array literal re-allocation add measurable overhead. A lazy-loading cache object for DOM elements and hoisting static arrays (like days/months) out of the loop can improve execution time by over 80%.
**Action:** Use a `getEl` helper with a local `ELS` cache for elements updated in intervals. Move all static configuration and labels to the outer scope.
