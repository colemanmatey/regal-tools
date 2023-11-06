"""
View
"""

import os

import datetime as dt
import xlsxwriter


def destination(location=None):
    """The location of the output file"""
    home_dir = os.path.expanduser("~")
    if location is not None:
        return os.path.join(home_dir, location)

    if not os.path.exists("out"):
        os.makedirs("out")
    return "out"


def create_workbook(name, location):
    """Create workbook"""
    name = (
        f"{destination(location)}/{dt.datetime.now().strftime('%y-%m%d')}_{name}.xlsx"
    )
    book = xlsxwriter.Workbook(name)
    return book


def create_worksheet(book):
    """Create worksheet"""
    sheet = book.add_worksheet()

    # Set column widths
    sheet.set_column("A:A", 4)
    sheet.set_column("B:B", 12)
    sheet.set_column("C:C", 40)
    sheet.set_column("D:D", 16)
    sheet.set_column("E:E", 8)

    return sheet


def current_arrears(data, destination=None):
    """Template for excel file"""
    workbook = create_workbook("current_arrears", destination)
    worksheet = create_worksheet(workbook)

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
        f"Arrears as at {dt.datetime.today().strftime('%A, %B %d, %Y - %I:%M %p')}",
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

    return workbook.close()
