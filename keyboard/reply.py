from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import emoji

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🏠 Главная страница 🏠')],
        [KeyboardButton(text='🧺 Каталог товаров 🧺')],
        [KeyboardButton(text='📦 Варианты доставки 📦')],
        [KeyboardButton(text='💰 Варианты оплаты 💰')],
        [KeyboardButton(text='🍀 О магазине 🍀')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Что вас интересует?',
    selective=False,
    row_width=2
)


