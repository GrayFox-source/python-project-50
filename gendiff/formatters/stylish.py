INDENT_SIZE = 4


def format_value(value, depth=0):
    if isinstance(value, dict):
        lines = ["{"]
        for key, val in value.items():
            indent = " " * ((depth + 2) * INDENT_SIZE)
            formatted_val = format_value(val, depth + 1)
            lines.append(f"{indent}{key}: {formatted_val}")

        indent_close = " " * ((depth + 1) * INDENT_SIZE)
        lines.append(f"{indent_close}}}")
        return "\n".join(lines)

    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"

    return str(value)


def format_stylish(diff_tree):
    lines = ["{"]

    stack = []

    for node in reversed(diff_tree):
        stack.append((node, 1))

    while stack:
        node, depth = stack.pop()

        status = node['status']

        indent = " " * (depth * INDENT_SIZE - 2)

        if status == 'close_brace':
            lines.append(f"{indent}}}")
            continue

        key = node['key']

        if status == 'nested':
            lines.append(f"{indent}{key}: {{")

            stack.append(({'status': 'close_brace'}, depth))

            for child in reversed(node['children']):
                stack.append((child, depth + 1))

        elif status == 'unchanged':
            val = format_value(node['value'], depth)
            lines.append(f"{indent}{key}: {val}")

        elif status == 'added':
            val = format_value(node['value'], depth)
            if val == "":
                lines.append(f"{indent}+ {key}:")
            else:
                lines.append(f"{indent}+ {key}: {val}")

        elif status == 'removed':
            val = format_value(node['value'], depth)
            if val == "":
                lines.append(f"{indent}- {key}:")
            else:
                lines.append(f"{indent}- {key}: {val}")

        elif status == 'changed':
            val_old = format_value(node['value_old'], depth)
            val_new = format_value(node['value_new'], depth)
            if val_old == "":
                lines.append(f"{indent}- {key}:")
            else:
                lines.append(f"{indent}- {key}: {val_old}")
            if val_new == "":
                lines.append(f"{indent}+ {key}:")
            else:
                lines.append(f"{indent}+ {key}: {val_new}")

    lines.append("}")
    return "\n".join(lines)
