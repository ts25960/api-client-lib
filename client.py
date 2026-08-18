import requests, time

def get(url, retries=3):
    for i in range(retries):
        try:
            return requests.get(url, timeout=10)
        except Exception:
            time.sleep(i + 1)
