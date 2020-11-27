from filters.read_write_file import ReadWrite
from filters.blur import Blur
from filters.black_and_white import BlackAndWhite
from filters.dilation import Dilation
from filters.filter_ze_team import FilterZeTeam


class Filters:

    def filter(self, file_path, filter_type, output_directory):
        """
        Filter method
        :param output_directory: The directory where filtered image are stored
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
                img = black_white.grayscale(img)
            elif t.startswith('filterzeteam'):
                filter_ze_team = FilterZeTeam()
                img = filter_ze_team.put_text(img)
        read_write.write_file(file_path, img, output_directory)
