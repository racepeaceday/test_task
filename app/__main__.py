import asyncio

from aiogram import Dispatcher

from app import utils, config
from app.loader import dp, bot

from app import handlers

if __name__ == '__main__':
    utils.setup_logger("INFO", ["aiogram.bot.api"])

    asyncio.run(dp.start_polling(bot))