
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp
from filters import IsAdmin, IsUser

catalog = '🛍️ Katalog'
balance = '🪙 Inhaltsstoffe'
cart = '📚 ⁠Lerne mehr über Zinzino'
delivery_status = '🚚 Alle Produkte'
Kundenfeedback = '📝 Kundenfeedback'
Bluttest = '🧪 Bluttest'
Feedback = '📦 Feedback'
Produktvideos = '🎥 Produktvideos'


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
    markup.add(balance, cart)
    markup.add(Kundenfeedback, Bluttest)
    markup.add(Feedback, Produktvideos)
    markup.add(delivery_status)

    await message.answer('Menü', reply_markup=markup)


@dp.message_handler(text=cart)
async def user_menu(message: Message):
#async def user_mode(message: types.Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(balance, cart)

    await message.answer('Menü', reply_markup=markup)