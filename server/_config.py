import json
import datetime


class Config:

    def __init__(self):
        self.__class_system = ['active', 'generate_log', 'export_url_request_log', 'export_update_sql_log',
                               'export_requests_json', 'sleep_timer_synchronize', 'register_max_returns']
        self.__class_log = ['path', 'log', 'log_fail', 'extension']

    def get_key(self, key):
        if key in self.__class_system:
            return self.__read_key_system_config(key)

        elif key in self.__class_log:
            return self.__read_key_log_config(key)

        else:
            generate_log('key {} not found in config')
            disable_service()

    def __read_key_log_config(self, key_log):
        return self.__read_keys_config('log')[key_log]

    def __read_key_database_config(self, key_log):
        return self.__read_keys_config('database')[key_log]

    def __read_key_system_config(self, key_log):
        return self.__read_keys_config('system')[key_log]

    @staticmethod
    def __read_keys_config(key):
        return read_archive('config.cfg')[key]


class Token:

    def __init__(self):
        self.__class_token = ['store_name', 'token']
        self.__class_database = ['server', 'port', 'database', 'trusted_connection', 'uid', 'pwd']

    def get_key(self, key):
        if key in self.__class_token:
            return self.__read_token(key)

        elif key in self.__class_database:
            return self.__read_database(key)

        else:
            generate_log('key {} not found in token')
            disable_service()

    def __read_token(self, key):
        return self.__read_token_file('key')[key]

    def __read_database(self, key):
        return self.__read_token_file('database')[key]

    @staticmethod
    def __read_token_file(key):
        return read_archive('key.token')[key]


def read_archive(file_name):
    try:
        file_read = 'C:\\Jave\\CSAPIService\\{}'.format(file_name)
        with open(file_read, 'r') as file:
            archive_config = json.loads(file.read())

        return archive_config
    except Exception as fail:
        generate_log('fail read config file {}, fail: {}'.format(file_name, fail))
        return None


def disable_service():
    config_name = 'C:\\Jave\\CSAPIService\\{}'.format("config.cfg")
        
    try:
        archive_config = __read_archive('config.cfg')
        archive_config['system']['active'] = 'no'

        with open(config_name, 'w') as file:
            file.write(json.dumps(archive_config))

        generate_log('turn off service')
    except Exception as fail:
        generate_log('fail disable service, fail: {}'.format(fail))


def generate_log(log, fail=False):
    config = Config()

    if fail:
        name_archive = config.get_key('log_fail')
    else:
        name_archive = config.get_key('log')

    if config.get_key('generate_log') == 'yes':
        log_file = 'C:\\Jave\\CSAPIService\\{}.{}'.format(name_archive, config.get_key('extension'))

        with open(log_file, 'a') as file:
            file.writelines('{}: {}!\n'.format(datetime.datetime.now(), log.replace('\n', ' -- ').lower()))
