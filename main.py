# from filters.black_and_white import BlackAndWhite
# from filters.blur import Blur
from filters.dilation import Dilation

dilate = Dilation()

dilate.dilate_file('data/images/zidane.jpg')