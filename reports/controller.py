"""
Controller
"""
import argparse

import model
import view


def arguments():    
    parser = argparse.ArgumentParser(
        prog='regal-tools',
        description='A simple tool to help me generate reports at Regal International School',
        epilog='Coleman A. Matey'
    )
    parser.add_argument('-a', '--arrears')
    return parser.parse_args()


def main():
    """The main function"""
    args = arguments()
    conn = model.connect()
    query = model.read_sql(f'./reports/scripts/{args.arrears}_arrears.sql')
    data = model.fetch_data(conn, query)
    view.template(args.arrears, data, "desktop")
    model.disconnect(conn)
