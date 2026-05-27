import requests

companies = [
    "netflix",
    "uber",
    "postman",
]

def fetch_lever_jobs():

    all_jobs = []

    for company in companies:

        url = f"https://api.lever.co/v0/postings/{company}?mode=json"

        try:

            response = requests.get(url)

            if response.status_code != 200:
                print(f"❌ Lever Failed: {company}")
                continue

            data = response.json()

            print(f"✅ Lever: {company}")

            for job in data:

                all_jobs.append({
                    "company": company.upper(),
                    "title": job["text"],
                    "url": job["hostedUrl"]
                })

        except Exception as e:
            print(f"❌ Lever Error ({company}):", e)

    return all_jobs