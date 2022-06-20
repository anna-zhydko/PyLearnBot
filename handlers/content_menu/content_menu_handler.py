from aiogram import types
from aiogram.utils.markdown import bold
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode, ContentType
from aiogram.dispatcher.filters import ChatTypeFilter

from bot_app import dp, bot
from config import *
from keyboards.content_inline import content_inline_keyboard as content_kb


async def show_question(photo, title, content_first, message, second_part=True):
    await message.edit_reply_markup(reply_markup=None)

    # Add button "next" if we have second part of description
    if second_part:
        reply_markup = content_kb.next_menu_keyboard
    else:
        reply_markup = None

    await message.answer_photo(photo=photo, caption=f'*{title}*\n\n{content_first}',
                               reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)


# What Python
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=CONTENT_WHAT_PYTHON, state='*')
async def show_what_python(call: types.CallbackQuery, state: FSMContext):
    await show_question(CONTENT_WHAT_PYTHON_PHOTO, CONTENT_WHAT_PYTHON, CONTENT_WHAT_PYTHON_FIRST, call.message)


# Why Python
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=CONTENT_WHY_PYTHON, state='*')
async def show_why_python(call: types.CallbackQuery, state: FSMContext):
    await show_question(CONTENT_WHY_PYTHON_PHOTO, CONTENT_WHY_PYTHON, CONTENT_WHY_PYTHON_FIRST, call.message)


# Python Inventor
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=CONTENT_INVENTOR, state='*')
async def show_what_python(call: types.CallbackQuery, state: FSMContext):
    await show_question(CONTENT_INVENTOR_PHOTO, CONTENT_INVENTOR, CONTENT_INVENTOR_FIRST, call.message)


# Data Types
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=CONTENT_DATA_TYPES, state='*')
async def show_what_python(call: types.CallbackQuery, state: FSMContext):
    await show_question(CONTENT_DATA_TYPES_PHOTO, CONTENT_DATA_TYPES, CONTENT_DATA_TYPES_FIRST, call.message,
                        second_part=False)


# If Else
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=CONTENT_IF_ELSE, state='*')
async def show_what_python(call: types.CallbackQuery, state: FSMContext):
    await show_question(CONTENT_IF_ELSE_PHOTO, CONTENT_IF_ELSE, CONTENT_IF_ELSE_FIRST, call.message, second_part=False)


# For Loop
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=CONTENT_FOR_LOOP, state='*')
async def show_what_python(call: types.CallbackQuery, state: FSMContext):
    await show_question(CONTENT_FOR_LOOP_PHOTO, CONTENT_FOR_LOOP, CONTENT_FOR_LOOP_FIRST, call.message)


# While Loop
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=CONTENT_WHILE_LOOP, state='*')
async def show_what_python(call: types.CallbackQuery, state: FSMContext):
    await show_question(CONTENT_WHILE_LOOP_PHOTO, CONTENT_WHILE_LOOP, CONTENT_WHILE_lOOP_FIRST, call.message,
                        second_part=False)


# Functions
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=CONTENT_FUNCTIONS, state='*')
async def show_what_python(call: types.CallbackQuery, state: FSMContext):
    await show_question(CONTENT_FUNCTIONS_PHOTO, CONTENT_FUNCTIONS, CONTENT_FUNCTIONS_FIRST, call.message)


