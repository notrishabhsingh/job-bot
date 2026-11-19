import os
from telegram import Bot

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not TOKEN or not CHAT_ID:
    raise SystemExit(
        "Missing credentials: set TOKEN and CHAT_ID in a .env file next to main.py "
        "(see .env.example) or as environment variables."
    )

bot = Bot(token=TOKEN)

async def send_telegram_message(message):

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )
