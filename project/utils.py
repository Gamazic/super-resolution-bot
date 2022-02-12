import os
from io import BytesIO

PHOTO_DIR = os.environ.get('PHOTO_DIR', 'photos')


def get_photo_file_path(photo_id, chat_id):
    return f'{PHOTO_DIR}/{chat_id}_{photo_id}.jpg'


def convert_image_to_bytes_io(image):
    bytes_io = BytesIO()
    bytes_io.name = 'image.png'
    image.save(bytes_io)
    bytes_io.seek(0)
    return bytes_io
