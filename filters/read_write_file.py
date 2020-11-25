import os
import cv2


class ReadWrite:

    # The output directory
    output_directory = "data/output/"

    def read_file(self, filepath):
        """
        :param filepath:
        :return:
        """
        return cv2.imread(filepath)

    def write_file(self, filepath, output_image):
        """
        Write the filter file in output directory
        :param filepath: The file path
        :param output_image: Filtered file / image
        :return:
        """
        file_name = os.path.basename(filepath)
        # Verify if the directory don't exist
        if not os.path.exists(self.output_directory):
            # Create the directory if not exist
            os.makedirs(self.output_directory)
        return cv2.imwrite(f'{self.output_directory}{file_name}', output_image)
