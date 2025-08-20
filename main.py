from telethon import TelegramClient, events
import os

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
SESSION = os.environ.get("SESSION", "")

# Buat client dari string session
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(pattern="^.alive"))
async def alive(event):
    await event.reply("⚡ Bot is alive and running on Heroku!")

print("Starting Userbot...")
client.start()
client.run_until_disconnected()
