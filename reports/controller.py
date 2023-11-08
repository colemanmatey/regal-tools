"""
Controller
"""

import model
import view


def get_arrears(option):
    conn = model.connect()

    if option == 'current':
        file = f'./reports/scripts/current_arrears.sql'
    elif option == 'previous':
        file = f'./reports/scripts/previous_arrears.sql'
     
    query = model.read_sql(file)
    data = model.fetch_data(conn, query)
    view.template(option, data, "desktop")
    model.disconnect(conn)
