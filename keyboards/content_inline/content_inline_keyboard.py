from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from config import *

from random import shuffle


deposit_menu_cb = CallbackData('post', 'value')


# Deposit InlineKeyboard
content_menu_keyboard = InlineKeyboardMarkup(row_width=1)
content_buttons = [
    InlineKeyboardButton(text=CONTENT_WHAT_PYTHON, callback_data=CONTENT_WHAT_PYTHON),
    InlineKeyboardButton(text=CONTENT_WHY_PYTHON, callback_data=deposit_menu_cb.new(value=CONTENT_WHY_PYTHON)),
    InlineKeyboardButton(text=CONTENT_INVENTOR, callback_data=deposit_menu_cb.new(value=CONTENT_INVENTOR)),
    InlineKeyboardButton(text=CONTENT_DATA_TYPES, callback_data=deposit_menu_cb.new(value=CONTENT_DATA_TYPES)),
    InlineKeyboardButton(text=CONTENT_IF_ELSE, callback_data=deposit_menu_cb.new(value=CONTENT_IF_ELSE)),
    InlineKeyboardButton(text=CONTENT_lOOP, callback_data=deposit_menu_cb.new(value=CONTENT_lOOP)),
    InlineKeyboardButton(text=CONTENT_FUNCTIONS, callback_data=deposit_menu_cb.new(value=CONTENT_FUNCTIONS)),
]
content_menu_keyboard.add(*content_buttons)

# Next InlineKeyboard
next_menu_keyboard = InlineKeyboardMarkup(row_width=1)
next_buttons = [
    InlineKeyboardButton(text=NEXT_BUTTON, callback_data=NEXT_BUTTON),
]
next_menu_keyboard.add(*next_buttons)

# Back InlineKeyboard
back_menu_keyboard = InlineKeyboardMarkup(row_width=1)
back_buttons = [
    InlineKeyboardButton(text=BACK_BUTTON, callback_data=BACK_BUTTON),
]
back_menu_keyboard.add(*back_buttons)
