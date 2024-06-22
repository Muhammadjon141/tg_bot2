from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_button = ReplyKeyboardMarkup([
    [KeyboardButton("Avtomobil sotish"), KeyboardButton("Avtomobil sotib olish")]],
    resize_keyboard=True)

sell_avto = ReplyKeyboardMarkup([
    [KeyboardButton("Yengil mashina"), KeyboardButton("Yuk mashina")],
    [KeyboardButton("Mototrsikl"), KeyboardButton("Qayiqlar")]],
    resize_keyboard=True)