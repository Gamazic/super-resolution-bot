import time


class InferenceModule:
    def __init__(self, delay):
        self.delay = delay

    def predict(self, image):
        time.sleep(self.delay)
        return image
