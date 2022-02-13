from project.bot.loader import dp
from project.celery_task_app.tasks import super_resolution_image_task
from project.utils import get_photo_file_path
from project.bot.messages import WELCOME_MESSAGE, GOT_PHOTO_MESSAGE


@dp.message_handler(commands=['start', 'help'])
async def start(message):
    await message.answer(WELCOME_MESSAGE)


@dp.message_handler(content_types=['photo'])
async def get_photo_and_delay_super_resolution_task(message):
    photo_info = message.photo[-1]
    chat_id = message.chat.id
    photo_id = photo_info.file_unique_id
    photo_file_path = get_photo_file_path(photo_id, chat_id)
    await photo_info.download(photo_file_path)
    await message.answer(GOT_PHOTO_MESSAGE)
    super_resolution_image_task.delay(photo_id, chat_id)
