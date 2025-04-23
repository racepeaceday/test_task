
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from app import config

bot = Bot(
    token=config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode='HTML')
)

dp = Dispatcher(
    bot=bot,
)

__all__ = (
    "bot",
    "dp",
)