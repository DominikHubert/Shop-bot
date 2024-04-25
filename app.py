#!/usr/bin/env python3
import os
import handlers
from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import config
from loader import dp, db, bot
import filters
import logging
from aiogram.types import InputFile

filters.setup(dp)

WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.environ.get("PORT", 5000))
user_message = 'Klicke hier, um zu beginnen'  # Übersetzt von 'Пользователь'
admin_message = 'Admin'  # Übersetzt von 'Админ'
catalog = '🛍️ Katalog'
balance = '🪙 Allgemeine Informationen über Omega3 & Krankheiten'
cart = '📚 ⁠Lerne mehr über Zinzino'
delivery_status = '🚚 Alle Produkte'
Kundenfeedback = '📝 Kundenfeedback'
Bluttest = '🧪 Bluttest'
Feedback = '📦 Reflexionsbogen'
Produktvideos = '🎥 Produktvideos'
info = '📞 Kundenservice'


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    user_first_name = message.chat.first_name  # Nutzernamen aus der Nachricht extrahieren
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    photo_path = 'data/assets/Gamechanger.png'
    photo = InputFile(photo_path)

    #markup.row(user_message, admin_message) 409300245
    markup.row(user_message)
    if message.chat.id == 409300245:
        markup.row(admin_message)

    # Füge den Namen des Nutzers zur Begrüßungsnachricht hinzu
    welcome_message = f'Hallo {user_first_name}, \n 📢 Dieser Bot enthält detaillierte Informationen über Zinzino Produkte und Bluttests.\n 💡Hier bekommst du auch Informationen über die Inhaltsstoffe und wie du deine Gesundheit unterstützen kannst. \n ✅ Die Informationen werden ständig aktualisiert und ergänzt.'
    await message.answer_photo(photo=photo, reply_markup=markup)
    await message.answer(welcome_message, reply_markup=markup)


@dp.message_handler(text=user_message)
async def user_mode(message: types.Message):

    cid = message.chat.id
    if cid in config.ADMINS:
        config.ADMINS.remove(cid)

    #await message.answer('Wähle aus dem Menü.', reply_markup=ReplyKeyboardRemove())
    
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(catalog)
    #markup.add(balance, cart)
    markup.add(delivery_status, cart)
    
    markup.add(Kundenfeedback, Bluttest)
    markup.add(Feedback, Produktvideos)
    markup.add(balance, info)
    await message.answer('Wähle aus dem Menü.', reply_markup=markup)


"""
@dp.message_handler(text=admin_message)
async def admin_mode(message: types.Message):

    cid = message.chat.id
    if cid not in config.ADMINS:
        config.ADMINS.append(cid)

    await message.answer('Admin-Modus aktiviert.', reply_markup=ReplyKeyboardRemove())

"""
@dp.message_handler(text=admin_message)
async def admin_mode(message: types.Message):
    cid = message.chat.id
    # Stellen Sie sicher, dass die chat.id genau 1111 entspricht
    if cid == 409300245:
        if cid not in config.ADMINS:
            config.ADMINS.append(cid)
            await message.answer('Admin-Modus aktiviert.', reply_markup=ReplyKeyboardRemove())
        else:
            await message.answer('Sie sind bereits im Admin-Modus.', reply_markup=ReplyKeyboardRemove())
    else:
        # Nachricht für Benutzer, die nicht die spezifische chat.id haben
        await message.answer('Zugriff verweigert. Sie haben keine Berechtigung, den Admin-Modus zu aktivieren.', reply_markup=ReplyKeyboardRemove())


async def on_startup(dp):
    logging.basicConfig(level=logging.INFO)
    db.create_tables()

    await bot.delete_webhook()
    await bot.set_webhook(config.WEBHOOK_URL)


async def on_shutdown():
    logging.warning("Shutting down..")
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning("Bot down")


if __name__ == '__main__':

    if "HEROKU" in list(os.environ.keys()):

        executor.start_webhook(
            dispatcher=dp,
            webhook_path=config.WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )

    else:

        executor.start_polling(dp, on_startup=on_startup, skip_updates=False)

    
