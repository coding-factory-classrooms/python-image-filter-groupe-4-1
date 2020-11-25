import cv2
import numpy as np
import os
import glob
from filters.read_write_file import ReadWrite



class Dilation:
    output_file = "data/output/"

    def dilate_file(self, filepath, filter):
        read_write = ReadWrite()
        img = read_write.read_file(filepath)
        kernel = np.ones((20, 20), np.uint8)
        output_image = ""
        if filter == 'dilate':
            output_image = cv2.dilate(img, kernel, iterations=1)
        elif filter == 'blur':
            output_image = cv2.GaussianBlur(img, (7, 7), 0)
        elif filter == 'black_and_white':
            output_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        read_write.write_file(filepath, output_image)
