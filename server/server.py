from _controller import ProductController
from _config import generate_log


class Application:

    def __init__(self):
        self._product_controller = ProductController()
        self._products_api = self._product_controller.get_products_api()
        self._products_database = self._product_controller.get_products_database()                

    def synchronize(self):
        generate_log('start process')
        for product_api in self._products_api:
            if product_api.id not in self._product_controller.get_id_products_database():
                generate_log('product {} not in database'.format(product_api.id))
                print(product_api.describe())
                print('\n')                


application = Application()
application.synchronize()
