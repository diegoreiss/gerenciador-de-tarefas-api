import os
from configparser import ConfigParser


def config_database(section: str = 'mysql') -> str:

    def get_string_connection(db: dict) -> str:
        pattern = 'dialect+driver://username:password@host:port/database'

        for key, value in db.items():
            pattern = pattern.replace(key, value)

        return pattern

    root_path = os.path.dirname(os.getcwd())
    full_file_path = os.path.join(root_path, 'database.ini')

    parser = ConfigParser()
    parser.read(full_file_path)

    if parser.has_section(section):
        params = parser.items(section)

        db_params = { param[0]: param[1] for param in params }

        return get_string_connection(db_params)
