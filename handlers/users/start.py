from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.btn import *
from states.user import UserStates
from loader import dp
from utils.databace import *
from aiogram.types import *
from states.user import *


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    user = await check_user(message.from_user.id)
    if user:
        random_user_data = await select_random()
        caption = f"""
Name: {random_user_data[6]} 
Age: {random_user_data[2]} 
City: {random_user_data[5]}
                """
        if random_user_data[7] == None:
            pass
        else:
            caption += f"\n\n{random_user_data[7]}"
        random_user_btn = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="❤️", callback_data=f"like_{random_user_data[1]}/{message.from_user.id}"),
                    InlineKeyboardButton(text="💌 / 📹",
                                         callback_data=f"send_msg_{random_user_data[1]}/{message.from_user.id}"),
                    InlineKeyboardButton(text="👎",
                                         callback_data=f"dislike_{random_user_data[1]}/{message.from_user.id}"),
                    InlineKeyboardButton(text="💤", callback_data=f"zzz_{random_user_data[1]}/{message.from_user.id}")
                ]
            ]
        )
        await message.answer_photo(random_user_data[8], caption=caption, reply_markup=random_user_btn)
        await state.finish()
        await Socials.state.set()
    else:
        await message.answer("Choose your language 👇", reply_markup=lang_btn)
        await UserStates.language.set()
