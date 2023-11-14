"""
Controller
"""

import os

import model
import view


def destination(location=None):
    """The location of the output file"""
    home_dir = os.path.expanduser("~")
    if location is not None:
        return os.path.join(home_dir, location)

    if not os.path.exists("out"):
        os.makedirs("out")
    return "out"

def get_arrears(option):
    conn = model.connect()

    if option == 'current':
        file = f'./reports/scripts/current_arrears.sql'
    elif option == 'previous':
        file = f'./reports/scripts/previous_arrears.sql'
     
    query = model.read_sql(file)
    cursor = model.fetch_data(conn, query)

    workbook = view.create_workbook(option, "desktop")
    worksheet = view.create_worksheet(workbook)
    view.arrears(option, workbook, worksheet, cursor)
    workbook.close()
    model.disconnect(conn)


def get_lists(option):
    conn = model.connect()
    
    file = f'./reports/scripts/classes.sql'
    query = model.read_sql(file)
    cursor = model.fetch_data(conn, query)

    classrooms = cursor.fetchall()

    file = f'./reports/scripts/class_list.sql'
    query = model.read_sql(file)

    workbook = view.create_workbook(option, "desktop")
    for classroom in classrooms:
        cursor.execute(query, classroom.classid)
        class_list = cursor.fetchall()

        worksheet = view.create_worksheet(workbook, classroom.classid)
        
        view.classlists(cursor, workbook, worksheet, class_list, classroom)  

    workbook.close()
    model.disconnect(conn)
