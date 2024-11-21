from aiogram.dispatcher.filters.state import State, StatesGroup


class UserStates(StatesGroup):
    language = State()


class EngUsers(StatesGroup):
    state = State()
    age = State()
    gender = State()
    lfgender = State()
    city = State()
    name = State()
    photo = State()
    description = State()
    correct = State()


class Socials(StatesGroup):
    state = State()
    like = State()