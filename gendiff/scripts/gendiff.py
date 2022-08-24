#!/usr/bin/env python3
from gendiff import generate_diff, cli


def main():
    args = cli.run()
    generate_diff.start(args)


if '__name__' == '__main__':
    main()
