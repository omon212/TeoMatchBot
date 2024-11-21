from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.btn import *
from states.user import UserStates
from loader import dp
from utils.databace import *


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    user = await check_user(message.from_user.id)
    print(user)
    if user:
        await message.answer_photo(user[8], f"""
Name: {user[6]} 
Age: {user[2]} 
City: {user[5]}

{user[7]}
""")
    else:
        await message.answer("Choose your language 👇", reply_markup=lang_btn)
        await UserStates.language.set()
