"""This module has a class to handle
environment variables into the project.

Author: Carlos Andres Sierra <cavirguezs@udistrital.edu.co>"""

import os
from dotenv import load_dotenv

load_dotenv()

# pylint: disable=too-few-public-methods
class EnvironmentVariables:
    """This class is used to handle environment variables."""

    def __init__(self):
        """This method is used to initialize the class."""
        self.path_videogames_data = os.getenv("PATH_VIDEOGAMES_DATA")
