from aiogram import F, types, Router
from aiogram.filters import or_f, CommandStart, Command
from filters.chat_types import ChatTypeFilter

from keyboard import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("_Привет, я виртуальный помошник_", reply_markup=reply.builder_keyboard_.as_markup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder='Что вас интересует?',
        selective=False,
    ), parse_mode="Markdown")


@user_private_router.message(or_f(Command('menu'), F.text.lower().contains('меню')))
async def menu_cmd(message: types.Message):
    await message.answer('Главная страница:')


@user_private_router.message(or_f(Command('market'), F.text.lower().contains('каталог товаров')))
async def market_cmd(message: types.Message):
    await message.answer('Каталог товаров:')


@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'вариант доставки'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    await message.answer('Варианты доставки:')


@user_private_router.message(or_f(Command('payment'), F.text.lower().contains('варианты оплаты')))
async def payment_cmd(message: types.Message):
    await message.answer('Варианты оплаты:')


@user_private_router.message(or_f(Command('about'), F.text.lower().contains('о магазине')))
async def status_cmd(message: types.Message):
    await message.answer('О магазине:')


@user_private_router.message(or_f(Command('contact'), F.text.lower().contains('о магазине')))
async def get_contact(message: types.Message):
    await message.answer(f"Данные получены", reply_markup=reply.request_keyboard)
    await message.answer(str(message.contact))
