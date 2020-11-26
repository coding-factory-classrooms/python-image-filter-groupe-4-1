import os
import cv2
from logger.logger import Logger


class ReadWrite:
    logger = Logger()

    def read_file(self, filepath):
        """
        :param filepath:
        :return:
        """
        self.logger.log(f"Opening image {filepath}")
        return cv2.imread(filepath)

    def write_file(self, filepath, output_image, output_directory):
        """
        Write the filter file in output directory
        :param output_directory:
        :param filepath: The file path
        :param output_image: Filtered file / image
        :return:
        """
        file_name = os.path.basename(filepath)
        # Verify if the directory don't exist
        if not os.path.exists(output_directory):
            # Create the directory if not exist
            os.makedirs(output_directory)

        self.logger.log(f"Saving result image {output_directory}{file_name}")
        return cv2.imwrite(f'{output_directory}{file_name}', output_image)
