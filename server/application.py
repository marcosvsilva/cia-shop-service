from server.controller.product_controller import ProductController
from server.service.config import Config


class Application(object):

    def __init__(self):
        product_controller = ProductController()
        self.products = product_controller.get_orders()

    def syncronize(self):
        for product in self.products:
            print('-------------------')
            product.response.print_json()
            print('-------------------')
            print('\n')