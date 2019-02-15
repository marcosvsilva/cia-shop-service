from server.service.request import Request
from server.service.token import Token
from server.model.order import Order


class OrderController(object):

    def __init__(self):
        self.token = Token()
        self.request = Request(store_name=self.token.get_store_name(), token=self.token.get_token())
        self.orders = self.request.get_list('orders')

    def get_orders(self):
        orders = []
        for order in self.orders:
            orders.append(Order(order))
        return orders