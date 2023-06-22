import logging
from aiogram import Dispatcher, CallbackQuery
from keyboards.inline.ichki_tugmalar import *
from aiogram.types import ReplyKeyboardRemove
from loader import dp, bot
from keyboards.inline.ichki_tugmalar import birinchiMenu
from loader import dp




@dp.callback_query_handler(text="kafelar")
async def kafelar(call: CallbackQuery):
     await call.message.answer("Cafes in Navai", reply_markup=ikkinchikafeMenu)
     await call.message.delete()
     await call.answer(cache_time=60)


@dp.callback_query_handler(text="hotellar")
async def hotellar(call: CallbackQuery):
     await call.message.answer("Hotels in Navai", reply_markup=ikkinchihotelMenu)
     await call.message.delete()
     await call.answer(cache_time=60)

@dp.callback_query_handler(text="muzeylar")
async def muzeylar(call: CallbackQuery):
     await call.message.answer("Museums in Navai", reply_markup=ikkinchimuzeyMenu)
     await call.message.delete()
     await call.answer(cache_time=60)

@dp.callback_query_handler(text="kafelar_ortga")
async def kafe_ort(call: CallbackQuery):
    await call.message.answer("Cafes, Hotels and Museums in Navai:", reply_markup=birinchiMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="hotellar_ortga")
async def kafe_ort(call: CallbackQuery):
    await call.message.answer("Cafes, Hotels and Museums in Navai:", reply_markup=birinchiMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="muzeylar_ortga")
async def kafe_ort(call: CallbackQuery):
    await call.message.answer("Cafes, Hotels and Museums in Navai:", reply_markup=birinchiMenu)
    await call.message.delete()
    await call.answer(cache_time=60)
