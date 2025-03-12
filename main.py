import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import config
import requests
# Твой Telegram Bot Token (замени на свой)

# Создаем бот и диспетчер
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

# Логирование (чтобы видеть ошибки, если что-то пойдет не так)
logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def start_command(message: types.Message):
    """Обработчик команды /start"""
    await message.answer("👋 Привет! Я бот. Я могу отправлять уведомления о новых ссылках.")

@dp.message(Command("help"))
async def help_command(message: types.Message):
    """Обработчик команды /help"""
    await message.answer("🔹 Доступные команды:\n/start — Запуск бота\n/help — Помощь")

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

async def main():
    """Функция запуска бота"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
