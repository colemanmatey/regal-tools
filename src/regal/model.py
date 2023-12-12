"""
Model
"""

import pyodbc
from decouple import config


def connect():
    """Connect to SQL Server database"""
    conn = pyodbc.connect(
        DRIVER=config("DRIVER"),
        SERVER=config("DB_HOST"),
        DATABASE=config("DB_NAME"),
        UID=config("DB_USER"),
        PWD=config("DB_PASS"),
    )
    return conn


def disconnect(conn):
    """Commit and close database connection"""
    if conn:
        conn.commit()
        conn.close()


def read_sql(file):
    """Read sql from file."""
    with open(file, "r") as f:
        query = f.read()
    return query


def fetch_data(conn, query):
    """Fetch the data from the database"""
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor
