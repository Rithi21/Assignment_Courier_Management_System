import pyodbc
import configparser

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            config = configparser.ConfigParser()
            config.read('db.properties')

            db_config = config['default']
            server = db_config['server']
            database = db_config['database']
            driver = db_config['driver']
            username = db_config.get('username', '')
            password = db_config.get('password', '')

            # Use trusted connection if username is empty
            if username.strip() == '':
                connection_string = (
                    f'DRIVER={{{driver}}};'
                    f'SERVER={server};'
                    f'DATABASE={database};'
                    f'Trusted_Connection=yes;'
                )
            else:
                connection_string = (
                    f'DRIVER={{{driver}}};'
                    f'SERVER={server};'
                    f'DATABASE={database};'
                    f'UID={username};PWD={password};'
                )

            try:
                DBConnection.connection = pyodbc.connect(connection_string)
                print("Database connected successfully!")
            except Exception as e:
                print("Error connecting to DB:", e)

        return DBConnection.connection
