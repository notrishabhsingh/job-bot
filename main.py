import json
import asyncio
import random

from filters import *
from telegram_bot import send_telegram_message


from scrapers.greenhouse import fetch_greenhouse_jobs
from scrapers.lever import fetch_lever_jobs
from scrapers.yc import fetch_yc_jobs
from scrapers.wellfound import fetch_wellfound_jobs
from scrapers.internshala import fetch_internshala_jobs
from scrapers.uplers import fetch_uplers_jobs


try:
    with open("seen_jobs.json", "r") as f:
        seen_jobs = json.load(f)
except:
    seen_jobs = []


def is_good_job(title):

    title = title.lower()

    if any(bad in title for bad in BAD_KEYWORDS):
        return False
    if any(good in title for good in GOOD_KEYWORDS):
        return True

    return False


def is_good_location(location):

    if not location:
        return True

    location = location.lower()

    if any(keyword in location for keyword in LOCATION_KEYWORDS):
        return True

    return False


async def main():

    jobs = []

    print("\n🚀 Fetching jobs from all sources...\n")


    try:
        jobs.extend(fetch_greenhouse_jobs())
        print("✅ Greenhouse Done")
    except Exception as e:
        print("❌ Greenhouse Error:", e)

    try:
        jobs.extend(fetch_lever_jobs())
        print("✅ Lever Done")
    except Exception as e:
        print("❌ Lever Error:", e)

    try:
        jobs.extend(fetch_yc_jobs())
        print("✅ YC Done")
    except Exception as e:
        print("❌ YC Error:", e)

    try:
        jobs.extend(fetch_wellfound_jobs())
        print("✅ Wellfound Done")
    except Exception as e:
        print("❌ Wellfound Error:", e)

    try:
        jobs.extend(fetch_internshala_jobs())
        print("✅ Internshala Done")
    except Exception as e:
        print("❌ Internshala Error:", e)

    try:
        jobs.extend(fetch_uplers_jobs())
        print("✅ Uplers Done")
    except Exception as e:
        print("❌ Uplers Error:", e)

    print(f"\n📦 Total Raw Jobs Found: {len(jobs)}")

    filtered_jobs = []

    for job in jobs:

        title = job.get("title", "")
        job_url = job.get("url", "")
        location = job.get("location", "")

        if not is_good_job(title):
            continue

        if not is_good_location(location):
            continue
        if job_url in seen_jobs:
            continue

        filtered_jobs.append(job)

    print(f"✅ Filtered Jobs: {len(filtered_jobs)}")


    top_jobs = []
    other_jobs = []

    for job in filtered_jobs:

        company = job["company"].upper()

        if company in TOP_COMPANIES:
            top_jobs.append(job)
        else:
            other_jobs.append(job)

    random.shuffle(top_jobs)
    random.shuffle(other_jobs)

    MAX_TOP_JOBS = 10
    MAX_OTHER_JOBS = 25

    top_jobs = top_jobs[:MAX_TOP_JOBS]
    other_jobs = other_jobs[:MAX_OTHER_JOBS]

    final_jobs = top_jobs + other_jobs

    random.shuffle(final_jobs)

    notifications_sent = 0

    for job in final_jobs:

        message = f"""
🚀 NEW SWE JOB

🏢 Company: {job['company']}
💼 Role: {job['title']}
📍 Location: {job.get('location', 'Not Mentioned')}

🔗 Apply Here:
{job['url']}
"""

        print(message)

        try:

            await send_telegram_message(message)

            # Prevent Telegram rate limit
            await asyncio.sleep(2)

        except Exception as e:
            print("Telegram Error:", e)

        seen_jobs.append(job["url"])

        notifications_sent += 1


    with open("seen_jobs.json", "w") as f:
        json.dump(seen_jobs, f, indent=4)


    print("\n==========================")
    print("✅ JOB SCAN COMPLETE")
    print("==========================")

    print(f"📦 Raw Jobs Found: {len(jobs)}")
    print(f"✅ Filtered Jobs: {len(filtered_jobs)}")
    print(f"🔥 Notifications Sent: {notifications_sent}")
    print(f"🏆 Top Company Jobs: {len(top_jobs)}")
    print(f"🚀 Other Jobs: {len(other_jobs)}")



asyncio.run(main())