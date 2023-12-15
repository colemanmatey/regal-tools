"""
Main
"""

from regal.database import DatabaseManager


def main():
    db = DatabaseManager()
    db.connect()

    query = "SELECT * FROM studentTbl"
    result = db.fetch_data(query)

    students = []

    for record in result:
        students.append(f"{record[3]} {record[4]}")

    for i in students:
        print(i)

    db.disconnect()

if __name__ == '__main__':
    main()
