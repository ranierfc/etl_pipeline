from typing import Dict
from .database_connector import DatabaseConnection
from .interfaces.database_repository import DatabaseRepositoryInterface


class DatabaseRepository(DatabaseRepositoryInterface):

    @classmethod
    def insert_artist(cls, data: Dict) -> None: # pylint: disable=arguments-differ
        query = '''
            INSERT INTO artist
                (first_name, second_name, surname, artist_id, link, extraction_date)
            VALUES
                (?, ?, ?, ?, ?, ?)
        '''

        cursor = DatabaseConnection.connection.cursor()
        cursor.execute(query, list(data.values()))
        DatabaseConnection.connection.commit()
