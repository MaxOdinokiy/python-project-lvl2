from gendiff.formatters import stylish


def formatter(data, format):
    if format == 'stylish':
        return stylish.rend_stylish(data)
    raise ValueError(f'Try use another format, not {format}')
