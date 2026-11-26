from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types import Message, BotCommand
from aiogram import Bot, Dispatcher, F
import asyncio
import os 
from dotenv import load_dotenv 
from random import randint,choice
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
from inline_buttons import *

load_dotenv()

tg_bot_token = os.getenv("TOKEN")
print(tg_bot_token)
dp = Dispatcher()








@dp.message(F.text=="/start")
async def cmd_start(message: Message):
    await message.delete()
    await message.answer("Добро пожаловать в Anus Casino", reply_markup=main_menu)

#Меню депа
@dp.callback_query(F.data == "btn_dep")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Меню пополнения ")
    await callback.message.edit_text("Меню Пополнения",reply_markup=dodep_menu)



#Возврат в меню 
@dp.callback_query(F.data == "btn_menu")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Назад в меню")
    await callback.message.edit_text("Главное меню Anus 777",reply_markup=main_menu)
    
@dp.callback_query(F.data == "btn_menu_from_img")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Назад в меню")
    await callback.message.delete()
    await callback.message.answer("Главное меню Anus 777",reply_markup=main_menu)
    

#Оплата SBP
@dp.callback_query(F.data == "btn_sbp")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Оплата SBP")
    media = InputMediaPhoto(media=FSInputFile(path=f"img/sbp.png"), caption="Отсканируйте QR-код для оплаты по SBP")
    await callback.message.edit_media(media, reply_markup=dodep_menu_img)


#Оплата visa
@dp.callback_query(F.data == "btn_visa")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Оплата visa")
    media = InputMediaPhoto(media=FSInputFile(path=f"img/visa.png"), caption="ВЕРНИ МАМИНУ КАРТОЧКУ! ")
    await callback.message.edit_media(media, reply_markup=dodep_menu_img)

#Оплата TRC-20
@dp.callback_query(F.data == "btn_crypto")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Оплата TRC-20")
    await callback.message.edit_text("Кошелек для перевода: 8708010020:AAEVwKYRfRu3ZGawJZs4oAyuxTIT963a2EY ", reply_markup=dodep_menu_img)


#Вывод

@dp.callback_query(F.data == "btn_w")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Меню Вывода ")
    await callback.message.edit_text("Меню Вывода",reply_markup=withdraw_menu)

@dp.callback_query(F.data == "btn_steam_w")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Вывод в Steam")
    media = InputMediaPhoto(media=FSInputFile(path=f"img/w.png"), caption="Вывод в процессе, пожалуйста ожидайте")
    await callback.message.edit_media(media, reply_markup=withdraw_menu_img)

@dp.callback_query(F.data == "btn_visa_w")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Вывод по реквезитам")
    media = InputMediaPhoto(media=FSInputFile(path=f"img/w.png"), caption="Вывод в процессе, пожалуйста ожидайте")
    await callback.message.edit_media(media, reply_markup=withdraw_menu_img)
    
@dp.callback_query(F.data == "btn_trc_w")
async def handle_btn1(callback: CallbackQuery):
    await callback.answer("Вывод TRC-20")
    media = InputMediaPhoto(media=FSInputFile(path=f"img/w.png"), caption="Вывод в процессе, пожалуйста ожидайте")
    await callback.message.edit_media(media, reply_markup=withdraw_menu_img)







async def main():
    bot = Bot(token=tg_bot_token)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

    