# Next
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=NEXT_BUTTON, state='*')
async def show_next(call: types.CallbackQuery, state: FSMContext):
    photo_caption = call.message.caption
    if photo_caption.startswith(CONTENT_WHAT_PYTHON):
        await call.message.edit_caption(caption=CONTENT_WHAT_PYTHON_SECOND, reply_markup=content_kb.back_menu_keyboard,
                                        parse_mode=ParseMode.MARKDOWN)
    elif photo_caption.startswith(CONTENT_WHY_PYTHON):
        await call.message.edit_caption(caption=CONTENT_WHY_PYTHON_SECOND, reply_markup=content_kb.back_menu_keyboard,
                                        parse_mode=ParseMode.MARKDOWN)
    elif photo_caption.startswith(CONTENT_INVENTOR):
        await call.message.edit_caption(caption=CONTENT_INVENTOR_SECOND, reply_markup=content_kb.back_menu_keyboard,
                                        parse_mode=ParseMode.MARKDOWN)
    elif photo_caption.startswith(CONTENT_FUNCTIONS):
        await call.message.edit_caption(caption=CONTENT_FUNCTIONS_SECOND, reply_markup=content_kb.back_menu_keyboard,
                                        parse_mode=ParseMode.MARKDOWN)
    elif photo_caption.startswith(CONTENT_FOR_LOOP):
        await call.message.edit_caption(caption=CONTENT_FOR_lOOP_SECOND, reply_markup=content_kb.back_menu_keyboard,
                                        parse_mode=ParseMode.MARKDOWN)
    elif photo_caption.startswith(CONTENT_IF_ELSE):
        await call.message.edit_caption(caption=CONTENT_IF_ELSE_SECOND, reply_markup=content_kb.back_menu_keyboard,
                                        parse_mode=ParseMode.MARKDOWN)


# Back
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=BACK_BUTTON, state='*')
async def show_next(call: types.CallbackQuery, state: FSMContext):
    photo_caption = call.message.caption
    if photo_caption.startswith(CONTENT_WHAT_PYTHON_SECOND.replace('_', '').replace('*', '')):
        await call.message.edit_caption(caption=f'*{CONTENT_WHAT_PYTHON}*\n{CONTENT_WHAT_PYTHON_FIRST}',
                                        reply_markup=content_kb.next_menu_keyboard, parse_mode=ParseMode.MARKDOWN)
    elif photo_caption.startswith(CONTENT_WHY_PYTHON_SECOND.replace('_', '').replace('*', '')):
        await call.message.edit_caption(caption=f'*{CONTENT_WHY_PYTHON}*\n{CONTENT_WHY_PYTHON_FIRST}',
                                        reply_markup=content_kb.next_menu_keyboard, parse_mode=ParseMode.MARKDOWN)
    elif photo_caption.startswith(CONTENT_INVENTOR_SECOND.replace('_', '').replace('*', '')):
        await call.message.edit_caption(caption=f'*{CONTENT_INVENTOR}*\n{CONTENT_INVENTOR_FIRST}',
                                        reply_markup=content_kb.next_menu_keyboard, parse_mode=ParseMode.MARKDOWN)
    elif photo_caption.startswith(CONTENT_FUNCTIONS_SECOND.replace('_', '').replace('*', '')):
        await call.message.edit_caption(caption=f'*{CONTENT_FUNCTIONS}*\n{CONTENT_FUNCTIONS_FIRST}',
                                        reply_markup=content_kb.next_menu_keyboard, parse_mode=ParseMode.MARKDOWN)
    elif photo_caption.startswith(CONTENT_FOR_lOOP_SECOND.replace('_', '').replace('*', '')):
        await call.message.edit_caption(caption=f'*{CONTENT_FOR_LOOP}*\n{CONTENT_FOR_LOOP_FIRST}',
                                        reply_markup=content_kb.next_menu_keyboard, parse_mode=ParseMode.MARKDOWN)
    elif photo_caption.startswith(CONTENT_IF_ELSE_SECOND.replace('_', '').replace('*', '')):
        await call.message.edit_caption(caption=f'*{CONTENT_IF_ELSE}*\n{CONTENT_IF_ELSE_FIRST}',
                                        reply_markup=content_kb.next_menu_keyboard, parse_mode=ParseMode.MARKDOWN)


# random message
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), state='*', content_types=ContentType.all())
async def unknown_message_reply(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(MESSAGE_UNKNOWN)