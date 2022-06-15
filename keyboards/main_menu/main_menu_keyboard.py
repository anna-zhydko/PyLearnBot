from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from config import *


# Main ReplyKeyboard
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_buttons = [KEY_BUTTON_CONTENT, KEY_BUTTON_AUTHOR]
main_keyboard.add(*main_buttons)



