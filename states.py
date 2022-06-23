from aiogram.dispatcher.filters.state import State, StatesGroup


class GraphState(StatesGroup):
    coefficient = State()


class RegxState(StatesGroup):
    pattern = State()
    string = State()
