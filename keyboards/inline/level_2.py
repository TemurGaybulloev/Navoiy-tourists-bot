from data.information_navoiy import *
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kafelarMenu = InlineKeyboardMarkup(row_width=1)
for key in kafelar:
    button1 = InlineKeyboardButton(text=key[0], callback_data=key[1])
    kafelarMenu.add(button1)
kafelarMenu.add(InlineKeyboardButton(text="⬅️ Back", callback_data="kafelarMenu_ortga"))


muzeylarMenu = InlineKeyboardMarkup(row_width=1)
for key in muzeylar:
    button2 = InlineKeyboardButton(text=key[0], callback_data=key[1])
    muzeylarMenu.add(button2)
muzeylarMenu.add(InlineKeyboardButton(text="⬅️ Back", callback_data="muzeylarMenu_ortga"))


hotellarMenu = InlineKeyboardMarkup(row_width=1)
for key in hotellar:
    button3 = InlineKeyboardButton(text=key[0], callback_data=key[1])
    hotellarMenu.add(button3)
hotellarMenu.add(InlineKeyboardButton(text="⬅️ Back", callback_data="hotellarMenu_ortga"))

