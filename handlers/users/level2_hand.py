from aiogram.types import CallbackQuery
from aiogram.types import Message
from keyboards.inline.ichki_tugmalar import *
from keyboards.inline.level_2 import *
from loader import dp
from keyboards.default.bittatugma import mylocationkey, menu
from utils.misc.get_distance import *
from keyboards.inline.oxiri import twoway
from keyboards.inline.oxiri import yaqinhotel, yaqinkafe

@dp.callback_query_handler(text="hotel_royxat")
async def hotellar(call: CallbackQuery):
    await call.message.answer("List of some hotels in Navai", reply_markup=hotellarMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="yaqin_hotel")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="Send your location:", reply_markup=mylocationkey)
    await call.message.delete()

@dp.callback_query_handler(text="close1")
async def hotel_ort(call: CallbackQuery):
    await call.message.answer("Locations:", reply_markup=yaqinkafe)
    await call.message.answer(text="Please choose the options👆", reply_markup=menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="close2")
async def hotel_ort(call: CallbackQuery):
    await call.message.answer("Locations:", reply_markup=yaqinhotel)
    await call.message.answer(text="Please choose the options👆", reply_markup=menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="hotellar_ortga")
async def hotel_ort(call: CallbackQuery):
    await call.message.answer("Cafes, Hotels and Museums in Navai:", reply_markup=birinchiMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="kafelar_royxat")
async def kafelar(call: CallbackQuery):
    await call.message.answer("List of some cafes in Navai", reply_markup=kafelarMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="yaqin_kafelar")
async def kafelar_yaqin(call: CallbackQuery):
    await call.message.answer(text="Send your location:", reply_markup=mylocationkey)
    await call.message.delete()

@dp.callback_query_handler(text="kafelar_ortga")
async def kafe_ort(call: CallbackQuery):
    await call.message.answer("Cafes, Hotels and Museums in Navai:", reply_markup=birinchiMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="muzey_royxat")
async def muzeylar(call: CallbackQuery):
    await call.message.answer("List of some museums in Navai:", reply_markup=muzeylarMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="yaqin_muzey")
async def muzeylar_yaqin(call: CallbackQuery):
    await call.message.answer("This is all museum in our list:", reply_markup=muzeylarMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="muzeylar_ortga")
async def muzey_ort(call: CallbackQuery):
    await call.message.answer("Cafes, Hotels and Museums in Navai:", reply_markup=birinchiMenu)
    await call.message.delete()
    await call.answer(cache_time=60)
