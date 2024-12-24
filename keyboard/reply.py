from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType,
                           KeyboardButtonRequestUser, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import emoji

import keyboard.reply

request_keyboard = InlineKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Ваши контактные данные', request_poll=KeyboardButtonPollType())],
        [KeyboardButton(text='Номер телефона ☎️', request_contact=True)],
        [KeyboardButton(text='Локация 🌍', request_location=True)],
        [KeyboardButton(text='@tg 🛩️')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Напишите ваши данные?',
    selective=False,
    row_width=2
)

delete_keyboard = ReplyKeyboardRemove()

builder_keyboard = ReplyKeyboardBuilder()
builder_keyboard.add(
    KeyboardButton(text='📁 Меню 📁'),
    KeyboardButton(text='🛍️ Каталог товаров 🛍️'),
    KeyboardButton(text='📦 Варианты доставки 📦'),
    KeyboardButton(text='💰 Варианты оплаты 💰'),
    KeyboardButton(text='🍀 О магазине 🍀'),
    KeyboardButton(text=' Опрос ', request_poll=KeyboardButtonPollType()),
)
builder_keyboard.adjust(1, 1, 1, 1, 1)

builder_keyboard_ = ReplyKeyboardBuilder()
builder_keyboard_.attach(builder_keyboard)
builder_keyboard_.row(KeyboardButton(text='Вызвать помошника ИИ'), )
