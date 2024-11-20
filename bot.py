from telethon import TelegramClient, events

# Biến môi trường
API_ID = int("YOUR_API_ID")
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"
SOURCE_CHAT_ID = -1001234567890  # Thay bằng ID nhóm cần giám sát

# Kết nối bot
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def handler(event):
    # Kiểm tra xem tin nhắn có phải là tin nhắn chuyển tiếp không
    if event.message.forward:
        # Xóa tin nhắn nếu nó được chuyển tiếp
        await event.delete()
        print("Forwarded message deleted.")
    else:
        print("Message is not forwarded.")

print("Bot is running...")
client.run_until_disconnected()
