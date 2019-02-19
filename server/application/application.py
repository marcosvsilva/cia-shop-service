from server.controller.order_controller import OrderController
from server.controller.product_controller import ProductController
from server.service.token import Token

token = Token()

order_controller = OrderController()
orders = order_controller.get_orders()

product_controller = ProductController()
products = product_controller.get_orders()


for order in orders:
    print('-------------------')
    print('Print orders list in {}'.format(token.get_store_name()))
    order.print_order()
    print('-------------------')
    print('\n')

for product in products:
    print('-------------------')
    print('Print product list in {}'.format(token.get_store_name()))
    product.print_product()
    print('-------------------')
    print('\n')