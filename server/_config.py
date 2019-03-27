import json
import datetime


class Config:

    def __init__(self):
        self.__class_system = ['active', 'generate_log', 'export_url_request_log', 'export_update_sql_log',
                               'export_requests_json', 'sleep_timer_synchronize', 'register_max_returns']
        self.__class_log = ['path', 'log', 'extension']
        self.__class_database = ['server', 'database', 'trusted_connection', 'uid', 'pwd']

    def get_key(self, key):
        if key in self.__class_system:
            return self.__read_key_system_config(key)

        elif key in self.__class_database:
            return self.__read_key_database_config(key)

        elif key in self.__class_log:
            return self.__read_key_log_config(key)

        else:
            generate_log('key {} not found')
            self.disable_service()

    def disable_service(self):
        config_name = "config.cfg"
        try:
            archive_config = self.__read_config_archive()
            archive_config['system']['active'] = 'no'

            with open(config_name, 'w') as file:
                file.write(json.dumps(archive_config))

            generate_log('turn off service')
        except Exception as fail:
            generate_log('fail disable service, fail: {}'.format(fail))

    def __read_key_log_config(self, key_log):
        return self.__read_keys_config('log')[key_log]

    def __read_key_database_config(self, key_log):
        return self.__read_keys_config('database')[key_log]
    
    def __read_key_system_config(self, key_log):
        return self.__read_keys_config('system')[key_log]

    def __read_keys_config(self, key):
        return self.__read_config_archive()[key]

    @staticmethod
    def __read_config_archive():
        config_name = "config.cfg"
        try:
            with open(config_name, 'r') as file:
                archive_config = json.loads(file.read())

            return archive_config
        except Exception as fail:
            generate_log('fail read config file, fail: {}'.format(fail))


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


def generate_log(log, fail=False):
    config = Config()

    if fail:
        name_archive = config.get_key('log_fail')
    else:
        name_archive = config.get_key('log')

    if config.get_key('generate_log') == 'yes':
        if config.get_key('path') != '':
            log_file = '{}\\{}.{}'.format(config.get_key('path'), name_archive, config.get_key('extension'))
        else:
            log_file = '{}.{}'.format(config.get_key('log'), config.get_key('extension'))

        with open(log_file, 'a') as file:
            file. writelines('{}: {}!\n'.format(datetime.datetime.now(), log.replace('\n', ' -- ').lower()))
