import cv2
import numpy as np


class Dilation:

    def dilate_file(self, filepath):
        img = cv2.imread(filepath, 0)
        kernel = np.ones((5, 5), np.uint8)
        img_dilation = cv2.dilate(img, kernel, iterations=1)
        cv2.imwrite(f'data/processed_images/test.jpg', img_dilation)