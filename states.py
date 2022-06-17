from aiogram.dispatcher.filters.state import State, StatesGroup


class GraphState(StatesGroup):
    coefficient = State()
