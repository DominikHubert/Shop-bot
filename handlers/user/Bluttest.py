import logging
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.products_from_cart import product_markup, product_cb
from aiogram.utils.callback_data import CallbackData
from keyboards.default.markups import *
from aiogram.types.chat import ChatActions
from states import CheckoutState
from loader import dp, db, bot
from filters import IsUser
from .menu import Bluttest


@dp.message_handler(IsUser(), text=Bluttest)
async def process_delivery_status(message: Message):
    
    await message.answer('Bluttest:')
    await show_products(message)

async def show_products(m):
    products = db.fetchall('''
SELECT idx, title, body, price 
FROM products 
WHERE idx NOT IN (
    SELECT idx 
    FROM cart 
    WHERE cid = ?
) 
AND tag LIKE '%Bluttest%'
''', (m.chat.id,))

    if not products:
        await m.answer('Hier ist nichts 😢')
    else:
        await bot.send_chat_action(m.chat.id, ChatActions.TYPING)
        for idx, title, body, price in products:
            markup = InlineKeyboardMarkup().add(InlineKeyboardButton("Mehr Details", callback_data=f"detail_{idx}"))
            #await m.answer(text=f'<b>{title}</b>\n\nPreis: {price}€', reply_markup=markup)
            await m.answer(text=f'<b>{title}</b>\n', reply_markup=markup)