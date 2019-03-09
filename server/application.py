import datetime
from server.controller.product_controller import ProductController
from server.service.config import Config


class Application(object):

    def __init__(self):
        product_controller = ProductController()
        self.__config = Config()
        self.__products = product_controller.get_orders()

    def syncronize(self):
        self.generate_log('start process')
        for product in self.__products:
            self.generate_log('print product')
            print('-------------------')
            product.response.print_json()
            print('-------------------')
            print('\n')

    def generate_log(self, log):
        log_file = '{}\\{}.{}'.format(self.__config.log_path, self.__config.log_name, self.__config.log_extension)
        with open(log_file, 'w') as file:
            file.write('{}: {}'.format(datetime.datetime.now(), log))

application = Application()
application.syncronize()
