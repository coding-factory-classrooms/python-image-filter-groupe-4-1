from filters.black_and_white import BlackAndWhite
from filters.dilation import Dilation
import glob
import os


dilate = Dilation()


dir_path = "data/images/"

for filepath in glob.glob(f'{dir_path}*'):
    try:
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
            dilate.dilate_file(filepath, 'dilate')
    except Exception as e:
        print(f'Please make sure your directory is correct, \nerror : {e}')

