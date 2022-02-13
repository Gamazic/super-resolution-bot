from PIL import Image
from celery import Task

from project.bot.sync_handlers import bot_send_photo_sync
from project.utils import get_photo_file_path, convert_image_to_bytes_io
from project.celery_task_app.worker import celery_app


class SuperResolutionTask(Task):
    def __init__(self):
        super().__init__()
        self.inference_module = None

    def __call__(self, *args, **kwargs):
        """
        Load model on first call (i.e. first task processed)
        Avoids the need to load model on each task request
        """
        if self.inference_module is None:
            from project.ml_model.loader import inference_module
            self.inference_module = inference_module
        return self.run(*args, **kwargs)


@celery_app.task(ignore_result=True,
                 bind=True,
                 base=SuperResolutionTask)
def super_resolution_image_task(self, photo_id: str, chat_id: str):
    """Celery task which read image, calls super-res model predict and
    send super resolution image to user.
    Each task is queued and waits for execution in the order of the queue.

    Args:
        photo_id (str): id of photo that user sent
        chat_id (str): id of user which sent photo
    """
    photo_file_path = get_photo_file_path(photo_id, chat_id)
    image = Image.open(photo_file_path).convert('RGB')
    super_image = self.inference_module.predict(image)
    bytes_io_image = convert_image_to_bytes_io(super_image)
    bot_send_photo_sync(chat_id, photo=bytes_io_image)
