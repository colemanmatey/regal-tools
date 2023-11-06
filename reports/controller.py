"""
Controller
"""

import model
import view


def main():
    """The main function"""
    conn = model.connect()
    query = model.read_sql("./reports/scripts/arrears.sql")
    data = model.fetch_data(conn, query)
    view.current_arrears(data, "desktop")
    model.disconnect(conn)
