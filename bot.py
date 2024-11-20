from telethon import TelegramClient, events
import os

# Nhập các thông tin từ môi trường
API_ID = int(os.getenv("API_ID", "your_api_id"))  # Thay bằng API ID của bạn
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Thay bằng API Hash của bạn
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")  # Thay bằng Token Bot của bạn

# Khởi tạo bot
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage)
async def handler(event):
    # Kiểm tra nếu tin nhắn là câu chuyện được chuyển tiếp
    if event.message.forward and event.message.forward.sender_name == "Stories":
        try:
            # Xóa tin nhắn
            await event.delete()
            print(f"Deleted forwarded story: {event.message.id}")
        except Exception as e:
            print(f"Error deleting message: {e}")

print("Bot is running...")
bot.run_until_disconnected()
