import argparse

from gendiff.core import generate_gendiff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="path to first file")
    parser.add_argument("second_file", help="path to second file")
    parser.add_argument(
        "-f",
        "--format",
        choices=["stylish", "plain"],
        default="stylish",
        help="set format of output (default: stylish)",
    )
    args = parser.parse_args()
    result = generate_gendiff(args.first_file, args.second_file, args.format)
    return result


if __name__ == "__main__":
    main()
