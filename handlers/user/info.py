
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from filters import IsUser
from .menu import info

from keyboards.inline.categories import product_markup, category_cb

# test card ==> 1111 1111 1111 1026, 12/22, CVC 000

# shopId 506751

# shopArticleId 538350

'''
@dp.message_handler(IsUser(), text=cart)
async def process_balance(message: Message, state: FSMContext):
    await message.answer('⁠Lerne mehr über Zinzino')
'''
