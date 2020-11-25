
import cv2
import numpy as np
import os


class Blur:
    # The output Directory
    output_file = "data/output/"

    def blur_image(self, image_path):
        """
        :param image_path: The image path
        :return:
        """

        try:
            # Load the input image
            original_data_image = cv2.imread(image_path)

            # Get current filename
            filename = os.path.basename(image_path)
            copy_image = np.copy(original_data_image)

            # Blur the image with gaussian filter
            gaussian_blur = cv2.GaussianBlur(copy_image, (7, 7), 0)
            cv2.imshow("Guassian blur", gaussian_blur)

            if not os.path.exists(self.output_file):
                os.makedirs(self.output_file)
            new_path = f"{self.output_file}{filename}"

            cv2.imwrite(new_path, gaussian_blur)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except FileNotFoundError as e:
            print("Le fichier n'existe pas" + e)

