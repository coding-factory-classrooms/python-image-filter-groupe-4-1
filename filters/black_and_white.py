import cv2
import os

class BlackAndWhite:

    def process(self, img_path):
        print(img_path)
        file_name = os.path.basename(img_path)
        print(file_name)
        image = cv2.imread(img_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Original image', image)
        cv2.imshow('Gray image', gray)
        cv2.imwrite(f"data/output/{file_name}", gray)

        cv2.waitKey(0)
        cv2.destroyAllWindows()