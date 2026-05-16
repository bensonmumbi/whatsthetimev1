## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-05-16 - DOM Caching and Extensive Throttling in Clock Loops
**Learning:** Even with cached formatters, repeated DOM lookups (`document.getElementById`, `querySelectorAll`) and redundant calculations for static-within-the-minute data (like UTC offsets or week numbers) in a 1-second loop waste CPU cycles.
**Action:** Cache all DOM element references once. Move all non-second-sensitive UI updates into throttled blocks (minutely or daily). Use `document.hidden` to pause updates entirely when the page is not visible.
