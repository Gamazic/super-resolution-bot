from PIL import Image

from project.ml_model.Real_ESRGAN.realesrgan import RealESRGAN
from project.ml_model.config import DEVICE, MODEL_PATH


class InferenceModule:
    """InferenceModule loads a model from a file and
    makes x2 super-resolution image"""
    def __init__(self):
        """
        Loading sber real-ESRGAN scorer
        """
        self.scorer = RealESRGAN(DEVICE)
        self.scorer.load_weights(MODEL_PATH)

    def predict(self, image: Image) -> Image:
        """Makes super resolution image from inpu image.

        Args:
            image (Image): input image

        Returns:
            Image: super resolution image
        """
        super_resolution_image = self.scorer.predict(image)
        return super_resolution_image
