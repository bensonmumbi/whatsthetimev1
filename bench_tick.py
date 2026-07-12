import subprocess
import time
import sys
import json
from playwright.sync_api import sync_playwright

def run_benchmark():
    # Start local server
    server_process = subprocess.Popen([sys.executable, "-m", "http.server", "8001"])
    time.sleep(2)  # Wait for server to start

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://localhost:8001/whatsthetime.html")

            # Benchmark the tick function
            benchmark_script = """
            () => {
                const iterations = 1000;
                const start = performance.now();
                for (let i = 0; i < iterations; i++) {
                    tick();
                }
                const end = performance.now();
                return (end - start) / iterations;
            }
            """

            # Warmup
            page.evaluate("for(let i=0; i<100; i++) tick();")

            avg_time = page.evaluate(benchmark_script)
            print(f"Average tick() execution time: {avg_time:.6f} ms")

            browser.close()
            return avg_time
    finally:
        server_process.terminate()

if __name__ == "__main__":
    run_benchmark()
