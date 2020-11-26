import cv2
import numpy as np
from logger.logger import Logger


class Dilation:

    def dilate_file(self, img, intensity):
        """
        Apply a dilation filter to the image
        :param img: The image path
        :param intensity: The intensity of the filter
        :return:
        """
        logger = Logger()
        kernel = np.ones((20, 20), np.uint8)
        logger.log(" Applying dilation filter...")
        return cv2.dilate(img, kernel, iterations=intensity)
