import asyncio

from aiogram.utils.executor import start_webhook
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from bot_app import dp, bot
from database import sqlite_db
from config import *
import handlers
from aiogram import Bot, Dispatcher, executor, types
from database.sqlite_db import show_expressions, get_questions1, get_questions2, get_questions3
from states import TestState


from services.set_commands import set_default_commands
from services.remove_extra_inline import remove_inline_markup
from services.throttling_middleware import ThrottlingMiddleware

import logging
from logging import handlers as logging_handlers


class StatMiddleware(BaseMiddleware):

    def __init__(self):
        super(StatMiddleware, self).__init__()
        self.counter = 0

    async def on_process_update(self, update: types.Update, data: dict):
        if not update.message or update.message.chat.type == types.chat.ChatType.PRIVATE:
            await remove_inline_markup(bot, update.message)

    async def on_process_message(self, message: types.Message, data: dict):
        dispatcher = Dispatcher.get_current()
        if dispatcher.current_state() == TestState:
            import random
            await asyncio.sleep(random.randint(3, 6))
            one = await get_questions1()[:3]
            two = await get_questions2()[:3]
            three = await get_questions3()[:3]
            await message.answer(''.join(one) + ''.join(two) + ''.join(three))


dp.middleware.setup(ThrottlingMiddleware())
dp.middleware.setup(StatMiddleware())


async def main():
    print("Starting bot")

    # logger = logging.getLogger('aiogram')
    # logger.setLevel(logging.INFO)
    #
    # handler = logging_handlers.TimedRotatingFileHandler(filename='logs/aiogram.log', when='d', interval=1)
    # handler.setLevel(logging.INFO)
    #
    # formatter = logging.Formatter('%(levelname)s %(asctime)s %(message)s')
    # handler.setFormatter(formatter)
    #
    # logger.addHandler(handler)

    try:
        await set_default_commands(bot)
        sqlite_db.sql_start()
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped!")
