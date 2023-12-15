"""
Database
"""

import threading
import pyodbc
from regal.config import ConfigManager, Logger

class DatabaseManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, env_var=".env"):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(DatabaseManager, cls).__new__(cls)
                cls._instance.logger = Logger().logger
                cls._instance.credentials = ConfigManager(env_var)
            return cls._instance
        
    def connect(self):
        """Initialize database connection"""
        try:
            self.logger.info("Connecting to database.")
            self.connection = pyodbc.connect(
                DRIVER=self.credentials.get_var("DRIVER"),
                SERVER=self.credentials.get_var("DB_HOST"),
                DATABASE=self.credentials.get_var("DB_NAME"),
                UID=self.credentials.get_var("DB_USER"),
                PWD=self.credentials.get_var("DB_PASS")
            )  
            self.logger.info("Connected to the database successfully.")
        except Exception as e:
            self.logger.exception(f'Could not establish a connection to the database: {e}')
            return None
        
    def execute_query(self, sql_query):
        """Execute the database query"""
        try:
            cursor = self.connection.cursor()
            self.logger.info(f"Executing query: {sql_query}")
            cursor.execute(sql_query)
            self.connection.commit()
            self.logger.info("Query has been executed successfully.")
        except AttributeError as e:
            self.logger.error(f"{e}. \nCall the .connect() method on the DatabaseManager object before calling the .fetch_data() method")
        except Exception as e:
            self.logger.exception(f"Error executing query: {e}")
    
    def fetch_data(self, sql_query):
        """Fetch the database query"""
        try:
            cursor = self.connection.cursor()
            self.logger.info("Fetching data from database")
            cursor.execute(sql_query)
            result = cursor.fetchall()
            self.logger.info("Data retrieved from database successfully.")
            return result
        except AttributeError as e:
            self.logger.error(f"{e}. \nCall the .connect() method on the DatabaseManager object before calling the .fetch_data() method")
            return None
        except Exception as e:
            self.logger.error(e)
            return None

    def disconnect(self):
        """Close the database connection"""
        self.logger.info("Closing database connection")
        try:
            self.connection.close()
            self.logger.info("Connection to database closed successfully")
        except AttributeError as e:
            self.logger.error(f"{e}. \nCan't close a database connection that does not exist")
