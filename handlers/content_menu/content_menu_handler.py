from aiogram import types
from aiogram.utils.markdown import bold
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode, ContentType
from aiogram.dispatcher.filters import ChatTypeFilter

from bot_app import dp, bot
from config import *
from keyboards.content_inline import content_inline_keyboard as content_kb
from keyboards.main_menu import main_menu_keyboard as main_kb
from database.sqlite_db import show_expressions, get_questions1, get_questions2, get_questions3
from states import RegxState, TestState

import os
import re


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


# regx online
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), lambda call: call.data == 'regx_online', state='*')
async def show_regx(call: types.CallbackQuery, state: FSMContext):
    await RegxState.pattern.set()
    await call.message.answer('Введіть шаблон регулярного виразу\nнаприклад *(?<=-)\w+*:', parse_mode=ParseMode.MARKDOWN)


# get pattern regx
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), state=RegxState.pattern)
async def get_pattern(message: types.Message, state: FSMContext):
    await state.update_data(pattern=message.text)
    await RegxState.string.set()
    await message.answer('Введіть строку:')


# get pattern string
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), state=RegxState.string)
async def get_string(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    pattern = state_data.get('pattern')
    match_obj = re.search(r'{}'.format(pattern), message.text)
    match = match_obj.group(0)
    await message.answer(f'Співпадіння:\n{match}', reply_markup=content_kb.again_menu_keyboard)
    await state.finish()


# Pattern
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), lambda call: call.data == 'pattern', state='*')
async def show_pattern(call: types.CallbackQuery, state: FSMContext):
    await show_expressions()
    path = os.path.abspath('table.png')
    await call.message.answer_photo(photo=open(path, 'rb'), reply_markup=content_kb.back_menu_keyboard)


# test start
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), lambda call: call.data == 'start_test', state='*')
async def show_pattern(call: types.CallbackQuery, state: FSMContext):
    # call.telegram_types.Rtypes.ReplyKeyboardRemove()
    await TestState.n_1.set()
    db_data = await get_questions2()
    question_first = db_data[0]
    # await TestState.n_11.set()
    # await state.update_data(correct=question_first[2], chat_id=call.message.chat.id)
    # await call.message.answer_poll(question=question_first[0],
    #                                options=question_first[1].split('_'),
    #                                is_anonymous=False,
    #                                type='regular',
    #                                allows_multiple_answers=True,
    #                                explanation='Неправильна відповідь!',
    #                                open_period=6,
    #                                correct_option_id=question_first[2], reply_markup=None)
    # await call.message.answer('Вам нараховано 2 бали')


# 14 question
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), state=TestState.n_11)
async def n_11(message: types.Message, state: FSMContext):
    await message.answer('Вам нараховано один бал')
    await message.answer('Ваш результат: 7')

