import os
import cv2

class ReadWrite:
    output_image = ""

    def read_file(self, filepath):
        return cv2.imread(filepath)

    def write_file(self, filepath, output_image):
        file_name = os.path.basename(filepath)
        return cv2.imwrite(f'data/output/{file_name}', output_image)
