from .formatters.stylish import format_stylish
from .parsers import get_parser

FORMATTERS = {
    'stylish': format_stylish,
}


def generate_gendiff(filepath1, filepath2, format_name='stylish'):
    data1 = get_parser(filepath1)
    data2 = get_parser(filepath2)
    diff_tree = build_diff_tree(data1, data2)
    formatter = FORMATTERS.get(format_name, format_stylish)
    formatted_result = formatter(diff_tree)
    return formatted_result


def build_diff_tree(data1, data2):
    result = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        in_first = key in data1
        in_second = key in data2
        val1 = data1.get(key)
        val2 = data2.get(key)

        if in_first and in_second and isinstance(val1, dict) and isinstance(val2, dict):
            result.append({
                'key': key,
                'status': 'nested',
                'children': build_diff_tree(val1, val2)
            })
        elif in_first and in_second:
            if val1 == val2:
                result.append({
                    'key': key,
                    'status': 'unchanged',
                    'value': val1
                })
            else:
                result.append({
                    'key': key,
                    'status': 'changed',
                    'value_old': val1,
                    'value_new': val2
                })
        elif in_first:
            result.append({
                'key': key,
                'status': 'removed',
                'value': val1
            })
        else:
            result.append({
                'key': key,
                'status': 'added',
                'value': val2
            })
    return result
