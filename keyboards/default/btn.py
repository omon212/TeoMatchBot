from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

lang_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Uzbek 🇺🇿"),
            KeyboardButton("English 🇺🇸"),
            KeyboardButton("Русский 🇷🇺"),
        ],
    ],
    resize_keyboard=True
)