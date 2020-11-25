from filters.filters import Filters
import glob


filter = Filters()


dir_path = "data/images/"

for filepath in glob.glob(f'{dir_path}*'):
    try:
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
            filter.filter(filepath, 'dilate')
    except Exception as e:
        print(f'Please make sure your directory is correct, \nerror : {e}')

