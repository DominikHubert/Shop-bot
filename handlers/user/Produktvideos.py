import logging
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.products_from_cart import product_markup, product_cb
from aiogram.utils.callback_data import CallbackData
from keyboards.default.markups import *
from aiogram.types.chat import ChatActions
from states import CheckoutState
from loader import dp, db, bot
from filters import IsUser
from .menu import Produktvideos, catalog


@dp.message_handler(IsUser(), text=Produktvideos)
async def process_balance(message: Message, state: FSMContext):
    
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add("Produktvideos","Vorträge")
    markup.add(catalog)
    await message.answer('Wähle', reply_markup=markup)

    produkt_videos = f'Links zu den Produktvideos : (du kannst sie hier herunterladen) \n\nBalance Oil Tutti Frutti: https://www.zinzino.tv/videos/d39ed8b61c1aeccf5a/balanceoil-tutti-frutti\n\n' \
                 f'BalanceOil+ Premium: https://www.zinzino.tv/videos/799ddeb71b16eec0f0/balanceoil-premium\n\n' \
                 f'R.E.V.O.O Oliveoil: https://www.zinzino.tv/videos/119cd7b91912ecca98/r-e-v-o-o-oliveoil-launch\n\n' \
                 f'BalanceOil Vegan: https://www.zinzino.tv/videos/4c9ad1b91617e3c3c4/balanceoil-vegan-de\n\n' \
                 f'BalanceOil AquaX: https://www.zinzino.tv/videos/489bdfb21e1eecccc0/balanceoil-aquax\n\n' \
                 f'Wie man den BalanceTest durchführt: https://www.zinzino.tv/videos/d39eddb01610e0c05a/how-to-take-the-balancetest-de\n\n' \
                 f'LeanShake with Dr. Paul Clayton: https://www.zinzino.tv/videos/d49adabe101ae3c25c/leanshake-with-dr-paul-clayton-de\n\n' \
                 f'Health Protocol Concept: https://www.zinzino.tv/videos/ac9fdeb01b1ee7c525/health-protocol-concept-de\n\n' \
                 f'How to take the Vitamin D Test: https://www.zinzino.tv/videos/119eddb01616e8c498/zinzino-vitamind-test-instructional-video-tt_dede-mp4\n\n' \
                 f'Zinzino HbA1c Test & Lifestyle Assessment: https://www.zinzino.tv/videos/799ed4b4101fe2c4f0/zinzino-hba1c-test-lifestyle-assessment-de'
    

@dp.message_handler(IsUser(), text="Produktvideos")
async def process_infos(message: Message):
    produkt_videos_de = f'Links zu den Produktvideos :\n\n' \
                 f'<b>Balance Öl Tutti Frutti</b>: https://www.zinzino.tv/videos/d39ed8b61c1aeccf5a/balanceoil-tutti-frutti\n\n' \
                 f'<b>BalanceÖl+ Premium</b>: https://www.zinzino.tv/videos/799ddeb71b16eec0f0/balanceoil-premium\n\n' \
                 f'<b>R.E.V.O.O Olivenöl</b>: https://www.zinzino.tv/videos/119cd7b91912ecca98/r-e-v-o-o-oliveoil-launch\n\n' \
                 f'<b>Balance Öl Vegan</b>: https://www.zinzino.tv/videos/4c9ad1b91617e3c3c4/balanceoil-vegan-de\n\n' \
                 f'<b>Balanc Öl AquaX</b>: https://www.zinzino.tv/videos/489bdfb21e1eecccc0/balanceoil-aquax\n\n' \
                 f'<b>Wie man den BalanceTest durchführt</b>: https://www.zinzino.tv/videos/d39eddb01610e0c05a/how-to-take-the-balancetest-de\n\n' \
                 f'<b>LeanShake mit Dr. Paul Clayton</b>: https://www.zinzino.tv/videos/d49adabe101ae3c25c/leanshake-with-dr-paul-clayton-de\n\n' \
                 f'<b>Gesundheitsprotokoll Konzept</b>: https://www.zinzino.tv/videos/ac9fdeb01b1ee7c525/health-protocol-concept-de\n\n' \
                 f'<b>Wie man den Vitamin-D-Test durchführt</b>: https://www.zinzino.tv/videos/119eddb01616e8c498/zinzino-vitamind-test-instructional-video-tt_dede-mp4\n\n' \
                 f'<b>Zinzino HbA1c-Test & Lifestyle-Bewertung</b>: https://www.zinzino.tv/videos/799ed4b4101fe2c4f0/zinzino-hba1c-test-lifestyle-assessment-de'
    
    await message.answer(produkt_videos_de)

@dp.message_handler(IsUser(), text="Vorträge")
async def process_infos(message: Message):
    vortaege = f'Links zu den Vorträgen :\n\n' \
                 f'<b>Schwangerschaft</b>: https://www.youtube.com/watch?v=Hx_Du7rA_HM\n\n' \
                 f'<b>Nerven, Gehirn, Psyche, Verhalten</b>: https://www.youtube.com/watch?v=6xWSDa_IIJ8\n\n' \
                 f'<b>Sport</b>: https://www.youtube.com/watch?v=E0dHKjltjX0\n\n' \
                 f'<b>Vitamine, Mineralien, Mikro- und Makrostoffe allgemein</b>: https://www.youtube.com/watch?v=eaUgUlR-g00\n\n' \
                 f'<b>Innere Organe & Organsysteme und ihre Erkrankungen</b>: https://www.youtube.com/watch?v=AcPv9CJO8TI\n\n' \
                 f'<b>Haut & Haare</b>: https://www.canva.com/design/DAF6nww9jHI/BScaFEJWHyWv5_F-9H0APg/view?utm_content=DAF6nww9jHI&utm_campaign=designshare&utm_medium=link&utm_source=editor\n\n' \
                 f'<b>TCM und das Gesundheitsprotokoll</b>: https://www.youtube.com/watch?v=2Ttc7TetPpY\n\n' \
                 f'<b>Vitamin D</b>: https://www.youtube.com/watch?v=xhB-3DZapt0\n\n' \
                 f'<b>Detox</b>: https://www.youtube.com/watch?v=8XknJoa90E8\n\n' \
                 f'<b>Kundenpräsentation</b>: https://www.youtube.com/watch?v=WVsEZ--3fVI \n\n'

                 
    await message.answer(vortaege)