import cv2
from logger.logger import Logger


class FilterZeTeam:

    def put_text(self, img):
        """
        Apply a put text filter
        :param img: the image to apply the filter
        :return: return the filtered image
        """
        logger = Logger()
        logger.log(" Applying FilterZeTeam filter...")
        return cv2.putText(img, 'Moise, Lucas & Kevin', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 0, 255), 2, cv2.LINE_AA)