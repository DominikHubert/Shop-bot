
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from filters import IsUser
from .menu import info

from keyboards.inline.categories import product_markup, category_cb

# test card ==> 1111 1111 1111 1026, 12/22, CVC 000

# shopId 506751

# shopArticleId 538350


@dp.message_handler(IsUser(), text=info)
async def process_balance(message: Message, state: FSMContext):
    text= f'Anrufen oder E-Mail schreiben\n' \
        f'+43 7 205 698 06\n' \
f'customer.at@zinzino.com\n' \
f'Öffnungszeiten 09-17 CET Mo bis Fr\n\n' \
f'Besucht unsere Webseite https://www.zinzino.com/site/at/de-de/uber-uns/kundenservice/'
    await message.answer(text)

