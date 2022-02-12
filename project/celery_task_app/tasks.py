from PIL import Image
from celery import Task


from project.bot.sync_handlers import bot_send_photo_sync
from project.utils import get_photo_file_path, convert_image_to_bytes_io
from project.celery_task_app.worker import celery_app


class SuperResolutionTask(Task):
    abstract = True

    def __init__(self):
        super().__init__()
        from project.ml_model.loader import inference_module
        self.inference_module = inference_module


@celery_app.task(bind=True,
                 base=SuperResolutionTask)
def super_resolution_image_task(self, photo_id, chat_id):
    inference_module = self.inference_module
    photo_file_path = get_photo_file_path(photo_id, chat_id)
    image = Image.open(photo_file_path)
    super_image = inference_module.predict(image)
    bytes_io_image = convert_image_to_bytes_io(super_image)
    bot_send_photo_sync(chat_id, photo=bytes_io_image)
