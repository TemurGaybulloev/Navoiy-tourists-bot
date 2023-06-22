from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

twoway = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="3 closest cafes", callback_data="close1")
        ],
        [
            InlineKeyboardButton(text="3 closest hotels", callback_data="close2")
        ],
    ]
)
