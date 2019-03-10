from _config import Token
from _request import Request
from _models import Product


class Controller:

    def __init__(self):
        token = Token()
        self._request = Request(store_name=token.store_name, token=token.token)


class ProductController(Controller):

    def __init__(self):
        super().__init__()
        self.products = self._request.get_list('products')

    def get_orders(self):
        products = []
        for product in self.products:
            products.append(Product(product))
        return products
