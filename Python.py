import requests
from bs4 import BeautifulSoup
import telegram
import asyncio

bot_token = '6739763498:AAGGDL_VOLHfyZB5jNaZVDge7KGQV4bE2CA'
bot_chat_id = '448325328'
bot = telegram.Bot(token=bot_token)

async def send_message_to_telegram_channel():
    url = 'https://www.fanabc.com/archives/category/tech'
    response = requests.get(url)
    s = BeautifulSoup(response.text, 'html.parser')
    post_url = s.find_all(class_='post-url')

    for i, post_link in enumerate(post_url):
        message = post_link['href']

        try:
            await bot.send_message(chat_id=bot_chat_id, text=message)
        except telegram.error.TelegramError as e:
            print(f"Failed to send message: {e}")
try:
    asyncio.run(send_message_to_telegram_channel())
except telegram.error.TelegramError as e:
    print(f"Failed to send message: {e}")