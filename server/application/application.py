from server.controller import ProductController
from server.service import Config, Connection
from server.application.log import Log


class Application(object):

    def __init__(self):
        product_controller = ProductController()
        self.__config = Config()
        self.__log = Log()
        self.__products = product_controller.get_orders()

    def synchronize(self):
        self.__log.generate_log('start process')
        for product in self.__products:
            self.__log.generate_log('print product')
            print('-------------------')
            product.response.print_json()
            print('-------------------')
            print('\n')


application = Application()
application.synchronize()
cnn = Connection()
cnn.sql_query('select * from csi_produtos')
print(cnn)