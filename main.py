from telethon import TelegramClient, events, sync
import asyncio
import time
import os
# Ваши данные
from dotenv import load_dotenv
load_dotenv()
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_username = '@anicardplaybot'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

async def send_messages():
    while True:  # Бесконечный цикл
        try:
            await client.send_message(bot_username, '🏵️ Получить карту')
            await asyncio.sleep(1200)
            await client.send_message(bot_username, '⚔️ Получить карту')
        except Exception as e:
            print(f"Ошибка: {e}")
            os.Exit(1)

async def main():
    await send_messages()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
