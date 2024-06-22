import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types
from default_button import menu_button, sell_avto
# from inline_button import keyboard
load_dotenv()

API_TOKEN = os.getenv("ssh_key")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def first_massage(message: types.Message):
    full_name = message.from_user.full_name
    await message.reply(f"Assalomu aleykum {full_name}", reply_markup=menu_button)

@dp.message_handler(lambda message: message.text == "Avtomobil sotish")
async def menu_massage(message: types.Message):
    await message.reply(f"Avtomobil turini tanglang", reply_markup=sell_avto)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)