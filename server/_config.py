import json
import datetime


class Config:

    def __init__(self):
        self.__config = json.loads(read_config_archive())
        self.log_path = self.read_key_log_config('log_path')
        self.log_name = self.read_key_log_config('log_name')
        self.log_extension = self.read_key_log_config('log_extension').replace('.', '')
        self.database = self.read_key_database_config('database')
        self.database_server = self.read_key_database_config('server')
        self.database_trusted_connection = self.read_key_database_config('trusted_connection')
        self.database_uid = self.read_key_database_config('uid')
        self.database_pwd = self.read_key_database_config('pwd')

    def read_key_log_config(self, key_log):
        log_json = self.read_keys_config('log')
        return log_json[key_log]

    def read_key_database_config(self, key_log):
        log_json = self.read_keys_config('database')
        return log_json[key_log]

    def read_keys_config(self, key):
        config_json = self.__config
        return config_json[key]


class Token:

    def __init__(self):
        self.store_name = read_token_archive('store_name')
        self.token = read_token_archive('token')


def read_config_archive():
    config_name = "config.cfg"
    with open(config_name) as file:
        archive_config = file.read()

    return archive_config


def read_token_archive(key):
    result = None
    token = "key.token"
    with open(token, 'r') as token_read:
        for line in token_read:
            line = line.replace('\n', '')
            line = line.split(':')

            if line[0] == key:
                result = line[1]

    return result


def generate_log(log):
    config = Config()
    if config.log_path != '':
        log_file = '{}\\{}.{}'.format(config.log_path, config.log_name, config.log_extension)
    else:
        log_file = '{}.{}'.format(config.log_name, config.log_extension)

    with open(log_file, 'a') as file:
        file. writelines('{}: {}\n'.format(datetime.datetime.now(), log.replace('\n', ' -- ').lower()))


def get_table(table):
    config = Config()
    tables = config.read_keys_config('tables')
    return tables[table]
