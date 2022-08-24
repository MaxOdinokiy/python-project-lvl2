from pydoc import plain
from gendiff.formatters import stylish, plain


def formatter(data, format):
    if format == 'stylish':
        return stylish.rend_stylish(data)
    elif format == 'plain':
        return plain.rend_plain(data)
    raise ValueError(f'Try use another format, not {format}')
