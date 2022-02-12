from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from project.bot.config import TG_TOKEN

bot = Bot(TG_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
