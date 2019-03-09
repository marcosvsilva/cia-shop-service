from server.controller import ProductController
from server.service import Config
from server.application import Log


class Application(object):

    def __init__(self):
        product_controller = ProductController()
        self.__config = Config()
        self.__log = Log()
        self.__products = product_controller.get_orders()

    def syncronize(self):
        self.generate_log('start process')
        for product in self.__products:
            self.__log.generate_log('print product')
            print('-------------------')
            product.response.print_json()
            print('-------------------')
            print('\n')

