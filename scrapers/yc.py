import requests
from bs4 import BeautifulSoup

def fetch_yc_jobs():

    all_jobs = []

    url = "https://www.ycombinator.com/jobs"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.find_all("a")

        for link in links:

            text = link.get_text(strip=True)
            href = link.get("href")

            if not href:
                continue

            if "engineer" in text.lower():

                if href.startswith("/"):

                    href = "https://www.ycombinator.com" + href

                all_jobs.append({
                    "company": "YC STARTUP",
                    "title": text,
                    "url": href
                })

        print("✅ YC Jobs Done")

    except Exception as e:
        print("❌ YC Error:", e)

    return all_jobs