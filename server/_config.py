import json
import datetime


class Config:

    def __init__(self):
        self.__config = json.loads(self.__read_config_archive())

        self.log_path = self.read_key_log_config('log_path')
        self.log_name = self.read_key_log_config('log_name')
        self.log_extension = self.read_key_log_config('log_extension').replace('.', '')

        self.database = self.read_key_database_config('database')
        self.database_server = self.read_key_database_config('server')
        self.database_trusted_connection = self.read_key_database_config('trusted_connection')
        self.database_uid = self.read_key_database_config('uid')
        self.database_pwd = self.read_key_database_config('pwd')

        self.system_active = self.read_key_system_config('active') == 'yes'
        self.system_generate_log = self.read_key_system_config('generate_log') == 'yes'
        self.system_export_url_request_log = self.read_key_system_config('export_url_request_log') == 'yes'
        self.system_export_update_sql_log = self.read_key_system_config('export_update_sql_log') == 'yes'
        self.system_export_requests_json = self.read_key_system_config('export_requests_json') == 'yes'
        self.system_sleep_timer_synchronize = self.__parse_int('sleep_timer_synchronize',
                                                               self.read_key_system_config('sleep_timer_synchronize'))
        self.system_register_max_returns = self.__parse_int('register_max_returns',
                                                            self.read_key_system_config('register_max_returns'))

    def read_key_log_config(self, key_log):
        log_json = self.read_keys_config('log')
        return log_json[key_log]

    def read_key_database_config(self, key_log):
        log_json = self.read_keys_config('database')
        return log_json[key_log]
    
    def read_key_system_config(self, key_log):
        log_json = self.read_keys_config('system')
        return log_json[key_log]

    def read_keys_config(self, key):
        config_json = self.__config
        return config_json[key]

    @staticmethod
    def __read_config_archive():
        config_name = "config.cfg"
        with open(config_name) as file:
            archive_config = file.read()

        return archive_config

    @staticmethod
    def __parse_int(key_name, key):
        try:
            return int(key)
        except ValueError:
            generate_log('failure! the {} key and it must be an integer'.format(key_name))


class Token:

    def __init__(self):
        self.store_name = self.__read_token_archive('store_name')
        self.token = self.__read_token_archive('token')

    @staticmethod
    def __read_token_archive(key):
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
    
    if config.system_generate_log:
        if config.log_path != '':
            log_file = '{}\\{}.{}'.format(config.log_path, config.log_name, config.log_extension)
        else:
            log_file = '{}.{}'.format(config.log_name, config.log_extension)

        with open(log_file, 'a') as file:
            file. writelines('{}: {}!\n'.format(datetime.datetime.now(), log.replace('\n', ' -- ').lower()))
