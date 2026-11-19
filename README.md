# Job Aggregation & Notification Bot

An automated job discovery platform that aggregates entry-level Software Engineering opportunities from multiple sources, applies intelligent filtering and duplicate detection, and delivers real-time job alerts directly through Telegram.

🌐 Live Demo: https://t.me/jobforrishabh_bot

## Key Features

- Automated job aggregation from multiple platforms
- Intelligent filtering by role, company, and location
- Duplicate job detection and prevention
- Real-time Telegram notifications
- Scheduled execution every 4 hours
- Runs locally via Windows Task Scheduler (no paid hosting required)
- Automated workflows using GitHub Actions
- REST API and web scraping integration
- Personalized job discovery pipeline

## Tech Stack

Backend: Python

Automation: Windows Task Scheduler / GitHub Actions

Integration: Telegram Bot API

Data Collection: Web Scraping, REST APIs

Deployment: Local machine or GitHub Actions

## Workflow

Job Sources → Data Collection → Filtering Engine → Duplicate Detection → Telegram Notifications

## Run Locally (no hosting required)

1. Install dependencies: `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and fill in `TOKEN` and `CHAT_ID`
3. Run once manually to confirm: `python main.py`
4. Schedule it every 4 hours with Windows Task Scheduler:

```
schtasks /Create /TN "Job Bot" /TR "\"%CD%\run_bot.bat\"" /SC HOURLY /MO 4 /ST 00:00 /F
```

Output is appended to `logs\jobbot.log`. Remove the task with
`schtasks /Delete /TN "Job Bot" /F`.



#preview of the telegram notifications

<img width="1001" height="1275" alt="image" src="https://github.com/user-attachments/assets/5514205d-395f-4f07-95b5-bf5af1bccf57" />
