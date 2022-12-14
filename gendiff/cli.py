import argparse

DESCRIPTION = 'Compares two configuration files and shows a difference.'


def run():
    '''
    Creating console args for gendiff.
    Returns input args - files (file1 and file2)
    '''
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        metavar='FORMAT',
        help='set format of output',
        default='stylish',
        choices=['stylish', 'plain', 'json']
    )
    args = parser.parse_args()
    return args
