"""This module contains the class MySQLDatabaseConnection that is responsible for
connecting to the MySQL database.

Author: Carlos Andres Sierra <cavirguezs@udistrital.edu.co>
"""

from typing import List
import mysql.connector
from mysql.connector import Error

from dao import ProjectDAO
from connections.database_connection import DatabaseConnection


class MySQLDatabaseConnection(DatabaseConnection):
    """This class is responsible for connecting to the MySQL database."""

    def __init__(self):
        self._dbname = "football"
        self._duser = "root"
        self._dpass = "admin12345"  # Update the password accordingly
        self._dhost = "localhost"
        self._dport = 3306
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                database=self._dbname,
                user=self._duser,
                password=self._dpass,
                host=self._dhost,
                port=self._dport,
            )
        except Error as e:
            print(f"MySQL Connection Error: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def list_schemas(self):
        schemas = None
        try:
            query = "SHOW DATABASES;"
            cursor = self.connection.cursor()
            cursor.execute(query)
            schemas_db = cursor.fetchall()
            cursor.close()
            schemas = schemas_db
        except Error as e:
            print(f"MySQL Execution Error: {e}")

        return schemas

    def create(self, query: str, values: tuple) -> int:
        id_ = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            id_ = cursor.lastrowid
            cursor.close()
        except Error as e:
            print(f"MySQL Add Data Error: {e}")

        return id_

    def update(self, query: str, values: tuple):
        try:
            print(query, values)
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"MySQL Update Data Error: {e}")

    def delete(self, query: str, item_id: int):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (item_id,))
            self.connection.commit()
            cursor.close()
        except Error as e:
            print(f"MySQL Delete Data Error: {e}")

    def get_one(self, query: str, values: tuple) -> ProjectDAO:
        item = None
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            item = cursor.fetchone()
            if item is not None:
                columns = [desc[0] for desc in cursor.description]
                item = dict(zip(columns, item))
            cursor.close()
        except Error as e:
            print(f"MySQL Get Data Error: {e}")

        return item

    def get_many(self, query: str, values: tuple = ()) -> List[ProjectDAO]:
        results = []
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            items = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            results = [dict(zip(columns, row)) for row in items]
            cursor.close()
        except Error as e:
            print(f"MySQL Get Data Error: {e}")

        return results
