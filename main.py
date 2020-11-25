from filters.blur import Blur
from filters.black_and_white import BlackAndWhite
from filters.dilation import Dilation

dilate = Dilation()

dilate.dilate_dir('data/images/')
