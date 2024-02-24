
from aiogram.types import Message
from loader import dp, db
from handlers.user.menu import orders
from filters import IsAdmin

@dp.message_handler(IsAdmin(), text=orders)
async def process_orders(message: Message):
    
    orders = db.fetchall('SELECT * FROM orders')
    
    if len(orders) == 0: await message.answer('Sie haben keine Bestellungen.')
    else: await order_answer(message, orders)

async def order_answer(message, orders):

    res = ''

    for order in orders:
        res += f'Bestellung <b>Nr. {order[3]}</b>\n\n'

    await message.answer(res)
