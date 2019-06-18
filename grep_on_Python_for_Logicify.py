import re


def grep(subline, file, is_invert):
    with open(file) as f:
        for line in f:
            match = re.search(subline, line)
            if match and not is_invert:
                print(line.rstrip())
            elif not match and is_invert:
                print(line.rstrip())
