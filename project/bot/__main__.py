from aiogram import executor

from project.bot.handlers import dp


def start_polling():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    start_polling()
