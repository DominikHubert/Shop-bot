import logging, re
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
        seen_categories = set()  # Set zum Speichern bereits hinzugefügter Kategorien

        for idx, question, category in products:
            if category not in seen_categories:
                seen_categories.add(category)  # Füge die Kategorie dem Set hinzu
                if category.lower() == "auto":
                    # Spezielle Behandlung für "Auto"
                    callback_data = category_cb2.new(id=idx, action='sell_auto')
                else:
                    callback_data = category_cb2.new(id=idx, action='sell_auto')

                markup.add(InlineKeyboardButton(category, callback_data=callback_data))

        if not markup.inline_keyboard:
            await m.answer('Keine Kategorien verfügbar 😢')
        else:
            await m.answer('Wähle eine Kategorie:', reply_markup=markup)


# Handler für allgemeine Kategorien und den speziellen Fall "Auto"
@dp.callback_query_handler(category_cb2.filter())
async def handle_category_action(query: CallbackQuery, callback_data: dict):
    
    product = db.fetchone('''SELECT question, category FROM questions WHERE idx = ?''', (callback_data['id'],))
    if product:
            question, category = product
            markup = product_markup(category, question)  # Annahme, dass diese Funktion bereits existiert
            #text = f'<b>{category}</b>\n{question}'
            text = f'{question}\n'
            
            if category != '':
                images = db.fetchall('SELECT question FROM questions WHERE category = ?', (category,))
                heading = f'<b>{category}</b>\n'
                await query.message.answer(text=heading)
                for image_data in images:
                    photo_bytes = image_data[0]  # Angenommen, image_data[0] enthält die binären Bilddaten
                    if photo_bytes:
                        if len(photo_bytes) > 1280:
                            # Nachricht in Teile von je maximal 1276 Zeichen teilen und einzeln senden
                            parts = [photo_bytes[i:i+1280] for i in range(0, len(photo_bytes), 1280)]
                            for part in parts:
                                # Text zwischen - und : finden und fett formatieren
                                formatted_part = re.sub(r'-(.*?)-:', r'<b>\1</b>:', part)
                                await query.message.answer(text=formatted_part, parse_mode='HTML')

                        #await query.message.answer(text=photo_bytes)
                        else:
                            await query.message.answer(text=text)
                            
    await query.answer()  # Schließt die CallbackQuery-Interaktion ab