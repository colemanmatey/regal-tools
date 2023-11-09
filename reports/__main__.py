"""
"""
import argparse

from controller import get_arrears, get_lists


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

    parser.add_argument('-c', '--classrooms')

    args = parser.parse_args()

    if args.arrears:
        get_arrears(args.arrears)
    elif args.classrooms:
        get_lists(args.classrooms)

if __name__ == "__main__":
    main()
