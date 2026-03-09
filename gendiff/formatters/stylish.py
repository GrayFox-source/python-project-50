# gendiff/formatters/stylish.py

INDENT_SIZE = 4


def format_value(value, depth=0):
    """Форматирует значение. Для словарей — цикл for."""
    if isinstance(value, dict):
        lines = ["{"]
        for key, val in value.items():
            indent = " " * ((depth + 1) * INDENT_SIZE - 2)
            formatted_val = format_value(val, depth + 1)
            lines.append(f"{indent}{key}: {formatted_val}")

        indent_close = " " * (depth * INDENT_SIZE - 2)
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
    """Обходит дерево diff с помощью цикла while и стека."""
    lines = ["{"]

    stack = []

    # Инициализируем стек: добавляем корневые узлы в обратном порядке
    for node in reversed(diff_tree):
        stack.append((node, 1))

    while stack:
        node, depth = stack.pop()

        # Сначала проверяем статус
        status = node['status']

        # ✅ Единая формула отступа для всех элементов
        indent = " " * (depth * INDENT_SIZE - 2)

        # Обработка маркера закрытия — до доступа к 'key'
        if status == 'close_brace':
            lines.append(f"{indent}}}")
            continue

        key = node['key']

        if status == 'nested':
            lines.append(f"{indent}{key}: {{")

            # ✅ ИСПРАВЛЕНИЕ 1: close_brace добавляем ПЕРЕД детьми
            stack.append(({'status': 'close_brace'}, depth))

            # Дети добавляем в обратном порядке
            for child in reversed(node['children']):
                stack.append((child, depth + 1))

        elif status == 'unchanged':
            val = format_value(node['value'], depth)
            lines.append(f"{indent}{key}: {val}")

        elif status == 'added':
            val = format_value(node['value'], depth)
            # ✅ ИСПРАВЛЕНИЕ 2: используем indent вместо status_indent
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