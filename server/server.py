from _controller import ProductController
from _config import generate_log

actions = {
    1: 'check database',
    2: 'update api id database'
}


class Application:

    def __init__(self):
        self._product_controller = ProductController()
        self._products_api = self._product_controller.get_products_api()
        self._products_database = self._product_controller.get_products_database()                

    def synchronize(self):
        generate_log('start process synchronize')        
        self.execute_action(actions[1])
        self.execute_action(actions[2])
    
    def execute_action(self, action):        
        print(action)
        generate_log('start process {}'.format(action))

        try:
            if action == actions[1]:
                self.check_database()

            elif action == actions[2]:
                self.update_api_id()

        except:
            generate_log('crash process {}'.format(action))
        
        generate_log('finishing process {}'.format(action))


    def check_database(self):
        for product_api in self._products_api:
            if product_api.id not in self._product_controller.get_id_products_database():
                generate_log('product {} not in database'.format(product_api.id))                
    
    def update_api_id(self):
        list_update
        



application = Application()
application.synchronize()
