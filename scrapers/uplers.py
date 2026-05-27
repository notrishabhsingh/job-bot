import requests
from bs4 import BeautifulSoup

def fetch_uplers_jobs():

    all_jobs = []

    url = "https://www.uplers.com/jobs/"

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

                all_jobs.append({
                    "company": "UPLERS",
                    "title": text,
                    "url": href
                })

        print("✅ Uplers Done")

    except Exception as e:
        print("❌ Uplers Error:", e)

    return all_jobs