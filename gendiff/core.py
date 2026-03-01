import json


def json_file_reader(filename):
    result = json.load(open(filename))
    return result

