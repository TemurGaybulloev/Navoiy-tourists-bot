from aiogram.types import CallbackQuery
from keyboards.inline.ichki_tugmalar import *
from keyboards.inline.level_2 import *
from loader import dp

@dp.callback_query_handler(text="muzeylarMenu_ortga")
async def muzeymenu_ort(call: CallbackQuery):
    await call.message.answer("List of some museums in Navai", reply_markup=ikkinchimuzeyMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="kafelarMenu_ortga")
async def kafemenu_ort(call: CallbackQuery):
    await call.message.answer("List of some cafes in Navai", reply_markup=ikkinchikafeMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="hotellarMenu_ortga")
async def hotelmenu_ort(call: CallbackQuery):
    await call.message.answer("List of some hotels in Navai", reply_markup=ikkinchihotelMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="h1")
async def h1(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h1":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h2")
async def h2(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h2":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h3")
async def h3(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h3":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h4")
async def h4(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h4":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h5")
async def h5(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h5":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h6")
async def h6(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h6":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h7")
async def h7(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h7":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h8")
async def h8(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h8":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h9")
async def h9(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h10":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h9")
async def h10(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h10":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h11")
async def h11(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h11":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h12")
async def h12(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h12":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h13")
async def h13(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h13":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h14")
async def h14(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h14":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="h15")
async def h15(call: CallbackQuery):
    for hotels in hotellar:
        if hotels[1] == "h15":
            await call.message.answer_location(latitude = hotels[2]["lat"], longitude = hotels[2]["lon"])
    await call.message.delete()


@dp.callback_query_handler(text="k1")
async def k1(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k1":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k2")
async def k2(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k2":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k3")
async def k3(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k3":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k4")
async def k4(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k4":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k5")
async def k5(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k5":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k6")
async def k6(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k6":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k7")
async def k7(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k7":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k8")
async def k8(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k8":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k9")
async def k9(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k9":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k10")
async def k10(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k10":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k11")
async def k11(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k11":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k12")
async def k12(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k12":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k13")
async def k13(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k13":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k14")
async def k14(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k14":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k15")
async def k15(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k15":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k16")
async def k16(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k16":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k17")
async def k17(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k17":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k18")
async def k18(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k18":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k19")
async def k19(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k19":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k20")
async def k20(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k20":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k21")
async def k21(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k21":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="k22")
async def k22(call: CallbackQuery):
    for kafe in kafelar:
        if kafe[1] == "k22":
            await call.message.answer_location(latitude=kafe[2]["lat"], longitude=kafe[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="m1")
async def m1(call: CallbackQuery):
    for muzey in muzeylar:
        if muzey[1] == "m1":
            await call.message.answer_location(latitude=muzey[2]["lat"], longitude=muzey[2]["lon"])
    await call.message.delete()

@dp.callback_query_handler(text="m2")
async def m2(call: CallbackQuery):
    for muzey in muzeylar:
        if muzey[1] == "m2":
            await call.message.answer_location(latitude=muzey[2]["lat"], longitude=muzey[2]["lon"])
    await call.message.delete()
