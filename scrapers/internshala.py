import requests
from bs4 import BeautifulSoup

def fetch_internshala_jobs():

    all_jobs = []

    url = "https://internshala.com/jobs/software-development-jobs/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:

        response = requests.get(url, headers=headers, timeout=30)

        soup = BeautifulSoup(response.text, "html.parser")

        jobs = soup.find_all("div", class_="individual_internship")

        for job in jobs:

            title_tag = job.find(class_="job-internship-name")

            if not title_tag:
                continue

            title = title_tag.get_text(strip=True)

            link_tag = job.find("a", class_="job-title-href")

            if not link_tag:
                continue

            href = link_tag.get("href")

            if not href:
                continue

            full_url = "https://internshala.com" + href

            company_tag = job.find(class_="company-name")
            company = company_tag.get_text(strip=True) if company_tag else "INTERNSHALA"

            location_tag = job.find(class_="locations")
            location = location_tag.get_text(" ", strip=True) if location_tag else ""

            all_jobs.append({
                "company": company.upper(),
                "title": title,
                "url": full_url,
                "location": location
            })

        print(f"✅ Internshala Done ({len(all_jobs)} jobs)")

    except Exception as e:
        print("❌ Internshala Error:", e)

    return all_jobs
