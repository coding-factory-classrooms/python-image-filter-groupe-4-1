import cv2
import numpy as np


class Dilation:

    def dilate_file(self, img, intensity):
        kernel = np.ones((20, 20), np.uint8)
        return cv2.dilate(img, kernel, iterations=intensity)
