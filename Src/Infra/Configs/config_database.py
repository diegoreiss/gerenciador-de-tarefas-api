import os
from configparser import ConfigParser


class ConfigDatabase(ConfigParser):
    def get_string_connection(self, section: str = 'mysql') -> str:
        full_file_path = os.path.join(os.getcwd(), 'database.ini')

        self.read(full_file_path)

        if self.has_section(section):
            params = self.items(section)

            db_params = {param[0]: param[1] for param in params}

            return ConfigDatabase.__format_db_string_connection(db_params)

    @staticmethod
    def __format_db_string_connection(params: dict) -> str:
        pattern = 'dialect+driver://username:password@host:port/database'

        for key, value in params.items():
            pattern = pattern.replace(key, value)

        return pattern
