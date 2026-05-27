from telegram import Bot

TOKEN = "8930002595:AAFiEl_jeWdSa1wApSIjEdkClLJLDEuXlFo"
CHAT_ID = "1849480383"

bot = Bot(token=TOKEN)

async def send_telegram_message(message):

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )