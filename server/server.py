from _controller import ProductController
from _config import generate_log


class Application:

    def __init__(self):
        product_controller = ProductController()
        self.__products = product_controller.get_products_api()
        #self.__products_database = product_controller.get_products_database()

    def synchronize(self):
        generate_log('start process')

        for product in self.__products:
            if True:
                print('-------------------')
                print(product.describe())
                print('-------------------')

        for product in self.__products_database:
            if False:
                print('-------------------')
                print(product.describe())
                print('-------------------')

application = Application()
application.synchronize()
