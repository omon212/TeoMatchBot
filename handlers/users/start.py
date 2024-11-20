from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.btn import *
from states.user import UserStates
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Choose your language 👇", reply_markup=lang_btn)
    await UserStates.language.set()

