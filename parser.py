import asyncio
import requests
from config import BOT_TOKEN, CHAT_ID, CHECK_INTERVAL

async def send_telegram_message(message):
    """Отправка строки в Telegram-канал"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print(f"✅ Сообщение отправлено: {message}")
        else:
            print(f"❌ Ошибка Telegram: {response.text}")
    except Exception as e:
        print(f"❌ Ошибка при отправке: {e}")

async def send_message_loop():
    """Отправляет сообщение в Telegram раз в 60 секунд"""
    while True:
        await send_telegram_message("🔔 Это тестовое сообщение!")  # Тут можно поменять текст
        await asyncio.sleep(CHECK_INTERVAL)  # Ожидание перед следующей отправкой

if __name__ == "__main__":
    asyncio.run(send_message_loop())
