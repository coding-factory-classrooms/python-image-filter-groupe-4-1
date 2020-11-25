import cv2
import numpy as np


class Dilation:

    def dilate_file(self, img):
        kernel = np.ones((20, 20), np.uint8)
        return cv2.dilate(img, kernel, iterations=1)
