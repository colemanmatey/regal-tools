"""
View
"""

import datetime as dt
from collections import namedtuple

import xlsxwriter
from . import controller

def create_workbook(name, location):
    """Create workbook"""
    name = (
        f"{controller.destination(location)}/{dt.datetime.now().strftime('%y-%m%d%I%M%p')}_{name}.xlsx"
    )
    book = xlsxwriter.Workbook(name)
    return book


def create_worksheet(book, sheet_name=None):
    """Create worksheet"""
    sheet = book.add_worksheet(name=sheet_name)

    # Set column widths
    sheet.set_column("A:A", 4)
    sheet.set_column("B:B", 12)
    sheet.set_column("C:C", 40)
    sheet.set_column("D:D", 16)
    sheet.set_column("E:E", 8)

    return sheet


def get_styles(workbook):
    """Template for views"""
    # Add formats
    title = workbook.add_format(
        {
            "font_size": 16,
            "bold": True,
            "text_wrap": False,
            "border": 0,
            "align": "center",
        }
    )

    subtitle = workbook.add_format(
        {
            "font_size": 12,
            "bold": True,
            "text_wrap": False,
            "border": 0,
            "align": "center",
        }
    )

    header = workbook.add_format({"bold": True, "text_wrap": True, "border": 1})

    row = workbook.add_format({"border": 1, "text_wrap": False})

    total = workbook.add_format(
        {
            "bold": True,
            "font_size": 12,
            "border": 1,
            "text_wrap": False,
        }
    )

    # Create a named tuple class for styles
    Style = namedtuple('Style', ['title', 'subtitle', 'header', 'row', 'total'])

    # Create an instance of the named tuple
    return Style(title=title, subtitle=subtitle, header=header, row=row, total=total)


def write_data(workbook, worksheet, cursor=None, *args):
    """Write the data to cells"""

    styles = get_styles(workbook)

    # Create column headers for each worksheet
    columns = [column[0] for column in cursor.description]

    # Write table header to the fourth row
    worksheet.write_row(3, 0, columns, styles.header)

    # Write data to subsequent roworksheet
    rownum = 4

    if args:
        for i in args[0]:
            worksheet.write_row(rownum, 0, i, styles.row)
            rownum += 1
    else:
        for i in cursor:
            worksheet.write_row(rownum, 0, i, styles.row)
            rownum += 1

    # Write data to last row for total
    last_row = rownum
    worksheet.merge_range(last_row, 0, last_row, 3, "Total:", styles.total)
    worksheet.write(last_row, 4, f"=SUM(E5:E{last_row})", styles.total)
    

def arrears(name, workbook, worksheet, cursor):
    """Template for an arrears excel file"""

    styles = get_styles(workbook)

    # Write title and subtitle to the first and second roworksheet respectively
    worksheet.merge_range(0, 0, 0, 4, "REGAL INTERNATIONAL SCHOOL", styles.title)
    worksheet.merge_range(1, 0, 1, 4,
        f"{name.title()} Arrears as at {dt.datetime.today().strftime('%A, %B %d, %Y - %I:%M %p')}",
        styles.subtitle,
    )

    write_data(workbook, worksheet, cursor)
    


def classlists(cursor, workbook, worksheet, class_list, classroom):
    """Template for a list"""

    styles = get_styles(workbook)

    # Write title and subtitle to the first and second roworksheet respectively
    worksheet.merge_range(0, 0, 0, 4, "REGAL INTERNATIONAL SCHOOL", styles.title)
    worksheet.merge_range(1, 0, 1, 4, f"Academic year - 1st Term, {dt.datetime.today().strftime('%Y')}", styles.subtitle)
    worksheet.merge_range(2, 0, 2, 4, classroom.classid, styles.subtitle)

    write_data(workbook, worksheet, cursor, class_list)
