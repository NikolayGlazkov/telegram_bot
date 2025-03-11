import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import config
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

async def main():
    """Функция запуска бота"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
