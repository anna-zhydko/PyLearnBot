import asyncio

from aiogram.utils.executor import start_webhook
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from bot_app import dp, bot
from config import *
import handlers


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
