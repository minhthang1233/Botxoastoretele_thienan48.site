from telethon import TelegramClient
import os

# Lấy thông tin từ biến môi trường
API_ID = int(os.getenv("API_ID"))  # Lấy API_ID từ biến môi trường
API_HASH = os.getenv("API_HASH")   # Lấy API_HASH từ biến môi trường
BOT_TOKEN = os.getenv("BOT_TOKEN") # Lấy BOT_TOKEN từ biến môi trường

# Kiểm tra xem các biến môi trường có được thiết lập đúng không
if not API_ID or not API_HASH or not BOT_TOKEN:
    print("Please make sure API_ID, API_HASH, and BOT_TOKEN are set in the environment variables.")
    exit()

# Khởi tạo TelegramClient
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

async def get_chat_id():
    # Lấy danh sách các nhóm mà bot đã tham gia
    async for dialog in client.iter_dialogs():
        # In ra các nhóm và thông tin liên quan
        print(f"Group Name: {dialog.name}, Group ID: {dialog.id}")

# Chạy hàm để lấy ID nhóm
with client:
    client.loop.run_until_complete(get_chat_id())
