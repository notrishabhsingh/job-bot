import requests
from bs4 import BeautifulSoup

def fetch_wellfound_jobs():

    all_jobs = []

    url = "https://wellfound.com/jobs"

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

                    href = "https://wellfound.com" + href

                all_jobs.append({
                    "company": "WELLFOUND",
                    "title": text,
                    "url": href
                })

        print("✅ Wellfound Done")

    except Exception as e:
        print("❌ Wellfound Error:", e)

    return all_jobs