import time
import subprocess
import sys
from playwright.sync_api import sync_playwright

def run_benchmark():
    # Start local server
    server_process = subprocess.Popen([sys.executable, "-m", "http.server", "8000"])
    time.sleep(2)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://localhost:8000/whatsthetime.html")

            # Inject benchmarking code
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
            avg_time = page.evaluate(benchmark_script)
            print(f"Average tick() execution time: {avg_time:.6f} ms")

            browser.close()
    finally:
        server_process.terminate()

if __name__ == "__main__":
    run_benchmark()
