import re
import argparse
import sys


def grep(subline, file, is_invert):
    subline = re.compile(subline)
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


def main():
    params = args_lookup(sys.argv[1:])
    grep(params.subline, params.file_name, params.invert)


if __name__ == '__main__':
    main()
