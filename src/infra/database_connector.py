import sqlite3


class DatabaseConnection:

    connection = None

    @classmethod
    def connect(cls):
        db_connection = sqlite3.connect('lhama.db')
        cls.connection = db_connection
