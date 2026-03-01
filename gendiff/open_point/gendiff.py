import argparse

from gendiff.core import json_file_reader


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_file = json_file_reader(args.first_file)
    second_file = json_file_reader(args.second_file)
    print(f"Сравниваю {args.first_file} и {args.second_file}")
    print(f"File 1: {first_file} ; File 2: {second_file}")


if __name__ == '__main__':
    main()
