
from aiogram import executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from handlers.user.states import OrderState
from loader import dp
from filters import IsAdmin, IsUser

catalog = '🛍️ Katalog'
balance = '🪙 Allgemeine Informationen über Omega3 & Krankheiten'
cart = '📚 ⁠Lerne mehr über Zinzino'
delivery_status = '🚚 Alle Produkte'
Kundenfeedback = '📝 Kundenfeedback'
Bluttest = '🧪 Bluttest'
Feedback = '📦 Reflexionsbogen'
Produktvideos = '🎥 Produktvideos'
info = '📞 Kundenservice'


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
    markup.add(delivery_status, cart)
    
    markup.add(Kundenfeedback, Bluttest)
    markup.add(Feedback, Produktvideos)
    markup.add(balance)

    await message.answer('Menü', reply_markup=markup)



    


