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
    view.arrears(option, data, "desktop")
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
        
        view.lists(cursor, workbook, worksheet, class_list, classroom)  

    workbook.close()
    model.disconnect(conn)
