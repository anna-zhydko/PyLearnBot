from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from config import *

from random import shuffle


deposit_menu_cb = CallbackData('post', 'value')


# Deposit InlineKeyboard
content_menu_keyboard = InlineKeyboardMarkup(row_width=1)
content_buttons = [
    InlineKeyboardButton(text=CONTENT_WHAT_PYTHON, callback_data=CONTENT_WHAT_PYTHON),
    InlineKeyboardButton(text=CONTENT_WHY_PYTHON, callback_data=CONTENT_WHY_PYTHON),
    InlineKeyboardButton(text=CONTENT_INVENTOR, callback_data=CONTENT_INVENTOR),
    InlineKeyboardButton(text=CONTENT_DATA_TYPES, callback_data=CONTENT_DATA_TYPES),
    InlineKeyboardButton(text=CONTENT_IF_ELSE, callback_data=CONTENT_IF_ELSE),
    InlineKeyboardButton(text=CONTENT_FOR_LOOP, callback_data=CONTENT_FOR_LOOP),
    InlineKeyboardButton(text=CONTENT_WHILE_LOOP, callback_data=CONTENT_WHILE_LOOP),
    InlineKeyboardButton(text=CONTENT_FUNCTIONS, callback_data=CONTENT_FUNCTIONS),
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


# Close InlineKeyboard
close_menu_keyboard = InlineKeyboardMarkup(row_width=1)
close_buttons = [
    InlineKeyboardButton(text='Стоп', callback_data='Close'),
]
close_menu_keyboard.add(*close_buttons)


# again InlineKeyboard
again_menu_keyboard = InlineKeyboardMarkup(row_width=1)
again_buttons = [
    InlineKeyboardButton(text='Знов', callback_data='again'),
]
again_menu_keyboard.add(*again_buttons)


# again InlineKeyboard
start_test_menu_keyboard = InlineKeyboardMarkup(row_width=1)
start_test_buttons = [
    InlineKeyboardButton(text='Почати тестування!', callback_data='start_test'),
]
start_test_menu_keyboard.add(*start_test_buttons)


# Regx InlineKeyboard
regx_menu_keyboard = InlineKeyboardMarkup(row_width=1)
regx_buttons = [
    InlineKeyboardButton(text='Шаблони', callback_data='pattern'),
    InlineKeyboardButton(text='Регулярні вирази online', callback_data='regx_online'),
]
regx_menu_keyboard.add(*regx_buttons)
