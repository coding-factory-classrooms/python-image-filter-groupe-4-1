from filters.filters import Filters
import glob
import argparse
from logger.logger import Logger
from configparser import ConfigParser
import os

filters = Filters()

parser = argparse.ArgumentParser(description='Filter a directory of images')

# Required arguments
arguments = parser.add_argument_group("arguments")
arguments.add_argument('-i', '--input', type=str, metavar='', required=False, help='Input directory')
arguments.add_argument('-o', '--output', type=str, metavar='', required=False, help='Output directory')
arguments.add_argument('-f', '--filters', type=str, metavar='', required=False, help='Apply Filters to output directory')

# Optional arguments
optional_arguments = parser.add_argument_group("optionals")
optional_arguments.add_argument('-l', '--log', required=False, help="Show logs and exit")
optional_arguments.add_argument('-cf', '--config', type=str, metavar='', required=False, help="Define a file to use instead of -f -i and -o options")

# Parsing args
args = parser.parse_args()

config = {
    "input": args.input,
    "output": args.output,
    "filters": args.filters,
}


def filter_directory(input_dir, filter_type, output_directory):
    for filepath in glob.glob(f'{input_dir}*'):
        try:
            if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
                filters.filter(filepath, filter_type, output_directory)
        except Exception as e:
            print(f'Please make sure your directory is correct, \nerror : {e}')


def conf_from_ini_file(ini_file):
    """
    :param ini_file: The .ini file to read
    :return:
    """

    config_file = ConfigParser()
    if os.path.exists(ini_file) and os.path.isfile(ini_file):
        config_file.read(ini_file)
        output = config_file["general"]["output_dir"]
        input = config_file["general"]["input_dir"]
        filters = config_file["FILTERS"]["filters"]
        log = config_file["general"]["log_file"]
        return {
            "output": output,
            "input": input,
            "filters": filters,
            "log": log,
        }


config_ini = conf_from_ini_file('config.ini')
config = config_ini
print(config["input"])

if __name__ == '__main__':
    filter_directory(args.input, args.filters, args.output)
    if args.log:
        logger = Logger()
        logger.dump_log()
    elif args.config:
        args.input = config["input"]
        args.output = config["output"]
        args.filters = config["filters"]
        filter_directory(args.input, args.filters, args.output)

