from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

birinchiMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Cafes", callback_data="kafelar"),
        ],
        [
            InlineKeyboardButton(text="Hotels", callback_data="hotellar"),
        ],
        [
            InlineKeyboardButton(text="Museums", callback_data="muzeylar"),
        ],
    ]
)
ikkinchikafeMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="list of cafes", callback_data="kafelar_royxat")
        ],
        [
            InlineKeyboardButton(text="3 closest cafes", callback_data="yaqin_kafelar")
        ],
        [
            InlineKeyboardButton(text="⬅️ Back", callback_data="kafelar_ortga")
        ],
    ]
)
ikkinchihotelMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="list of hotels", callback_data="hotel_royxat")
        ],
        [
            InlineKeyboardButton(text="3 closest hotels", callback_data="yaqin_hotel")
        ],
        [
            InlineKeyboardButton(text="⬅️ Back", callback_data="hotellar_ortga")
        ],
    ]
)
ikkinchimuzeyMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="list of museums", callback_data="muzey_royxat")
        ],
        [
            InlineKeyboardButton(text="3 closest museums", callback_data="yaqin_muzey")
        ],
        [
            InlineKeyboardButton(text="⬅️ Back", callback_data="muzeylar_ortga")
        ],
    ]
)

