"""
"""
import argparse

from controller import get_arrears


def main():
    parser = argparse.ArgumentParser(
        prog='regal-tools',
        description='A simple tool to help me generate reports',
        epilog='Coleman A. Matey'
    )

    parser.add_argument(
        '--arrears', 
        choices=['current', 'previous'],
        help="Choose the type of arrears: current, previous",
    )

    args = parser.parse_args()

    if args.arrears:
        get_arrears(args.arrears)


if __name__ == "__main__":
    main()
