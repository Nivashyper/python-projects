import time, requests

def get_json(url, retries=3, backoff=1.5):
    for i in range(retries):
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            return r.json()
        except Exception:
            if i == retries - 1: raise
            time.sleep(backoff ** (i+1))

if __name__ == "__main__":
    data = get_json("https://api.github.com")
    print(data.get("current_user_url"))
