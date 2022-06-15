from aiogram.utils.emoji import emojize
from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

# Token
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Settings Commands
COMMAND_START = 'Головне меню'
COMMAND_HELP = 'Довідка'
COMMAND_CONTENT = 'Зміст'
COMMAND_AUTHOR = 'Про автора'

# Messages
MESSAGE_GREETINGS_PRIVATE = "Вітаю в Learn.py!\nВчи Python разом з нами"
MESSAGE_HELP = "Бот призначений для ознайомлення з мовою програмування Python.\nЗавжди з вами."
MESSAGE_UNKNOWN = 'Натисність /start щоб побачити голвне меню'

# Selected
SELECTED = 'Selected: \n'

# Main Menu ReplyKeyboard
KEY_BUTTON_CONTENT = emojize(':page_with_curl:') + ' Зміст'
KEY_BUTTON_AUTHOR = emojize(':bar_chart:') + ' Про автора'

# Author
ABOUT_AUTHOR = ''

# Content
CONTENT_LIST = 'Оберіть тему'
CONTENT_WHY_PYTHON = 'Чому Python?'
CONTENT_WHAT_PYTHON = 'Що таке Python?'
CONTENT_INVENTOR = 'Ким був розроблений Python?'
CONTENT_DATA_TYPES = 'Типи даних'
CONTENT_IF_ELSE = 'Умовні оператори'
CONTENT_lOOP = 'Цикли'
CONTENT_FUNCTIONS = 'Функції'

CONTENT_WHY_PYTHON_PHOTO = 'Чому Python?'
CONTENT_WHAT_PYTHON_PHOTO = 'Що таке Python?'
CONTENT_INVENTOR_PHOTO = 'Ким був розроблений Python?'
CONTENT_DATA_TYPES_PHOTO = 'Типи даних'
CONTENT_IF_ELSE_PHOTO = 'Умовні оператори'
CONTENT_lOOP_PHOTO = 'Цикли'
CONTENT_FUNCTIONS_PHOTO = 'Функції'

# Navigate buttons
NEXT_BUTTON = emojize(':arrow_forward:')
BACK_BUTTON = emojize(':arrow_backward:')

# CLOSE BUTTON
CLOSE_BUTTON = emojize(':heavy_multiplication_x:') + 'Close'

# WENT WRONG
FAILED_SORRY = emojize(':heavy_exclamation_mark:') + ' Sorry. Something went wrong. Try later.'


# THROTTLING MESSAGES
THROTTLING_EXCEEDED_LIMIT = 'Exceeded the limit of messages to user, try again later.'
THROTTLING_UNBLOCKED = 'Unblocked.'


