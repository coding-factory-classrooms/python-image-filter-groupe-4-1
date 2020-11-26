from filters.filters import Filters
import glob
import argparse
from logger.logger import Logger

filters = Filters()

parser = argparse.ArgumentParser(description='Filter a directory of images')

# Required arguments
arguments = parser.add_argument_group("arguments")
arguments.add_argument('-i', '--input', type=str, metavar='', required=False, help='Input directory')
arguments.add_argument('-o', '--output', type=str, metavar='', required=False, help='Output directory')
arguments.add_argument('-f', '--filters', type=str, metavar='', required=False, help='Apply Filters to output directory')

# Optional arguments
optional_arguments = parser.add_argument_group("optionals")
optional_arguments.add_argument('-l', '--log', action="store_true", required=False, help="Show logs and exit")

# Parsing args
args = parser.parse_args()


def filter_directory(input_dir, filter_type, output_directory):
    for filepath in glob.glob(f'{input_dir}*'):
        try:
            if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
                filters.filter(filepath, filter_type, output_directory)
        except Exception as e:
            print(f'Please make sure your directory is correct, \nerror : {e}')


if __name__ == '__main__':
    filter_directory(args.input, args.filters, args.output)
    if args.log:
        logger = Logger()
        logger.dump_log()
