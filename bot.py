from aiogram import Dispatcher, types, Bot
from aiogram import F
from aiogram.filters.command import Command
from aiogram.types.callback_query import CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
import random 
import config
import asyncio
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest

dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message) -> None:
    kb = [
        [types.InlineKeyboardButton(text="каталог", callback_data='kurs_list')],

        [
            types.InlineKeyboardButton(text="профиль", callback_data='name'),
            types.InlineKeyboardButton(text="тех. поддержка", callback_data='portfolio')
        ],
        [types.InlineKeyboardButton(text="о нас", callback_data='about_as')]
    ]
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=kb, input_field_placeholder="Choose your destiny")
    if isinstance(message, types.CallbackQuery):
        await message.message.edit_text("Hello my friend", reply_markup=keyboard)
    else:
        await message.answer("Hello my friend", reply_markup=keyboard)


@dp.callback_query(F.data == "kurs_list")
async def kurs_list(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(text = 'курс python',callback_data="python_curs"),types.InlineKeyboardButton(text = 'курс django',callback_data='django_curs')],
        [types.InlineKeyboardButton(text = 'курс c#',callback_data="c_curs"),types.InlineKeyboardButton(text = 'курс C++',callback_data='c_plus_curs')],
        [types.InlineKeyboardButton(text = 'на главную страницу',callback_data="start")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text('выберите список курсов', reply_markup=keyboard)

@dp.callback_query(F.data == "start")
async def start_command(callback: types.CallbackQuery) -> None:
    kb = [
        [types.InlineKeyboardButton(text="каталог", callback_data='kurs_list')],

        [
            types.InlineKeyboardButton(text="профиль", callback_data='name'),
            types.InlineKeyboardButton(text="тех. поддержка", callback_data='portfolio')
        ],
        [types.InlineKeyboardButton(text="о нас", callback_data='about_as')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text('выберите список курсов', reply_markup=keyboard)

async def main():
    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)
    
if __name__== '__main__':
    asyncio.run(main())