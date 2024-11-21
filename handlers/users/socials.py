from keyboards.default.eng import *
from loader import dp, bot
from aiogram.types import *
from aiogram import types
from states.user import Socials
from utils.databace import *


@dp.callback_query_handler(state=Socials.state)
async def socials_func(call: types.CallbackQuery):
    action, user_data_str = call.data.split("_", 1)
    try:
        user_id, sender_id = user_data_str.split("/")
        user_id, sender_id = int(user_id), int(sender_id)
    except ValueError:
        await call.answer("Xatolik yuz berdi. Callback ma'lumotlari noto'g'ri!")
        return

    if action == "like":
        user = await user_data(user_id)
        sender_user = await user_data(sender_id)
        socials_btn = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton("1 👍", callback_data=f"user_like_{user_id}/{sender_id}"),
                    InlineKeyboardButton("2 👎", callback_data=f"user_dislike_{user_id}/{sender_id}")
                ]
            ]
        )
        await bot.send_message(user_id, f"""
{user[6]} liked you. Have a look?

1. Show.
2. Not searching anymore.
        """, reply_markup=socials_btn)
        await bot.send_message(user_id,
                               f'Matched! Start chatting 👉 <a href="https://t.me/user?id={sender_id}">{sender_user[6]}</a>')
        await Socials.like.set()
    elif action == "send_msg":
        await call.answer(f"Foydalanuvchi {user_id} ga xabar yuborish!")

    elif action == "dislike":
        await call.answer(f"Foydalanuvchi {user_id} dislike bosdi! 👎")

    elif action == "zzz":
        await call.answer(f"Foydalanuvchi {user_id} dam olmoqda! 💤")


@dp.callback_query_handler(state=Socials.like)
async def socials_like_funcc(call: types.CallbackQuery):
    print(call.data)
    action, user_data_str = call.data.split("_", 1)
    print(action)
    try:
        user_id, sender_id = user_data_str.split("/")
        user_id, sender_id = int(user_id), int(sender_id)
    except ValueError:
        await call.answer("Xatolik yuz berdi. Callback ma'lumotlari noto'g'ri!")
        return

    if action == "user_like_":
        sender_user_data = await user_data(sender_id)
        caption = f"""
Name: {sender_user_data[6]} 
Age: {sender_user_data[2]} 
City: {sender_user_data[5]}
                        """
        if sender_user_data[7] == None:
            pass
        else:
            caption += f"\n\n{sender_user_data[7]}"
        random_user_btn = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="❤️", callback_data=f"like_{sender_user_data[1]}/{call.message.chat.id}"),
                    InlineKeyboardButton(text="💌 / 📹",
                                         callback_data=f"send_msg_{sender_user_data[1]}/{call.message.chat.id}"),
                    InlineKeyboardButton(text="👎",
                                         callback_data=f"dislike_{sender_user_data[1]}/{call.message.chat.id}"),
                    InlineKeyboardButton(text="💤", callback_data=f"zzz_{sender_user_data[1]}/{call.message.chat.id}")
                ]
            ]
        )
        await call.message.answer_photo(sender_user_data[8], caption=caption, reply_markup=random_user_btn)
        await Socials.state.set()

    elif action == "user_dislike_":
        pass
