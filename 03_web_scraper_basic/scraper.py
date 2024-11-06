import requests
from bs4 import BeautifulSoup

def fetch_titles(url: str):
    html = requests.get(url, timeout=10).text
    soup = BeautifulSoup(html, "html.parser")
    return [h.get_text(strip=True) for h in soup.select("h1, h2, h3")]

if __name__ == "__main__":
    for t in fetch_titles("https://example.com"):
        print(t)
