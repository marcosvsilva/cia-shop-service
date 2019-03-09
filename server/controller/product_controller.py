from server.controller import Controller
from server.model import Product


class ProductController(Controller):

    def __init__(self):
        super().__init__()
        self.products = self._request.get_list('products')

    def get_orders(self):
        products = []
        for product in self.products:
            products.append(Product(product))
        return products
