"""
View
"""

import datetime as dt
import xlsxwriter

import controller


def create_workbook(name, location):
    """Create workbook"""
    name = (
        f"{controller.destination(location)}/{dt.datetime.now().strftime('%y-%m%d')}_{name}.xlsx"
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


def arrears(name, workbook, worksheet, data):
    """Template for an arrears excel file"""

    # Add formats
    title_format = workbook.add_format(
        {
            "font_size": 16,
            "bold": True,
            "text_wrap": False,
            "border": 0,
            "align": "center",
        }
    )

    subtitle_format = workbook.add_format(
        {
            "font_size": 12,
            "bold": True,
            "text_wrap": False,
            "border": 0,
            "align": "center",
        }
    )

    header_format = workbook.add_format({"bold": True, "text_wrap": True, "border": 1})

    row_format = workbook.add_format({"border": 1, "text_wrap": False})

    total_format = workbook.add_format(
        {
            "bold": True,
            "font_size": 12,
            "border": 1,
            "text_wrap": False,
        }
    )

    # Write title and subtitle to the first and second roworksheet respectively
    worksheet.merge_range(0, 0, 0, 4, "REGAL INTERNATIONAL SCHOOL", title_format)
    worksheet.merge_range(1, 0, 1, 4,
        f"{name.title()} Arrears as at {dt.datetime.today().strftime('%A, %B %d, %Y - %I:%M %p')}",
        subtitle_format,
    )

    # Create column headers for each worksheet
    columns = [column[0] for column in data.description]

    # Write table header to the fourth row
    worksheet.write_row(3, 0, columns, header_format)

    # Write data to subsequent roworksheet
    rownum = 4
    for i in data:
        worksheet.write_row(rownum, 0, i, row_format)
        rownum += 1

    # Write data to last row for total
    last_row = rownum
    worksheet.merge_range(last_row, 0, last_row, 3, "Total:", total_format)
    worksheet.write(last_row, 4, f"=SUM(E5:E{last_row})", total_format)


def lists(cursor, workbook, worksheet, class_list, classroom):
    """Template for a list"""
    title_format = workbook.add_format({
        'font_size': 16,
        'bold': True,
        'text_wrap': False,
        'border': 0,
        'align': 'center'
    })

    subtitle_format = workbook.add_format({
        'font_size': 12,
        'bold': True,
        'text_wrap': False,
        'border': 0,
        'align': 'center'
    })

    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'border': 1
    })

    row_format = workbook.add_format({
        'border': 1,
        'text_wrap': False
    })

    total_format = workbook.add_format({
        'bold': True,
        'font_size': 13,
        'border': 1,
        'text_wrap': False,
    })

    # Write title and subtitle to the first and second roworksheet respectively
    worksheet.merge_range(0, 0, 0, 4, "REGAL INTERNATIONAL SCHOOL", title_format)
    worksheet.merge_range(1, 0, 1, 4, f"Academic year - 1st Term, {dt.datetime.today().strftime('%Y')}", subtitle_format)
    worksheet.merge_range(2, 0, 2, 4, classroom.classid, subtitle_format)

    # Create column headers for each worksheet
    columns = [column[0] for column in cursor.description]

    # Write table header to the fourth row
    worksheet.write_row(3, 0, columns, header_format)

    # Write data to subsequent rows
    rownum = 4
    for student in class_list:
        worksheet.write_row(rownum, 0, student, row_format)
        rownum += 1

    # Write data to last row for total
    last_row = rownum
    worksheet.merge_range(last_row, 0, last_row, 3, "Total:", total_format)
    worksheet.write(last_row, 4, f"=SUM(E5:E{last_row})", total_format)
