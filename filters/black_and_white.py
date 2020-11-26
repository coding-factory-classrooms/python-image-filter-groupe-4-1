import cv2
from log.logger import Logger


class BlackAndWhite:

    def grayscale(self, img):
        """
        Apply a grayscale filter
        :param img: the image to apply the filter
        :return: return the filtered image
        """
        logger = Logger()
        logger.log(" Applying grayscale filter...")
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
