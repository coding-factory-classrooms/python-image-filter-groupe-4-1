
import cv2
import numpy as np
import os
from datetime import datetime


class Blur:
    output_file = "data/output/"

    def blur_image(self, filename):
        """
        Blur the image
        :return:
        """
        # Get the current date and time
        now = datetime.now()
        # Format date
        timestamp = now.strftime("%Y-%m-%d%H-%M-%S")

        # Load the input image
        original_data_image = cv2.imread(filename)

        copy_image = np.copy(original_data_image)
        # Blur the image with gaussian filter
        gaussian_blur = cv2.GaussianBlur(copy_image, (7, 7), 0)
        cv2.imshow("Guassian blur", gaussian_blur)
        if not os.path.exists(self.output_file):
            os.makedirs(self.output_file)
        new_path = f"{self.output_file}blured-image-{timestamp}.jpg"
        cv2.imwrite(new_path, gaussian_blur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return
