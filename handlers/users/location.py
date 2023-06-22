from loader import dp
from aiogram.types import *
from utils.misc.get_distance import choose_shortest_kafelar, choose_shortest_hotellar
from keyboards.inline.oxiri import twoway, yaqinhotel, yaqinkafe


@dp.message_handler(content_types='location')
async def get_location(message: Message):
    location = message.location
    closest_hotels = choose_shortest_hotellar(location)
    closest_cafes = choose_shortest_kafelar(location)
    await message.answer("Sorry, Can you choose that:", reply_markup=twoway)
    try:
        yaqinkafe.inline_keyboard = []
        yaqinhotel.inline_keyboard = []

    except:
        pass
    for hotel_name, distance1, url1, hotel_location in closest_hotels:
        key1 = InlineKeyboardButton(text=f"{hotel_name} \nOradagi masofa: {distance1} metr", url=url1, )
        yaqinhotel.insert(key1)
    for kafe_name, distance2, url2, kafe_location in closest_cafes:
        key1 = InlineKeyboardButton(text=f"{kafe_name} \nOradagi masofa: {distance2} metr", url=url2)
        yaqinkafe.insert(key1)
