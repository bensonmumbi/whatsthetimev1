## 2026-05-15 - Caching Intl.DateTimeFormat and Throttling Updates
**Learning:** `Intl.DateTimeFormat` instantiation is expensive and can become a bottleneck when called multiple times per second in a `requestAnimationFrame` or `setInterval` loop. Throttling DOM updates for elements that don't need high-frequency refresh (like `HH:mm` displays) significantly reduces main-thread work.
**Action:** Always cache `Intl.DateTimeFormat` instances in a `Map` when performing repeated date formatting. Check if visual updates can be throttled based on the data's precision (e.g., only update on minute change if seconds aren't shown).

## 2026-05-21 - Optimizing High-Frequency Tick Loops with Lazy DOM Caching and Throttling
**Learning:** In a single-page application with a main clock loop running every second, repetitive `document.getElementById` calls and unnecessary DOM updates for static or slow-changing data (like Week Number or Date) create measurable overhead.
**Action:** Implement a lazy DOM element cache (`getEl` helper) and separate per-second updates from throttled (per-minute) updates within the `tick()` loop.
