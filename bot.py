from telethon import TelegramClient, events
import os

# Lấy thông tin từ biến môi trường
API_ID = int(os.getenv("API_ID", "your_api_id"))  # Thay "your_api_id" bằng API ID của bạn
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Thay "your_api_hash" bằng API Hash của bạn
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")  # Thay "your_bot_token" bằng Token của Bot

# Khởi tạo bot
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage)
async def handler(event):
    try:
        # Kiểm tra nếu tin nhắn là tin nhắn được chuyển tiếp
        if event.message.forward:
            forward_info = event.message.forward

            # Ghi log chi tiết tin nhắn để kiểm tra
            print("Forward info:", forward_info.to_dict())

            # Kiểm tra xem tin nhắn chuyển tiếp có phải từ "Stories" hay không
            if forward_info.sender_name == "Stories":
                await event.delete()  # Xóa tin nhắn
                print(f"Deleted forwarded story: {event.message.id}")
            else:
                print("Not a forwarded story.")
        else:
            print("Message is not forwarded.")
    except Exception as e:
        print(f"Error: {e}")

print("Bot is running...")
bot.run_until_disconnected()
