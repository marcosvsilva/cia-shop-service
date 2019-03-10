from _controller import ProductController
from _config import generate_log


class Application:

    def __init__(self):
        product_controller = ProductController()
        self.__products = product_controller.get_orders()

    def synchronize(self):
        generate_log('start process')
        for product in self.__products:
            generate_log('print product')
            print('-------------------')
            product.response.print_json()
            print('-------------------')
            print('\n')


application = Application()
application.synchronize()

