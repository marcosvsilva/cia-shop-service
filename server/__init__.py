from server.controller.product_controller import ProductController
from server.service.token import Token

token = Token()

product_controller = ProductController()
products = product_controller.get_orders()

for product in products:
    print('-------------------')
    print('Print product list in {}'.format(token.get_store_name()))
    product.print_product()
    print('-------------------')
    print('\n')
