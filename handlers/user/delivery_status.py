
from aiogram.types import Message
from loader import dp, db
from .menu import delivery_status
from filters import IsUser
import logging
from aiogram.types import Message, CallbackQuery
from keyboards.inline.categories import categories_markup, category_cb
from keyboards.inline.products_from_catalog import product_markup, product_cb
from aiogram.utils.callback_data import CallbackData
from aiogram.types.chat import ChatActions
from loader import dp, db, bot
from filters import IsUser
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Gibt alle Produkte zurück

@dp.message_handler(IsUser(), text=delivery_status)
async def process_delivery_status(message: Message):
    
    await message.answer('Alle Produkte:')
    await show_products(message)

async def show_products(m):
    products = db.fetchall('SELECT idx, title, body, price FROM products WHERE idx NOT IN (SELECT idx FROM cart WHERE cid = ?)', (m.chat.id,))

    if not products:
        await m.answer('Hier ist nichts 😢')
    else:
        await bot.send_chat_action(m.chat.id, ChatActions.TYPING)
        for idx, title, body, price in products:
            markup = InlineKeyboardMarkup().add(InlineKeyboardButton("Mehr Details", callback_data=f"detail_{idx}"))
            #await m.answer(text=f'<b>{title}</b>\n\nPreis: {price}€', reply_markup=markup)
            await m.answer(text=f'<b>{title}</b>\n', reply_markup=markup)
