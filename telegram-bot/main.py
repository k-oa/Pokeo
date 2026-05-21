import asyncio
from contextlib import suppress

from aiogram import Dispatcher

from middleware import MessageMiddleware, CallbackMiddleware
# from  handlers import new_player, inline, battle, info, box, chat, room, start
from routers import chat
from bot import bot
# from i18n import I18nMiddleware, i18n, _


def startup():
    print('start')


def shutdown():
    print('thats all')


async def main():
    dp = Dispatcher()
    # dp.update.middleware(I18nMiddleware(i18n))
    dp.message.middleware(MessageMiddleware())
    dp.callback_query.middleware(CallbackMiddleware())
    
    # dp.include_router(start.router)
    # dp.include_router(new_player.router)
    # dp.include_router(info.router)
    # dp.include_router(battle.router)
    # dp.include_router(box.router)
    # dp.include_router(room.router)
    dp.include_router(chat.router)
    # dp.include_router(inline.router)

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    try:
        await bot.delete_webhook(False)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
