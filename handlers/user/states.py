from aiogram.dispatcher.filters.state import StatesGroup, State

class OrderState(StatesGroup):
    awaiting_product_selection = State()  # Benutzer wählt ein Produkt
