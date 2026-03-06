import json


def read_file(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)


def generate_gendiff(filepath1, filepath2):
    data1 = read_file(filepath1)
    data2 = read_file(filepath2)
    diff_tree = build_diff_tree(data1, data2)
    formated_result = formation_output(diff_tree)
    return formated_result


def add_prefix(key, value, status):
    prefixes = {
        'unmatched': ' ',
        'added': '+',
        'removed': '-',
    }
    return f"{prefixes[status]} {key}: {value}"


def formation_output(diff_tree):
    lines = ['{']
    for line in diff_tree:
        lines.append(line)
    lines.append('}')
    return '\n'.join(lines)


def build_diff_tree(data1, data2):
    result = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in all_keys:
        in_first_file = key in data1
        in_second_file = key in data2

        if in_first_file and in_second_file:
            if data1[key] == data2[key]:
                result.append(add_prefix(key, data1[key], 'unmatched'))
            else:
                result.append(add_prefix(key, data1[key], 'removed'))
                result.append(add_prefix(key, data2[key], 'added'))
        elif in_first_file:
            result.append(add_prefix(key, data1[key], 'removed'))
        else:
            result.append(add_prefix(key, data2[key], 'added'))

    return result
