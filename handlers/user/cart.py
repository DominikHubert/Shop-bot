
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from filters import IsUser
from .menu import cart
from aiogram.types import InputFile

from keyboards.inline.categories import product_markup, category_cb

# test card ==> 1111 1111 1111 1026, 12/22, CVC 000

# shopId 506751

# shopArticleId 538350


@dp.message_handler(IsUser(), text=cart)
async def process_balance(message: Message, state: FSMContext):
    await message.answer('⁠Lerne mehr über Zinzino')
    #markup = ReplyKeyboardMarkup(resize_keyboard=True)
    photo_path = 'data/assets/Gruender.jpg'
    photo = InputFile(photo_path)
    welcome_message = f'Seit 2005 stellen wir den Status Quo in Frage\n' \
                f'Zinzino ist aus dem Wunsch nach neuen Denkweisen entstanden. Das Gründerpaar Hilde und Ørjan Sæle wollte zurück zu ihren Wurzeln, ihrer Leidenschaft für das Teilen großartiger Produkterfahrungen. Es wurde ihre Mission, den Direktvertrieb wieder kundenzentriert zu gestalten. Ein gewagter Schritt, der Zinzino an die vorderste Front für test-basierte, personalisierte Ernährungsmittel katapultierte. \n' \
                f'Inzwischen hat es Zinzino von einem kleinen skandinavischen Start-up zu einem der an der Nasdaq First North am schnellsten wachsenden Direktvertriebsunternehmen im Gesundheits- und Wellness-Bereich gebracht, wo es nach wie vor den Status Quo herausfordert. Dabei steht der Kunde stets im Mittelpunkt.'
    await message.answer_photo(photo=photo, caption="Hilde und Ørjan Sæle, Gründer von Zinzino")
    await message.answer(welcome_message)
    
