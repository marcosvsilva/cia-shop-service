import json


class Config(object):

    def __init__(self):
        self.__config = json.loads(self.read_config_archive())
        self.log_path = self.read_key_log_config('log_path')
        self.log_name = self.read_key_log_config('log_name')
        self.log_extension = self.read_key_log_config('log_extension').replace('.', '')

    def read_key_log_config(self, key_log):
        log_json = self.read_keys_config('log')
        return log_json[key_log]

    def read_keys_config(self, key):
        config_json = self.__config
        return config_json[key]

    @staticmethod
    def read_config_archive():
        config_name = "config.cfg"
        with open(config_name) as file:
            archive_config = file.read()

        return archive_config
