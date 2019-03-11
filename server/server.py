from _controller import ProductController
from _config import generate_log


class Application:

    def __init__(self):
        product_controller = ProductController()
        self.__products = product_controller.get_products_api()
        self.__products_database = product_controller.get_products_database()

    def synchronize(self):
        generate_log('start process')

        for product in self.__products:
            generate_log('print product')
            print('-------------------')
            print(product.describe())
            generate_log(product.describe())
            print('-------------------')
            print('\n')

        for product in self.__products_database:
            generate_log('print product')
            print('-------------------')
            print(product.describe())
            generate_log(product.describe())
            print('-------------------')


app = Application()
app.synchronize()
