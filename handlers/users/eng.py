from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp, bot
from aiogram import types
from states.user import EngUsers, UserStates
from keyboards.default.eng import *
from utils.databace import *
from .location import get_location_address


@dp.message_handler(state=UserStates.language, text="English 🇺🇸")
async def eng_lang(message: types.Message):
    await message.answer("""
Already millions of people meet in Teomatchbot 😍

I will help you find a mate or just friends 👫    
    """, reply_markup=lets_start)
    await EngUsers.state.set()


@dp.message_handler(state=EngUsers.state, text="👌 let's start")
async def letsstart(message: types.Message):
    await message.answer(f"""
❗️Remember that on the internet people can impersonate others

The bot does not ask for personal data and does not identify users by any documents.

By continuing, you accept <a href="https://docs.google.com/document/d/1r2aBc9qr17o8IH_acy0IU7a1hz_8z4yh6HTdw7nkLOg/edit?tab=t.0">user agreement</a> and <a href="https://docs.google.com/document/d/1auIszEse9cwatbvRTS1hPxapFU5ekvh3DfcDeTcwBtc/edit?tab=t.0">privacy policy</a>.    
    """, reply_markup=ok_btn)


@dp.message_handler(state=EngUsers.state, text="👌 Ok")
async def ok_func(message: types.Message):
    await message.answer("Your age?", reply_markup=types.ReplyKeyboardRemove())
    await EngUsers.age.set()


@dp.message_handler(state=EngUsers.age, content_types=types.ContentType.TEXT)
async def age_save_func(message: types.Message):
    check = message.text.isdigit()
    if check:
        await save_age(message.from_user.id, int(message.text))
        await message.answer("Specify your gender", reply_markup=gender_btn)
        await EngUsers.gender.set()
    else:
        await message.answer("Please send only the number", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=EngUsers.gender, text=["I'm female", "I'm male"])
async def gender_save_func(message: types.Message):
    gender = ""
    if message.text == "I'm female":
        gender = "female"
    else:
        gender = "male"
    await save_gender(message.from_user.id, gender)
    await message.answer("Who are you looking for?", reply_markup=lfgender_btn)
    await EngUsers.lfgender.set()


@dp.message_handler(state=EngUsers.lfgender, text=["Women", "Men", "No matter"])
async def lfgender_save_func(message: types.Message):
    await save_lfgender(message.from_user.id, message.text)
    await message.answer("Your city?", reply_markup=city_loc_btn)
    await EngUsers.city.set()


@dp.message_handler(state=EngUsers.city, content_types=[types.ContentType.LOCATION, types.ContentType.TEXT])
async def location_save_func(message: types.Message, state: FSMContext):
    address = None
    if message.location:
        longitude = message.location.longitude
        latitude = message.location.latitude
        address = await get_location_address(latitude, longitude)
    else:
        address = message.text
    await save_city(message.from_user.id, address)
    name_btn = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(f"{message.from_user.full_name}")]], resize_keyboard=True)
    await message.answer("What’s your name?", reply_markup=name_btn)
    await EngUsers.name.set()


@dp.message_handler(state=EngUsers.name, content_types=types.ContentType.TEXT)
async def name_save_func(message: types.Message):
    await save_name(message.from_user.id, message.text)
    await message.answer(
        "Tell more about yourself. Who are you looking for? What do you want to do? I'll find the best matches.",
        reply_markup=skip_btn)
    await EngUsers.description.set()


@dp.message_handler(state=EngUsers.description, content_types=types.ContentType.TEXT, text="Skip")
async def description_save_func(message: types.Message):
    if message.text != "Skip":
        await save_description(message.from_user.id, message.text)
    await message.answer("Send your photo (up to 15 sec)", reply_markup=types.ReplyKeyboardRemove())
    await EngUsers.photo.set()


@dp.message_handler(state=EngUsers.photo, content_types=types.ContentType.PHOTO)
async def handle_photo_album(message: types.Message):
    file_id = message.photo[-1].file_id
    await save_photo(message.from_user.id, file_id)
    await message.answer("Your profile:")
    user = await user_data(message.from_user.id)
    print(user)
    caption = f"""
Name: {user[6]} 
Age: {user[2]} 
City: {user[5]}
"""
    if user[7] == None:
        pass
    else:
        caption += f"\n\n{user}"
    await message.answer_photo(file_id, caption=caption)
    await message.answer("Correct?", reply_markup=correct_btn)
    await EngUsers.correct.set()


@dp.message_handler(state=EngUsers.correct, text=["Yes", "Edit My Profile"])
async def accounc_data_finished(message: types.Message):
    if message.text == "Yes":
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
                    InlineKeyboardButton(text="❤️", callback_data=f"like_{message.from_user.id}"),
                    InlineKeyboardButton(text="💌 / 📹", callback_data=f"send_msg_{message.from_user.id}"),
                    InlineKeyboardButton(text="👎", callback_data=f"dislike_{message.from_user.id}"),
                    InlineKeyboardButton(text="💤", callback_data=f"zzz_{message.from_user.id}")
                ]
            ]
        )
        await message.answer_photo(random_user_data[8], caption=caption, reply_markup=random_user_btn)
    elif message.text == "Edit My Profile":
        await message.answer("Your age?", reply_markup=types.ReplyKeyboardRemove())
        await EngUsers.age.set()
    else:
        pass
