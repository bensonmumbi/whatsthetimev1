import subprocess
import time
import sys
import json
from playwright.sync_api import sync_playwright

def run_benchmark():
    server_process = subprocess.Popen([sys.executable, "-m", "http.server", "8001"])
    time.sleep(2)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://localhost:8001/whatsthetime.html")

            # Benchmark tick()
            metrics = page.evaluate("""
                () => {
                    const iterations = 1000;
                    // Warmup
                    for(let i=0; i<100; i++) tick();

                    const start = performance.now();
                    for(let i=0; i<iterations; i++) {
                        tick();
                    }
                    const end = performance.now();
                    return {
                        iterations,
                        totalMs: end - start,
                        avgMs: (end - start) / iterations
                    };
                }
            """)
            print(json.dumps(metrics, indent=2))
            browser.close()
    finally:
        server_process.terminate()

if __name__ == "__main__":
    run_benchmark()
