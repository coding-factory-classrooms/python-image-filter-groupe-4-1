from filters.read_write_file import ReadWrite
from filters.blur import Blur
from filters.black_and_white import BlackAndWhite
from filters.dilation import Dilation


class Filters:

    def filter(self, file_path, filter_type, output_directory):
        """
        Filter method
        :param output_directory:
        :param file_path: The file path
        :param filter_type: The type of filter to apply " dilate, blur or black_and_white "
        :return:
        """
        read_write = ReadWrite()
        img = read_write.read_file(file_path)
        table = filter_type.split(",")
        for t in table:
            print(t)
            if t.startswith('dilate'):
                if ":" in t:
                    intensity = t.split(":")[1]
                    dilate = Dilation()
                    img = dilate.dilate_file(img, int(intensity))
            elif t.startswith('blur'):
                if ":" in t:
                    intensity = t.split(":")[1]
                    blur = Blur()
                    img = blur.blur_image(img, int(intensity))
            elif t.startswith('grayscale'):
                black_white = BlackAndWhite()
                img = black_white.black_and_white_filter(img)
        read_write.write_file(file_path, img, output_directory)
