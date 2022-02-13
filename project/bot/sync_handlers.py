import asyncio
from project.bot.loader import bot


def bot_send_photo_sync(*args, **kwargs):
    """aiogram bot wrapper.
    Needed beacause of native celery can't work with async io coro.
    This wrapper get event loop and run `send_photo` coroutine.
    """
    asyncio.get_event_loop().run_until_complete(
        bot.send_photo(*args, **kwargs)
    )
