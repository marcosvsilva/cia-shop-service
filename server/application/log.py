import datetime
from server.service import Config


class Log(object):

    def __init__(self):
        self.__config = Config()

    def generate_log(self, log):
        log_file = '{}\\{}.{}'.format(self.__config.log_path, self.__config.log_name, self.__config.log_extension)
        with open(log_file, 'a') as file:
            file. writelines('{}: {}\n'.format(datetime.datetime.now(), log.lower()))
