from filters.read_write_file import ReadWrite
from filters.blur import Blur
from filters.black_and_white import BlackAndWhite
from filters.dilation import Dilation


class Filters:

    def filter(self, file_path, filter_type):
        """
        Filter method
        :param file_path: The file path
        :param filter_type: The type of filter to apply " dilate, blur or black_and_white "
        :return:
        """
        read_write = ReadWrite()
        img = read_write.read_file(file_path)
        output_image = ""
        if filter_type == 'dilate':
            dilate = Dilation()
            output_image = dilate.dilate_file(img)
        elif filter_type == 'blur':
            blur = Blur()
            output_image = blur.blur_image(img)
        elif filter_type == 'black_and_white':
            black_white = BlackAndWhite()
            output_image = black_white.black_and_white_filter(img)
        read_write.write_file(file_path, output_image)
