from CiaShopServer.server.controller.order_controller import OrderController

order_controller = OrderController()
orders = order_controller.get_orders()

for order in orders:
    print(order.id)