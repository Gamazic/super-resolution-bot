import asyncio
from project.bot.loader import bot


def bot_send_message_sync(*args, **kwargs):
    asyncio.get_event_loop().run_until_complete(
        bot.send_message(*args, **kwargs)
    )


def bot_send_photo_sync(*args, **kwargs):
    asyncio.get_event_loop().run_until_complete(
        bot.send_photo(*args, **kwargs)
    )
