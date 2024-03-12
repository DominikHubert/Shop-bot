import io
import logging
from aiogram.types import Message, CallbackQuery
from keyboards.inline.categories import categories_markup, category_cb
from keyboards.inline.products_from_catalog import product_markup, product_cb
from aiogram.utils.callback_data import CallbackData
from aiogram.types.chat import ChatActions
from loader import dp, db, bot
from .menu import catalog, user_menu
from filters import IsUser
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from .menu import cart, Kundenfeedback, Bluttest, Feedback, Produktvideos, delivery_status
from .menu import balance


user_product_map = {}

@dp.message_handler(IsUser(), text=catalog)
async def process_catalog(message: Message):
    await message.answer('Wählen Sie eine Kategorie, um die Produktliste anzuzeigen:',
                         reply_markup=categories_markup())
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(catalog)
    #markup.add(balance, cart)
    markup.add(delivery_status, cart)
    
    markup.add(Kundenfeedback, Bluttest)
    markup.add(Feedback, Produktvideos)
    #markup.add(delivery_status)

    await message.answer('Wähle', reply_markup=markup)


@dp.callback_query_handler(IsUser(), category_cb.filter(action='view'))
async def category_callback_handler(query: CallbackQuery, callback_data: dict):

    category_name = db.fetchone('''SELECT title FROM categories WHERE idx=?''', (callback_data['id'],))
    
    products = db.fetchall('''SELECT * FROM products product
    WHERE product.tag = (SELECT title FROM categories WHERE idx=?) 
    AND product.idx NOT IN (SELECT idx FROM cart WHERE cid = ?)''',
                           (callback_data['id'], query.message.chat.id))

    #await query.answer('Alle verfügbaren Produkte.')
    #await show_products(query.message, products)
    if category_name:
        await show_products(query.message, products, category_name[0])
    else:
        await query.answer('Kategorie nicht vorhanden.', show_alert=True)



@dp.callback_query_handler(IsUser(), product_cb.filter(action='add'))
async def add_product_callback_handler(query: CallbackQuery, callback_data: dict):

    db.query('INSERT INTO cart VALUES (?, ?, 1)',
             (query.message.chat.id, callback_data['id']))

    await query.answer('Produkt zum Warenkorb hinzugefügt!')
    await query.message.delete()

"""
async def show_products(m, products):

    if len(products) == 0:

        await m.answer('Hier ist nichts 😢')

    else:

        await bot.send_chat_action(m.chat.id, ChatActions.TYPING)

        for idx, title, body, image, price, _ in products:

            markup = product_markup(idx, price)
            text = f'<b>{title}</b>\n\n{body}'

            await m.answer_photo(photo=image,
                                 caption=text,
                                 reply_markup=markup)

"""
async def show_products(m, products,category_name=None):
    if not products:
        await m.answer('Hier ist nichts 😢')
    else:
        await bot.send_chat_action(m.chat.id, ChatActions.TYPING)
        #await m.answer('Alle verfügbaren Produkte aus:')
        message_prefix = f'Alle verfügbaren Produkte aus der Kategorie "{category_name}":' if category_name else 'Alle verfügbaren Produkte aus:'
        await m.answer(message_prefix)
        for idx, title, _, _, _, _ in products:
            markup = InlineKeyboardMarkup().add(InlineKeyboardButton("Mehr Details", callback_data=f"detail_{idx}"))
            await m.answer(text=f'<b>{title}</b>', reply_markup=markup)

        
@dp.callback_query_handler(lambda c: c.data.startswith('detail_'))
async def product_detail_callback_handler(query: CallbackQuery):
    product_id = query.data.split('_')[1]  # Extrahiert die ID aus der Callback Data
    product = db.fetchone('SELECT idx, title, body, photo, price FROM products WHERE idx = ?', (product_id,))
    
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add("Info","Bilder", "Benefits")
    markup.add(catalog)
    await query.message.answer('Menü', reply_markup=markup)
    '''
    if product:
        idx, title, body, image, price = product
        markup = product_markup(idx, price)  # Annahme, dass diese Funktion bereits existiert
        #text = f'<b>{title}</b>\n\n{body}\n\nPreis: {price}€'
        text = f'<b>{title}</b>\n\n{body}'
        
        #await query.message.answer_photo(photo=image, caption=text, reply_markup=markup)
        await query.message.answer_photo(photo=image, reply_markup=markup)
        
        await query.message.answer(text=text, reply_markup=markup)
    else:
        await query.answer('Produkt nicht gefunden.', show_alert=True)
    '''
    chat_id = query.message.chat.id
    user_product_map[chat_id] = product_id


    
@dp.message_handler(IsUser(), text="Info")
async def process_infos(message: Message):
    chat_id = message.chat.id

    # Zugriff auf die product_id aus der globalen Variable
    if chat_id in user_product_map:
        product_id = user_product_map[chat_id]
        product = db.fetchone('SELECT idx, title, body, photo, price FROM products WHERE idx = ?', (product_id,))
    
        if product:
            idx, title, body, image, price = product
            markup = product_markup(idx, price)  # Annahme, dass diese Funktion bereits existiert
            #text = f'<b>{title}</b>\n\n{body}\n\nPreis: {price}€'
            text = f'<b>{title}</b>\n\n{body}'
        
            #await query.message.answer_photo(photo=image, caption=text, reply_markup=markup)
        
        
            await message.answer(text=text, reply_markup=markup)
    else:
        await message.answer("Kein Produkt ausgewählt.")
@dp.message_handler(IsUser(), text="Bilder")
async def process_infos(message: Message):
    chat_id = message.chat.id

    # Zugriff auf die product_id aus der globalen Variable
    if chat_id in user_product_map:
        product_id = user_product_map[chat_id]
        product = db.fetchone('SELECT idx, title, body, photo, price FROM products WHERE idx = ?', (product_id,))

    
        if product:
            idx, title, body, image, price = product
            markup = product_markup(idx, price)  # Annahme, dass diese Funktion bereits existiert
            #text = f'<b>{title}</b>\n\n{body}\n\nPreis: {price}€'
            text = f'<b>{title}</b>\n\n{body}'
        
            #await message.answer_photo(photo=image, reply_markup=markup)

            if title == 'Zinzino LeanShake':
                images = db.fetchall('SELECT photo FROM products WHERE title = ?', (title,))
                for image_data in images:
                    photo_bytes = image_data[0]  # Angenommen, image_data[0] enthält die binären Bilddaten
                    if photo_bytes:
                        await message.answer_photo(photo=io.BytesIO(photo_bytes))
            else:
                await message.answer_photo(photo=image, reply_markup=markup)
            #await message.answer(text=text, reply_markup=markup)
    else:
        await message.answer("Kein Produkt ausgewählt.")

@dp.message_handler(IsUser(), text="Benefits")
async def process_infos(message: Message):
    chat_id = message.chat.id

    # Zugriff auf die product_id aus der globalen Variable
    if chat_id in user_product_map:
        product_id = user_product_map[chat_id]
        product = db.fetchone('SELECT idx, title, body, photo, price FROM products WHERE idx = ?', (product_id,))
    
        if product:
            idx, title, body, image, price = product
            markup = product_markup(idx, price)  # Annahme, dass diese Funktion bereits existiert
            text = f'<b>{title}</b>\n\nBenefits: {price}'
            #text = f'<b>{title}</b>\n\n{body}'
        
            #await message.answer_photo(photo=image, reply_markup=markup)
        
        
            await message.answer(text=text, reply_markup=markup)
    else:
        await message.answer("Kein Produkt ausgewählt.")