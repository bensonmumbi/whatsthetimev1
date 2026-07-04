import subprocess
import time
import sys
import json
from playwright.sync_api import sync_playwright

def run_benchmark():
    # Start local server
    server_process = subprocess.Popen([sys.executable, "-m", "http.server", "8000"])
    time.sleep(2)  # Wait for server to start

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://localhost:8000/whatsthetime.html")

            # Benchmark script
            benchmark_js = """
            async () => {
                const iterations = 1000;
                const warmup = 100;

                // Warmup
                for(let i=0; i<warmup; i++) tick();

                const start = performance.now();
                for(let i=0; i<iterations; i++) {
                    tick();
                }
                const end = performance.now();
                return (end - start) / iterations;
            }
            """

            avg_time = page.evaluate(benchmark_js)
            print(f"Average execution time of tick(): {avg_time:.6f} ms")

            browser.close()
    finally:
        server_process.terminate()

if __name__ == "__main__":
    run_benchmark()
