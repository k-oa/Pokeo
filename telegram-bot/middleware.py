import os
from typing import  Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject

from bot import bot
from models.player import PlayerStatus
from services.players import get_player

LOG_CHAT_ID = os.getenv('LOG_CHAT_ID')

class MessageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        await bot.forward_message(LOG_CHAT_ID, event.chat.id, event.message_id)

        player_data = await get_player(event.from_user.id)
        if player_data.status == PlayerStatus.BANNED:
            return

        data["player"] = player_data
        return await handler(event, data)


class CallbackMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        # player_data = await get_player(event.from_user.id)
        # if player_data.status == PlayerStatus.BANNED:
        #     return
        
        # if event.data[-1] == '_': #якщо це індивідуальний колбек
        #     if str(event.from_user.id) in event.data:
        #         return await handler(event, data)

        #     await event.answer('You cant do dis🗣🗣🔥🔥💯🔥💯', True)
        #     return
        return await handler(event, data)