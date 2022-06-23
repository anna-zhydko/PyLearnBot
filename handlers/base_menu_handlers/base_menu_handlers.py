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
from services.graphbuild import build_graph
from states import GraphState
from database.sqlite_db import show_expressions, get_questions1
from bot_app import dp, bot
import text_to_image


@dp.message_handler(commands=['start'], state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(MESSAGE_GREETINGS_PRIVATE, reply_markup=main_kb.main_keyboard)


@dp.message_handler(commands=['help'], state='*')
async def send_help(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(MESSAGE_HELP)


@dp.message_handler(commands=['stop_test'], state='*')
async def send_help(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Тест був випадково зупинений')


# Content
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), commands=['content'], state='*')
@dp.message_handler(Text(equals=KEY_BUTTON_CONTENT), state='*')
async def exchange(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(CONTENT_LIST, reply_markup=content_kb.content_menu_keyboard,  parse_mode=ParseMode.MARKDOWN)


# Author
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), commands=['author'], state='*')
@dp.message_handler(Text(equals=KEY_BUTTON_AUTHOR), state='*')
async def settings_reply(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(ABOUT_AUTHOR)


# Graph
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), commands=['function'], state='*')
@dp.message_handler(Text(equals=KEY_BUTTON_FUNCTION), state='*')
async def settings_reply(message: types.Message, state: FSMContext):
    await state.finish()
    await GraphState.coefficient.set()
    await message.answer(GRAPH_ENTER_COEFFICIENT, parse_mode=ParseMode.MARKDOWN)


# Enter "k" coefficient
@dp.message_handler(state=GraphState.coefficient)
async def exchange(message: types.Message, state: FSMContext):
    try:
        coefficient = float(message.text)
        graph_file = await build_graph(coefficient)
        await message.answer_photo(photo=graph_file)
    except:
        await message.answer(GRAPH_WRONG_COEFFICIENT, reply_markup=content_kb.close_menu_keyboard)


# Regex
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), commands=['regular_expression'], state='*')
@dp.message_handler(Text(equals=KEY_BUTTON_REGX), state='*')
async def regex_show(message: types.Message, state: FSMContext):
    await message.answer_photo(photo='https://miro.medium.com/max/1400/0*GU4K0A0TapCLjB07.jpeg',
                               caption=REGX_DESC, reply_markup=content_kb.regx_menu_keyboard, parse_mode=ParseMode.MARKDOWN)


# Test
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), commands=['test'], state='*')
@dp.message_handler(Text(equals=KEY_BUTTON_TEST), state='*')
async def start_test(message: types.Message, state: FSMContext):
    await message.answer_photo(photo='https://www.testim.io/blog/test-environment-guide/',
                               caption='Ви готові почати тестування?\nДля припинення натисність команду */stop_test*',
                               reply_markup=content_kb.start_test_menu_keyboard, parse_mode=ParseMode.MARKDOWN)
