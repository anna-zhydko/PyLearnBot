from aiogram.dispatcher.filters.state import State, StatesGroup


class FAQState(StatesGroup):
    question = State()
