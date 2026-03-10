def format_value_plain(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def walk_plain(diff_tree, path=""):
    lines = []

    for node in diff_tree:
        key = node["key"]
        status = node["status"]

        # Полный путь
        current_path = f"{path}.{key}" if path else key

        if status == "nested":
            # Если вложенный, рекурсивно обходим детей
            lines.extend(walk_plain(node["children"], current_path))

        elif status == "unchanged":
            # Неизменённые не выводим в plain
            pass

        elif status == "added":
            val = format_value_plain(node["value"])
            lines.append(
                f"Property '{current_path}' was added with value: {val}"
            )

        elif status == "removed":
            lines.append(f"Property '{current_path}' was removed")

        elif status == "changed":
            old_val = format_value_plain(node["value_old"])
            new_val = format_value_plain(node["value_new"])
            lines.append(
                f"Property '{current_path}' was updated."
                f" From {old_val} to {new_val}"
            )

    return lines


def format_plain(diff_tree):
    lines = walk_plain(diff_tree)
    return "\n".join(lines)
