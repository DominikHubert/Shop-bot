import os
import handlers
from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from data import config
from loader import dp, db, bot
import filters
import logging

filters.setup(dp)

WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.environ.get("PORT", 5000))
user_message = 'Benutzer'  # Übersetzt von 'Пользователь'
admin_message = 'Admin'  # Übersetzt von 'Админ'
catalog = '🛍️ Katalog'
delivery_status = '🚚 Alle Produkte'


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    #markup.row(user_message, admin_message)
    markup.row(user_message)
    if message.chat.id == 409300245:
        markup.row(admin_message)

    await message.answer('''Hallo! 👋

🤖 Ich bin ein Shop-Bot für den Verkauf von Produkten jeder Kategorie.
    
🛍️ Um zum Katalog zu gelangen und die gewünschten Produkte auszuwählen, verwenden Sie den Befehl /menu.

💰 Das Konto kann über Yandex.Kasse, Sberbank oder Qiwi aufgeladen werden.

❓ Fragen? Kein Problem! Das Kommando /sos hilft, sich mit den Administratoren in Verbindung zu setzen, die versuchen werden, so schnell wie möglich zu antworten.

🤝 Einen ähnlichen Bot bestellen? Kontaktieren Sie den Entwickler <a href="https://t.me/NikolaySimakov">Nikolay Simakov</a>, er beißt nicht)))''', reply_markup=markup)


@dp.message_handler(text=user_message)
async def user_mode(message: types.Message):

    cid = message.chat.id
    if cid in config.ADMINS:
        config.ADMINS.remove(cid)

    await message.answer('Benutzermodus aktiviert.', reply_markup=ReplyKeyboardRemove())
    
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(catalog)
        #markup.add(balance, cart)
    markup.add(delivery_status)

    await message.answer('Menü', reply_markup=markup)


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