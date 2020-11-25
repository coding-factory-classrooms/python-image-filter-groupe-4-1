import cv2


class BlackAndWhite:

    def black_and_white_filter(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