@dp.poll_answer_handler()
async def some_poll_answer_handler(poll_answer: types.PollAnswer):
    state = dp.current_state()
    state_data = await state.get_data()
    correct_option, chat_id = state_data.get('correct'), state_data.get('chat_id')

    if await state.get_state() == TestState.n_1.state:
        answer_id = poll_answer.option_ids[0]
        if correct_option == str(answer_id):
            await TestState.n_2.set()
            db_data = await get_questions1()
            question_second = db_data[1]
            state.update_data(score=1)
            await bot.send_message(chat_id=chat_id, text='Вам нараховано 1 бал')
            await bot.send_poll(question=question_second[0],
                                   options=question_second[1].split('_'),
                                   is_anonymous=False,
                                   type='quiz',
                                   allows_multiple_answers=False,
                                   explanation='Неправильна відповідь!',
                                   open_period=6,
                                   correct_option_id=question_second[2])

    elif await state.get_state() == TestState.n_2.state:
        answer_id = poll_answer.option_ids[0]
        if correct_option == str(answer_id):
            score = state_data.get('score') + 1
            state.update_data(score=score)
        await TestState.n_3.set()
        db_data = await get_questions1()
        question = db_data[2]

        await bot.send_message(chat_id=chat_id, text='Вам нараховано 1 бал')
        await bot.send_poll(question=question[0],
                            options=question[1].split('_'),
                            is_anonymous=False,
                            type='quiz',
                            allows_multiple_answers=False,
                            explanation='Неправильна відповідь!',
                            open_period=6,
                            correct_option_id=question[2])

    elif await state.get_state() == TestState.n_3.state:
        answer_id = poll_answer.option_ids[0]
        if correct_option == str(answer_id):
            await TestState.n_4.set()
            db_data = await get_questions1()
            question = db_data[3]
            score = state_data.get('score') + 1
            state.update_data(score=score)
            await bot.send_message(chat_id=chat_id, text='Вам нараховано 1 бал')
            await bot.send_poll(question=question[0],
                                options=question[1].split('_'),
                                is_anonymous=False,
                                type='quiz',
                                allows_multiple_answers=False,
                                explanation='Неправильна відповідь!',
                                open_period=6,
                                correct_option_id=question[2])

    elif await state.get_state() == TestState.n_4.state:
        answer_id = poll_answer.option_ids[0]
        if correct_option == str(answer_id):
            await TestState.n_5.set()
            db_data = await get_questions1()
            question = db_data[4]
            score = state_data.get('score') + 1
            state.update_data(score=score)
            await bot.send_message(chat_id=chat_id, text='Вам нараховано 1 бал')
            await bot.send_poll(question=question[0],
                                options=question[1].split('_'),
                                is_anonymous=False,
                                type='quiz',
                                allows_multiple_answers=False,
                                explanation='Неправильна відповідь!',
                                open_period=6,
                                correct_option_id=question[2])

    elif await state.get_state() == TestState.n_5.state:
        answer_ids = poll_answer.option_ids
        for ans in answer_ids:
            if ans == correct_option:
                score = state_data.get('score') + 1
                state.update_data(score=score)

        await TestState.n_6.set()
        db_data = await get_questions2()
        question = db_data[0]

        await bot.send_poll(question=question[0],
                            options=question[1].split('_'),
                            is_anonymous=False,
                            type='regular',
                            allows_multiple_answers=False,
                            explanation='Неправильна відповідь!',
                            open_period=6,
                            correct_option_id=question[2])

    elif await state.get_state() == TestState.n_6.state:
        answer_ids = poll_answer.option_ids
        for ans in answer_ids:
            if ans == correct_option:
                score = state_data.get('score') + 1
                state.update_data(score=score)

        await TestState.n_7.set()
        db_data = await get_questions2()
        question = db_data[1]

        await bot.send_poll(question=question[0],
                            options=question[1].split('_'),
                            is_anonymous=False,
                            type='regular',
                            allows_multiple_answers=False,
                            explanation='Неправильна відповідь!',
                            open_period=6,
                            correct_option_id=question[2])

    elif await state.get_state() == TestState.n_7.state:
        answer_ids = poll_answer.option_ids
        for ans in answer_ids:
            if ans == correct_option:
                score = state_data.get('score') + 1
                state.update_data(score=score)

        await TestState.n_8.set()
        db_data = await get_questions2()
        question = db_data[2]

        await bot.send_poll(question=question[0],
                            options=question[1].split('_'),
                            is_anonymous=False,
                            type='regular',
                            allows_multiple_answers=False,
                            explanation='Неправильна відповідь!',
                            open_period=6,
                            correct_option_id=question[2])

    elif await state.get_state() == TestState.n_8.state:
        answer_ids = poll_answer.option_ids
        for ans in answer_ids:
            if ans == correct_option:
                score = state_data.get('score') + 1
                state.update_data(score=score)

        await TestState.n_9.set()
        db_data = await get_questions2()
        question = db_data[3]

        await bot.send_poll(question=question[0],
                            options=question[1].split('_'),
                            is_anonymous=False,
                            type='regular',
                            allows_multiple_answers=False,
                            explanation='Неправильна відповідь!',
                            open_period=6,
                            correct_option_id=question[2])

    elif await state.get_state() == TestState.n_9.state:
        answer_ids = poll_answer.option_ids
        for ans in answer_ids:
            if ans == correct_option:
                score = state_data.get('score') + 1
                state.update_data(score=score)

        await TestState.n_10.set()
        db_data = await get_questions2()
        question = db_data[4]

        await bot.send_poll(question=question[0],
                            options=question[1].split('_'),
                            is_anonymous=False,
                            type='regular',
                            allows_multiple_answers=False,
                            explanation='Неправильна відповідь!',
                            open_period=6,
                            correct_option_id=question[2])

    elif await state.get_state() == TestState.n_10.state:
        answer_ids = poll_answer.option_ids
        for ans in answer_ids:
            if ans == correct_option:
                score = state_data.get('score') + 1
                state.update_data(score=score)

        await TestState.n_11.set()
        db_data = await get_questions2()
        question = db_data[2]
        await bot.send_message(question[0])
        state.update_data(correct=question[1])


# 11 question
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), state=TestState.n_11)
async def n_11(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    correct, score = state_data.get('correct'), state_data.get('score')
    if correct == message.text:
        new_score = score + 1
        await state.update_data(score=new_score)
        await message.answer('Вам нараховано один бал')
    await TestState.n_12.set()


# 12 question
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), state=TestState.n_12)
async def n_11(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    correct, score = state_data.get('correct'), state_data.get('score')
    if correct == message.text:
        new_score = score + 1
        await state.update_data(score=new_score)
        await message.answer('Вам нараховано один бал')
    await TestState.n_13.set()


# 13 question
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), state=TestState.n_13)
async def n_11(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    correct, score = state_data.get('correct'), state_data.get('score')
    if correct == message.text:
        new_score = score + 1
        await state.update_data(score=new_score)
        await message.answer('Вам нараховано один бал')
    await TestState.n_14.set()


# 14 question
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), state=TestState.n_14)
async def n_11(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    correct, score = state_data.get('correct'), state_data.get('score')
    if correct == message.text:
        new_score = score + 1
        await state.update_data(score=new_score)
        await message.answer('Вам нараховано один бал')
    await TestState.n_15.set()


# 15 question
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), state=TestState.n_15)
async def n_11(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    correct, score = state_data.get('correct'), state_data.get('score')
    if correct == message.text:
        new_score = score + 1
        await message.answer('Вам нараховано один бал')
    else:
        new_score = score
        await message.answer(f'Ваш результат: {new_score}')


# random message
@dp.message_handler(ChatTypeFilter(types.ChatType.PRIVATE), state='*', content_types=ContentType.all())
async def unknown_message_reply(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(MESSAGE_UNKNOWN)