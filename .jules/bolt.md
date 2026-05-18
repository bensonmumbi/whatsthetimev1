## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-05-18 - DOM Caching and Visibility Throttling
**Learning:** Frequent `document.getElementById` calls in a 1Hz loop add unnecessary main-thread overhead. Additionally, continuing DOM updates when the page is not visible wastes CPU and battery.
**Action:** Cache DOM elements in a persistent object for high-frequency loops. Use `document.hidden` to early-return from update functions when the tab is inactive.
