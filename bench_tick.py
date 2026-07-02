import subprocess
import time
import sys
import json
from playwright.sync_api import sync_playwright

def run_benchmark():
    server_process = subprocess.Popen([sys.executable, "-m", "http.server", "8000"])
    time.sleep(2)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://localhost:8000/whatsthetime.html")

            # Benchmark tick() function
            # We'll run it 1000 times and measure the time
            benchmark_js = """
            async () => {
                const start = performance.now();
                const iterations = 1000;
                for (let i = 0; i < iterations; i++) {
                    tick();
                }
                const end = performance.now();
                return (end - start) / iterations;
            }
            """
            avg_time = page.evaluate(benchmark_js)
            print(f"Average tick() execution time: {avg_time:.6f} ms")

            browser.close()
    finally:
        server_process.terminate()

if __name__ == "__main__":
    run_benchmark()
