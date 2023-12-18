"""
Controller
"""

import os
from pathlib import Path

from . import model
from . import view


def destination(location=None):
    """The location of the output file"""
    home_dir = os.path.expanduser("~")
    if location is not None:
        return os.path.join(home_dir, location)

    if not os.path.exists("out"):
        os.makedirs("out")
    return "out"


def get_scripts_directory(folder):
    return Path(__file__).resolve().parent / folder


def get_arrears(option):
    conn = model.connect()
    scripts = get_scripts_directory('scripts')

    if option == 'current':
        file = scripts / 'current_arrears.sql'
    elif option == 'previous':
        file = scripts / 'previous_arrears.sql'

     
    query = model.read_sql(file)
    cursor = model.fetch_data(conn, query)

    workbook = view.create_workbook(option, "desktop")
    worksheet = view.create_worksheet(workbook)
    view.arrears(option, workbook, worksheet, cursor)
    workbook.close()
    model.disconnect(conn)


def get_lists(option):
    conn = model.connect()
    scripts = get_scripts_directory('scripts')

    
    file = scripts / 'classes.sql'
    query = model.read_sql(file)
    cursor = model.fetch_data(conn, query)

    classrooms = cursor.fetchall()

    if option == "schedules":
        file = scripts / 'fee_schedules.sql'
    else:
        file = scripts / 'class_list.sql'
    query = model.read_sql(file)

    workbook = view.create_workbook(option, "desktop")
    for classroom in classrooms:
        cursor.execute(query, classroom.classid)
        class_list = cursor.fetchall()

        worksheet = view.create_worksheet(workbook, classroom.classid)
        worksheet.set_margins(0.25, 0.25, 0.75, 0.75)

        # Set column widths
        worksheet.set_column('A:A', 4)
        worksheet.set_column('B:B', 11)
        worksheet.set_column('C:C', 42)
        worksheet.set_column('D:D', 8)
        worksheet.set_column('E:E', 7)
        worksheet.set_column('F:F', 7)
        worksheet.set_column('G:G', 7)
        worksheet.set_column('H:H', 7)
        
        view.schedules(cursor, workbook, worksheet, class_list, classroom)  

    workbook.close()
    model.disconnect(conn)
