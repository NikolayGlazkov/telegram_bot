from create_bot import logger
from .base import connection
from .models import User, Note
from sqlalchemy import select
from typing import List, Dict, Any, Optional
from sqlalchemy.exc import SQLAlchemyError

@connection
async def set_user(session, tg_id, username: str, full_name: str) -> Optional[User]:
    try:
        user = await session.scalar(select(User).filter_by(id=tg_id))

        if not user:
            new_user = User(id=tg_id, username=username, full_name=full_name)
            session.add(new_user)
            await session.commit()
            logger.info(f"Зарегистрировал пользователя с ID {tg_id}!")
            return None
        else:
            logger.info(f"Пользователь с ID {tg_id} найден!")
            return user
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при добавлении пользователя: {e}")
        await session.rollback()


@connection
async def add_note(session, user_id: int, content_type: str, content_text: Optional[str] = None, file_id: Optional[str] = None) -> Optional[Note]:
    try:
        user = await session.scalar(select(User).filter_by(id=user_id))
        if not user:
            logger.error(f"Пользователь с ID {user_id} не найден.")
            return None
        
        new_note = Note(
            user_id = user_id,
            content_type = content_type,
            content_text = content_text,
            file_id = file_id)
        session.add(new_note)
        await session.commit()
        logger.info(f"Заметка для пользователя с ID {user_id} успешно добавлена!")
        return new_note
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при добавлении пользователя: {e}")
        await session.rollback()
        
@connection
async def get_note_by_id(session, note_id:int,) -> Optional[Dict[str,Any]]:
    try:
        note = await session.get(None,note_id)
        if not note:
            logger.error(f"Заметка с таким ID {note_id} не найдена.")
            return None
        
        return {
            'id':note.id,
            'content_type': note.content_type,
            'content_text': note.content_text,
            'file_id': note.file_id,
            
        }
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при добавлении пользователя: {e}")
        await session.rollback()
        
@connection
async def delete_note_by_id(session, note_id:int,) -> Optional[None]:
    try:
        note = await session.get(None,note_id)
        if not note:
            logger.error(f"Заметка с таким ID {note_id} не найдена.")
            return None
        
        await session.delete(note)
        await session.comet()
        logger.info(f"Заметка с id {note_id} успешно удалена")
        return note
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при добавлении пользователя: {e}")
        await session.rollback()
        
@connection
async def get_notes_by_user(session, user_id: int, date_add: str = None, text_search: str = None,
                           content_type: str = None)  -> List[Dict[str, Any]]:
    
    try:
        result = await session.execute(select(Note).filter_by(user_id=user_id))
        notes = result.scalar().all()
        
        if not notes:
            logger.error(f"Пользователь с таким ID {user_id} не найдена.")
            return []
        
        note_list = [
            {
            'id':note.id,
            'content_type': note.content_type,
            'content_text': note.content_text,
            'file_id': note.file_id,
            'date_created': note.created_at
            } for note in notes
        ]
    
        if date_add:
            
            notes_list = [note for note in note_list if note["date_created"].strftime('%Y-%m-%d') == date_add]
            
        if text_search:
            
            notes_list  = [note for note in note_list if text_search.lower() in (note['content_text'] or "").lower()]
            
        if content_type:
            notes_list  = [note for note in note_list if note['content_type'] == content_type]
            
        return note_list
    
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении заметок: {e}")
        await session.rollback()
        
