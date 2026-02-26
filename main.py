import os
import asyncio
from telethon import TelegramClient, events

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
CHAT_ID = int(os.getenv("CHAT_ID"))

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=CHAT_ID))
async def handler(event):
    text = event.raw_text
    print("Получено сообщение:", text)

    await asyncio.sleep(1)

    await client.send_message(CHAT_ID, text)
    print("Отправлено повторно")

client.start()
client.run_until_disconnected()
