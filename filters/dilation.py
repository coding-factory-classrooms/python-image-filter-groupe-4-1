import cv2
import numpy as np
import os
import glob


class Dilation:

    def dilate_file(self, filepath):
        try:
            img = cv2.imread(filepath)
            file_name = os.path.basename(filepath)
            kernel = np.ones((20, 20), np.uint8)
            img_dilation = cv2.dilate(img, kernel, iterations=1)
            output_file = f'data/output/{file_name}'
            if output_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                cv2.imwrite(f'data/output/{file_name}', img_dilation)
        except Exception as e:
            print(f'Please enter a correct file, \n error : {e}')

    def dilate_dir(self, dir_path):
        for filepath in glob.glob(f'{dir_path}*'):
                try:
                    img = cv2.imread(filepath)
                    file_name = os.path.basename(filepath)
                    kernel = np.ones((20, 20), np.uint8)
                    img_dilation = cv2.dilate(img, kernel, iterations=1)
                    output_file = f'data/output/{file_name}'
                    if output_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                        cv2.imwrite(f'data/output/{file_name}', img_dilation)
                except Exception as e:
                    print(f'Please make sure your directory is correct, \n error : {e}')
