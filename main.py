from filters.filters import Filters
import glob
import sys
import argparse

filters = Filters()

parser = argparse.ArgumentParser(description='Filter a directory of images')
parser.add_argument('-i', '--input', type=str, metavar='', required=True, help='Input directory')
parser.add_argument('-o', '--output', type=str, metavar='', required=True, help='Output directory')
parser.add_argument('-f', '--filters', type=str, metavar='', required=True, help='Apply Filters to output directory')
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
