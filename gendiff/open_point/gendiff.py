import argparse

from ..core import generate_gendiff


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                                 ' files and shows a difference'
                                                 '.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    result = generate_gendiff(args.first_file, args.second_file)
    return result


if __name__ == '__main__':
    main()
