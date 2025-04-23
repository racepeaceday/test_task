import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command

from app.loader import bot, dp

from app import config

@dp.message(Command(commands=['start']))
async def start_menu_handler(message: Message):
    await message.answer(
        text=
        f'Привет, @{message.from_user.username}!\n\n'
        'Все настройки находятся в <code>config.ini</code>\n'
        'Переменное окружение - <code>app/config.py</code>\n'
        'Сам скрипт <code>~/script.py</code>'
    )