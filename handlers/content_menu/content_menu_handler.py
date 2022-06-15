from aiogram import types
from aiogram.utils.markdown import bold
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import ChatTypeFilter

from bot_app import dp, bot
# from states import SeedPhraseState, DepositState, TokenState, BtcDepositState
from config import *
from keyboards.content_inline import content_inline_keyboard as content_kb

from random import shuffle


# What Python
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=CONTENT_WHAT_PYTHON, state='*')
async def show_what_python(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=None)
    # await call.message.answer(SELECTED + bold(CONTENT_WHAT_PYTHON), parse_mode=ParseMode.MARKDOWN)
    await call.message.answer_photo(photo='https://avatars.githubusercontent.com/u/51515513?s=280&v=4',
                                    caption=f'{CONTENT_WHAT_PYTHON}\n', reply_markup=content_kb.next_menu_keyboard,
                                    parse_mode=ParseMode.MARKDOWN)


# Next
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=NEXT_BUTTON, state='*')
async def show_next(call: types.CallbackQuery, state: FSMContext):
    photo_caption = call.message.caption
    if photo_caption.startswith(CONTENT_WHAT_PYTHON):
        await call.message.edit_caption(caption='fjldfjldf', reply_markup=content_kb.back_menu_keyboard)
        # await call.message.edit_reply_markup(reply_markup=content_kb.back_menu_keyboard)


# Back
@dp.callback_query_handler(ChatTypeFilter(types.ChatType.PRIVATE), text=BACK_BUTTON, state='*')
async def show_next(call: types.CallbackQuery, state: FSMContext):
    photo_caption = call.message.caption
    await call.message.edit_caption(caption=CONTENT_WHAT_PYTHON, reply_markup=content_kb.next_menu_keyboard)
