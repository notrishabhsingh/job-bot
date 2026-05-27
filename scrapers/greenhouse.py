import requests

companies = [
    "airbnb",
    "databricks",
    "scaleai",
    "figma",
    "robinhood",
    "discord",
    "stripe",
]

def fetch_greenhouse_jobs():

    all_jobs = []

    for company in companies:

        url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

        try:

            response = requests.get(url)

            if response.status_code != 200:
                print(f"❌ Failed: {company}")
                continue

            data = response.json()

            print(f"✅ Greenhouse: {company}")

            for job in data["jobs"]:

                all_jobs.append({
                    "company": company.upper(),
                    "title": job["title"],
                    "url": job["absolute_url"]
                })

        except Exception as e:
            print(f"❌ Greenhouse Error ({company}):", e)

    return all_jobs