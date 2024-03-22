from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Главная страница')],
        [KeyboardButton(text='О магазине')],
        [KeyboardButton(text='Варианты доставки'), KeyboardButton(text='Варианты оплаты')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Что вас интересует?',
    selective=False,
    row_width=2
)

