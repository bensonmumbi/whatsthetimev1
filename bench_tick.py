import subprocess
import time
import sys
from playwright.sync_api import sync_playwright

def run_benchmark():
    server_process = subprocess.Popen([sys.executable, "-m", "http.server", "8000"])
    time.sleep(2)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://localhost:8000/whatsthetime.html")

            # Benchmark script to run in-browser
            benchmark_js = """
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

            # Warm up
            page.evaluate(benchmark_js)

            # Run benchmark
            avg_time = page.evaluate(benchmark_js)
            return avg_time
    finally:
        server_process.terminate()

if __name__ == "__main__":
    avg = run_benchmark()
    print(f"Average tick() execution time: {avg:.6f} ms")
