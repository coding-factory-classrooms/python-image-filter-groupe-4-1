
import cv2
import numpy as np


class Dilation:

    output_file = "../data/images/ouput/"

    def __init__(self, filename):
        """
        :param filename: The file to be dilated
        """
        self.filename = filename

    def dilate_image(self):
        # Load the input image
        original_data_image = cv2.imread(self.filename)

        # dilating the image with gaussian
        gaussian_blur = cv2.GaussianBlur(original_data_image, (7, 7), 0)
        cv2.imshow("Gaussian blur", gaussian_blur)
        #cv2.imwrite(self.output_file)
        cv2.waitKey(0)
        return

