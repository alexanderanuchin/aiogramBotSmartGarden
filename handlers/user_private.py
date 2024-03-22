from aiogram import F, types, Router
from aiogram.filters import or_f, CommandStart, Command
from filters.chat_types import ChatTypeFilter

from keyboard import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("_Привет, я виртуальный помошник_", reply_markup=reply.start_keyboard, parse_mode="Markdown")


@user_private_router.message(or_f(Command('homepage'), F.text.lower().contains('главная страница')))
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
