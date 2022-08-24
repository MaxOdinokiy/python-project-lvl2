#!/usr/bin/env python3
from gendiff import file_parser, tree
from gendiff.formatters import stylish


def get_file_data(file_path):
    return file_parser.pars(file_path)


def generate_diff(file_path1, file_path2):
    file_data1 = get_file_data(file_path1)
    file_data2 = get_file_data(file_path2)
    difference = tree.diff(file_data1, file_data2)
    result = stylish.walk(difference)
    return result


def start(args):
    print(generate_diff(args.first_file, args.second_file))
