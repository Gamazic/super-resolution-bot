from project.bot.loader import dp
from project.celery_task_app.tasks import super_resolution_image_task
from project.utils import get_photo_file_path


@dp.message_handler(commands=['start', 'help'])
async def start(message):
    welcome_message = "Привет!"
    await message.answer(welcome_message)


@dp.message_handler(commands=['super-res'])
async def super_res(message):
    answer_message = "Принято!"
    await message.answer(answer_message)
    image = message.chat.id
    super_resolution_image_task.delay(image, image)


@dp.message_handler(content_types=['photo'])
async def get_photo(message):
    photo_info = message.photo[0]
    chat_id = message.chat.id
    photo_id = photo_info.file_unique_id
    photo_file_path = get_photo_file_path(photo_id, chat_id)
    await photo_info.download(photo_file_path)
    super_resolution_image_task.delay(photo_id, chat_id)
