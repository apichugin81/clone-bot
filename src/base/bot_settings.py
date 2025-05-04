from os import getenv

from aiogram import Bot, Dispatcher, types, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
# from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.constants import API_TOKEN

# bot = Bot(token=API_TOKEN)
# For example use simple MemoryStorage for Dispatcher.
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)

TOKEN = getenv(API_TOKEN)

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))

router = Router()
dp = Dispatcher()
dp.include_router(router)

