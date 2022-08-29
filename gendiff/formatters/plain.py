STATUSES = {
    'ADDED': 'added',
    'DELETED': 'removed',
    'CHANGED': 'updated',
}


def rend_plain(data):
    return walk(data, '')


def get_string_value(value):
    if isinstance(value, dict):
        value = '[complex value]'
    elif isinstance(value, bool):
        value = str(value).lower()
    elif isinstance(value, int):
        value = value
    elif value is None:
        value = 'null'
    else:
        value = f"'{value}'"
    return value


def make_path(depth, key):
    return '.'.join((depth, key)) if depth else key


def walk(data, depth=''):
    result = []
    key = data.get('key')
    value = get_string_value(data.get('value'))
    value1 = get_string_value(data.get('value1'))
    value2 = get_string_value(data.get('value2'))
    status = data.get('status')
    children = data.get('children')
    depth = make_path(depth, key)
    if status == 'main':
        lines = map(lambda child: walk(child), children)
        result = '\n'.join(lines)
    if status == 'NESTED':
        lines = map(lambda child: walk(child, depth), children)
        filtered_lines = filter(lambda line: line != 'unchanged', lines)
        result = '\n'.join(filtered_lines)
    if status == 'ADDED':
        result = f"Property '{depth}' was {STATUSES[status]} with value: {value}"
    if status == 'DELETED':
        result = f"Property '{depth}' was {STATUSES[status]}"
    if status == 'CHANGED':
        result = f"Property '{depth}' was {STATUSES[status]}. From {value1} to {value2}"  # noqa
    if status == 'UNCHANGED':
        result = 'unchanged'
    return result
