import cv2


class Blur:

    def blur_image(self, img, intensity):
        """
        :param intensity:
        :param img: The image path
        :return:
        """
        # Blur the image with gaussian filter
        return cv2.GaussianBlur(img, (intensity, intensity), 0)
