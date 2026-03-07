import json
from pathlib import Path

import yaml


def get_parser(filepath):
    extension = Path(filepath).suffix.lower()

    parsers = {
        '.json': parse_json,
        '.yaml': parse_yaml,
        '.yml': parse_yaml,
    }
    return parsers[extension](filepath)


def parse_json(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)


def parse_yaml(file_name):
    with open(file_name, 'r') as f:
        return yaml.safe_load(f)
