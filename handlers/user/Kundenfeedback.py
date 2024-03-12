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
from .menu import Kundenfeedback

@dp.message_handler(IsUser(), text=Kundenfeedback)
async def process_delivery_status(message: Message):
    
    await message.answer('Kundenfeedback:')
    await show_products(message)

# Bestehende CallbackData für Kategorien
category_cb2 = CallbackData('category', 'id', 'action')

# Handler für das Anzeigen von Produkten/Fragen
async def show_products(m):
    products = db.fetchall('''
SELECT idx, question, category
FROM questions 
WHERE tag LIKE '%Feedback%'
''')

    if not products:
        await m.answer('Hier ist nichts 😢')
    else:
        markup = InlineKeyboardMarkup()
        for idx, question, category in products:
            # Überprüfen, ob die Kategorie "Auto" ist und eine spezielle callback_data verwenden
            if category.lower() == "auto":
                # Spezielle Behandlung für "Auto"
                callback_data = category_cb2.new(id=idx, action='sell_auto')
            else:
                callback_data = category_cb2.new(id=idx, action='sell_auto')

            markup.add(InlineKeyboardButton(category, callback_data=callback_data))

        await m.answer('Wähle eine Kategorie:', reply_markup=markup)

# Handler für allgemeine Kategorien und den speziellen Fall "Auto"
@dp.callback_query_handler(category_cb2.filter())
async def handle_category_action(query: CallbackQuery, callback_data: dict):
    
    product = db.fetchone('''SELECT question, category FROM questions WHERE idx = ?''', (callback_data['id'],))
    if product:
            question, category = product
            markup = product_markup(category, question)  # Annahme, dass diese Funktion bereits existiert
            text = f'<b>{category}</b>\n{question}'
            await query.message.answer(text=text)
    await query.answer()  # Schließt die CallbackQuery-Interaktion ab