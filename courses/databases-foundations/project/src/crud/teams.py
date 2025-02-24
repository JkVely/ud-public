"""This module contains the CRUD operations for the team table.

Author: Carlos Andres Sierra <cavirguezs@udistrital.edu.co
"""

from typing import List

from connections import DatabaseConnection
from dao import TeamData


class TeamsCRUD:
    """This class is responsible for performing CRUD operations on the team table."""

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection
        self.db_connection.connect()

    def create(self, data: TeamData) -> int:
        """This method creates a new team in the database.

        Args:
            data (TeamData): The team data.

        Returns:
            The perdisted id (code) of the new team.
        """
        query = """
            INSERT INTO team(code, name, color, coach)
            VALUES (%s, %s, %s, %s);
        """
        values = (data.code, data.name, data.color, data.coach)
        return self.db_connection.create(query, values)

    def update(self, code: int, data: TeamData):
        """This method updates the team data in the database.

        Args:
            code (int): The code of the team to be updated.
            data (TeamData): The team data.
        """
        query = """
            UPDATE team 
            SET name = %s, color = %s, coach = %s
            WHERE code = %s;
        """
        values = (data.name, data.color, data.coach, code)
        print(query, values)
        self.db_connection.update(query, values)

    def delete(self, code: int):
        """This method deletes the team from the database.

        Args:
            code (int): The code of the team.
        """
        query = "DELETE FROM team WHERE code = %s;"
        self.db_connection.delete(query, code)

    def get_by_code(self, code: int) -> TeamData:
        """This method gets a team from repository based on the code.

        Args:
            code (int): The code of the team.

        Returns:
            The team data.
        """
        query = """
            SELECT code, name, color, coach 
            FROM team
            WHERE code = %s;
        """
        values = (code,)
        return self.db_connection.get_one(query, values)

    def get_all(self) -> List[TeamData]:
        """This method gets all teams from the repository.

        Returns:
            A list of all teams.
        """
        query = """
            SELECT code, name, color, coach 
            FROM team;
        """
        return self.db_connection.get_many(query)

    def get_by_name(self, name: str) -> List[TeamData]:
        """This method gets a team from repository based on the name.

        Args:
            name (str): The name of the team.

        Returns:
            The team data.
        """
        query = """
            SELECT code, name, color, coach 
            FROM team
            WHERE LOWER(name) LIKE LOWER(%s);
        """
        values = (f"%{name}%",)
        return self.db_connection.get_many(query, values)

    def get_by_color(self, color: str) -> List[TeamData]:
        """This method gets a team from repository based on the color.

        Args:
            color (str): The color of the team.

        Returns:
            The team data.
        """
        query = """
            SELECT code, name, color, coach 
            FROM team
            WHERE color LIKE %s;
        """
        values = (f"%{color}%",)
        return self.db_connection.get_many(query, values)

    def get_by_coach(self, coach: str) -> List[TeamData]:
        """This method gets a team from repository based on the coach.

        Args:
            coach (str): The coach of the team.

        Returns:
            The team data.
        """
        query = """
            SELECT code, name, color, coach 
            FROM team
            WHERE coach LIKE %s;
        """
        values = (f"%{coach}%",)
        return self.db_connection.get_many(query, values)
