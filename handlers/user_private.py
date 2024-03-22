from aiogram import F, types, Router
from aiogram.filters import or_f, CommandStart, Command
from filters.chat_types import ChatTypeFilter

from keyboard import reply


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет, я виртуальный помошник', reply_markup=reply.start_keyboard)


@user_private_router.message(or_f(Command('Homepage'), (F.text.lower() == 'Главная страница')))
async def menu_cmd(message: types.Message):
    await message.answer('Главная страница:')


@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def status_cmd(message: types.Message):
    await message.answer('О нас:')


@user_private_router.message(F.text.lower() == 'варианты оплаты')
@user_private_router.message(Command('payment'))
async def login_cmd(message: types.Message):
    await message.answer('Варианты оплаты:')


@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'вариант доставки'))
@user_private_router.message(Command('shipping'))
async def help_cmd(message: types.Message):
    await message.answer('Варианты доставки:')
