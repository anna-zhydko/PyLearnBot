from aiogram import types
from aiogram.utils.markdown import bold
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import ChatTypeFilter

from bot_app import dp, bot
from config import *
from keyboards.main_menu import main_menu_keyboard as main_kb
from keyboards.content_inline import content_inline_keyboard as content_kb
from bot_app import dp, bot


@dp.message_handler(commands=['start'], state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(MESSAGE_GREETINGS_PRIVATE, reply_markup=main_kb.main_keyboard)


@dp.message_handler(commands=['help'], state='*')
async def send_help(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(MESSAGE_GREETINGS_PRIVATE)


# Content
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), commands=['content'], state='*')
@dp.message_handler(Text(equals=KEY_BUTTON_CONTENT), state='*')
async def exchange(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(CONTENT_LIST, reply_markup=content_kb.content_menu_keyboard)


# Author
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), commands=['author'], state='*')
@dp.message_handler(Text(equals=KEY_BUTTON_AUTHOR), state='*')
async def settings_reply(message: types.Message, state: FSMContext):
    await state.finish()
