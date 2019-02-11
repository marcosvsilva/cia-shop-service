from CiaShopServer.server.controller.order_controller import OrderController
from CiaShopServer.server.service.token import Token

order_controller = OrderController()
orders = order_controller.get_orders()
token = Token()

for order in orders:
    print('-------------------')
    print('Print orders list in {}'.format(token.get_store_name()))
    order.print_order()
    print('-------------------')
    print('\n')