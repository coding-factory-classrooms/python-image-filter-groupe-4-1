import cv2
from logger.logger import Logger


class Blur:

    def blur_image(self, img, intensity):
        """
        Apply a blur filter to the image
        :param intensity: The intensity of the filter
        :param img: The image path
        :return:
        """
        if intensity % 2 == False:
            intensity += 1
        log = Logger()
        log.log(" Applying a blur filter...")
        # Blur the image with gaussian filter
        return cv2.GaussianBlur(img, (intensity, intensity), 0)
