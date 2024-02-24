
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

catalog = '🛍️ Katalog'
balance = '💰 Guthaben'
cart = '🛒 Warenkorb'
delivery_status = '🚚 Alle Produkte'

settings = '⚙️ Katalogeinstellungen'
orders = '🚚 Bestellungen'
questions = '❓ Fragen'

@dp.message_handler(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(settings)
    #markup.add(questions, orders)

    await message.answer('Menü', reply_markup=markup)

@dp.message_handler(IsUser(), commands='menu')
async def user_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(catalog)
    #markup.add(balance, cart)
    markup.add(delivery_status)

    await message.answer('Menü', reply_markup=markup)
