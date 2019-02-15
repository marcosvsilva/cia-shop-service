from server.service.request import Request
from server.service.token import Token
from server.model.product import Product


class ProductController(object):

    def __init__(self):
        self.token = Token()
        self.request = Request(store_name=self.token.get_store_name(), token=self.token.get_token())
        self.products = self.request.get_list('products')

    def get_orders(self):
        products = []
        for product in self.products:
            products.append(Product(product))
        return products