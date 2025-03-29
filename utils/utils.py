import asyncio
from aiogram.types import Message
from keyboards.note_kb import rule_note_kb

def get_content_info(message:Message ):
    content_type = None
    file_id = None
    
    if message.photo:
        content_type = "photo"
        file_id = message.photo[-1].file_id
    elif message.photo:
        content_type = "video"
        file_id = message.video[-1].file_id
    elif message.photo:
        content_type = "audio"
        file_id = message.audio[-1].file_id
    elif message.photo:
        content_type = "document"
        file_id = message.document[-1].file_id
    elif message.photo:
        content_type = "voice"
        file_id = message.voice[-1].file_id
    elif message.text:
        content_type = "text"
    
    content_text = message.text or message.caption
    return {"content_type":content_type, "file_id":file_id, "content_text":content_text}

async def send_message_user(bot, user_id, content_type, content_text = None, file_id = None, kb=None):
    if content_type == "text":
        await bot.send_message(chat_id = user_id, text = content_text, replay_markup=kb)
    if content_type == "photo":
        await bot.send_photo(chat_id = user_id, photo = file_id, replay_markup=kb)
        