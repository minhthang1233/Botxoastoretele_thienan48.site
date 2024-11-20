import os
from telethon import TelegramClient, events

# Lấy thông tin từ biến môi trường
API_ID = int(os.getenv("API_ID"))  # Lấy API_ID từ biến môi trường
API_HASH = os.getenv("API_HASH")   # Lấy API_HASH từ biến môi trường
BOT_TOKEN = os.getenv("BOT_TOKEN") # Lấy BOT_TOKEN từ biến môi trường

# Kiểm tra xem các biến môi trường có được thiết lập đúng không
if not API_ID or not API_HASH or not BOT_TOKEN:
    print("Please make sure API_ID, API_HASH, and BOT_TOKEN are set in the environment variables.")
    exit()

# Kết nối bot
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Link nhóm bạn muốn giám sát (username của nhóm)
SOURCE_CHAT_LINK = "nhom1573248"  # Thay bằng username của nhóm (không có https://t.me/)

@client.on(events.NewMessage)
async def handler(event):
    # Lấy thông tin nhóm từ username (link nhóm)
    try:
        chat = await client.get_entity(SOURCE_CHAT_LINK)
        print(f"Monitoring group ID: {chat.id}")  # In ra ID nhóm
    except Exception as e:
        print(f"Error fetching group: {e}")
        return

    # In ra tên nhóm nhận được từ sự kiện
    print(f"Received message in group: {event.chat.username if event.chat else 'Unknown Group'}")
    
    # Kiểm tra xem tin nhắn có thuộc nhóm bạn muốn giám sát không
    if event.chat.id == chat.id:
        print(f"Message belongs to the monitored group: {SOURCE_CHAT_LINK}")

        # Kiểm tra xem tin nhắn có phải là tin nhắn chuyển tiếp không
        if event.message.forward:
            # Xóa tin nhắn nếu nó được chuyển tiếp
            await event.delete()
            print("Forwarded message deleted.")
        else:
            print("Message is not forwarded.")
    else:
        print(f"Message is not from the monitored group. Message from: {event.chat.id}")

print("Bot is running...")
client.run_until_disconnected()
