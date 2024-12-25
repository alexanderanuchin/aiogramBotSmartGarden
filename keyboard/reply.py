from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType,
                           KeyboardButtonRequestUser, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import emoji

import keyboard.reply

# Исправленный InlineKeyboardMarkup
request_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Ваши контактные данные', callback_data='request_poll')],
        [InlineKeyboardButton(text='Номер телефона ☎️', callback_data='request_contact')],
        [InlineKeyboardButton(text='Локация 🌍', callback_data='request_location')],
        [InlineKeyboardButton(text='@tg 🛩️', url='https://t.me/')]
    ]
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
builder_keyboard_.row(KeyboardButton(text='Вызвать помощника ИИ'))
