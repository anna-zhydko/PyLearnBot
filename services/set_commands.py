from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
from config import *


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('/start', COMMAND_START),
            BotCommand('/help', COMMAND_HELP),
            BotCommand('/content', COMMAND_CONTENT),
            BotCommand('/author', COMMAND_AUTHOR),
        ],
        scope=BotCommandScopeDefault()
    )
