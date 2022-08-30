#!/usr/bin/env python3
from gendiff import file_parser, tree
from gendiff.formatters import formatter


def get_file_data(file_path):
    return file_parser.pars(file_path)


def generate_diff(file_path1, file_path2, format='stylish'):
    '''
    Two files difference generator.
    get_file data returns python format of file
    tree.diff returs difference between 2 files
    formatter returns requiring format
    '''
    file_data1 = get_file_data(file_path1)
    file_data2 = get_file_data(file_path2)
    difference = tree.diff(file_data1, file_data2)
    result = formatter.formatter(difference, format)
    return result


def start(args):
    '''
    Output difference to console
    '''
    print(generate_diff(args.first_file, args.second_file, args.format))
