from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lets_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👌 let's start")
        ]
    ],
    resize_keyboard=True
)

ok_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👌 Ok")
        ]
    ],
    resize_keyboard=True
)

gender_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("I'm female"),
            KeyboardButton("I'm male")

        ],
    ],
    resize_keyboard=True
)

lfgender_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Women"),
            KeyboardButton("Men"),
            KeyboardButton("No matter")
        ]
    ],
    resize_keyboard=True
)

city_loc_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Send Location 📍", request_location=True)
        ]
    ],
    resize_keyboard=True
)

correct_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Yes"),
            KeyboardButton("Edit My Profile")
        ]
    ],
    resize_keyboard=True
)

skip_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Skip")
        ]
    ]
)

