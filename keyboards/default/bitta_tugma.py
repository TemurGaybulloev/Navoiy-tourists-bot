from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import middlewares
import filters
import handlers
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/start from scratch")
        ],
    ],
    resize_keyboard = True
)
mylocationkey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="location", request_location=True)
        ],
    ],
    resize_keyboard=True
)
