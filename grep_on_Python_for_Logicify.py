import re
import argparse


def grep(subline, file, is_invert):
    with open(file) as f:
        for line in f:
            match = re.search(subline, line)
            if match and not is_invert:
                print(line.rstrip())
            elif not match and is_invert:
                print(line.rstrip())


def args_lookup(args):
    parser = argparse.ArgumentParser(description='GREP on Python')

    parser.add_argument(
        '-v',
        action="store_true",
        dest="invert",
        default=False,
        help='Selecte lines are that do NOT match')

    parser.add_argument('subline', action="store", help='Define a subline')
    parser.add_argument('file_name', action="store", help='Define a file name')
    return parser.parse_args(args)
