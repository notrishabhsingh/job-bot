import requests
from bs4 import BeautifulSoup

def fetch_internshala_jobs():

    all_jobs = []

    url = "https://internshala.com/jobs/software-development-jobs/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        jobs = soup.find_all("div", class_="individual_internship")

        for job in jobs:

            title_tag = job.find("h3")

            if not title_tag:
                continue

            title = title_tag.text.strip()

            link_tag = job.find("a")

            if not link_tag:
                continue

            href = link_tag.get("href")

            full_url = "https://internshala.com" + href

            all_jobs.append({
                "company": "INTERNSHALA",
                "title": title,
                "url": full_url
            })

        print("✅ Internshala Done")

    except Exception as e:
        print("❌ Internshala Error:", e)

    return all_jobs