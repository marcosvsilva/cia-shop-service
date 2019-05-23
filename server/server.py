import time
from _controller import ProductController, DepartmentController
from _config import Config, generate_log

actions = {
    1: 'update database api id products',
    2: 'update database api id departments',
    3: 'update database department id products', 
    4: 'update api brands',
    5: 'update api filters'
}


class Application:

    def __init__(self):
        self._config = Config()

        if self._config.get_key('active') == 'yes':
            self._product_controller = ProductController()
            self._products_api = None
            self._products_database = None
            
            self._departments_controller = DepartmentController()
            self._departments_api = None
            self._departments_database = None
        else:
            generate_log('application not start because config active = "no"')

    def synchronize(self):
        while self._config.get_key('active') == 'yes':
            try:
                generate_log('start process synchronize')
                self._products_api = self._product_controller.get_products_api()
                self._products_database = self._product_controller.get_products_database()

                self._departments_api = self._departments_controller.get_departments_api()
                self._departments_database = self._departments_controller.get_departments_database()

                self.execute_action(actions[1])
                self.execute_action(actions[2])
                self.execute_action(actions[3])
                self.execute_action(actions[4])
                self.execute_action(actions[5])

                time_to_sleep = int(self._config.get_key('sleep_timer_synchronize'))
                generate_log('application waiting {} seconds to synchronize'.format(time_to_sleep))
                time.sleep(time_to_sleep)
            except Exception as fail:
                generate_log('crash synchronize, fail: {}'.format(fail))
                break

    def execute_action(self, action):
        generate_log('start process {}'.format(action))

        try:
            if action == actions[1]:
                self.update_database_api_id_products()
            
            if action == actions[2]:
                self.update_database_api_id_departments()
                
            if action == actions[3]:
                self.update_database_departament_id_products()

            if action == actions[5]:
                self.update_api_brands()

            if action == actions[6]:
                self.update_api_filters()

        except Exception as fail:
            generate_log('crash process {}, fail: {}'.format(action, fail))

        generate_log('finishing process {}'.format(action))

    def update_database_api_id_products(self):
        values_keys = {}
        for product_database in self._products_database:
            if product_database['id'] < 0:
                products_api = filter(lambda x: x['erpId'] == product_database['erpId'], self._products_api)
                products_api = list(products_api)

                if len(products_api) == 0:
                    generate_log('product {} not found in ciashop'.format(product_database['erpId']), fail=True)

                for product_api in products_api:
                    if product_database['id'] != product_api['id']:
                        values_keys.update({product_database['erpId']: product_api['id']})

        self._product_controller.update_products_database(values_keys)

    def update_database_api_id_departments(self):
        values_keys = {}
        for departments_database in self._departments_database:
            if departments_database['id'] < 0:
                departments_api = filter(lambda x: x['erpId'] == departments_database['erpId'], self._departments_api)
                departments_api = list(departments_api)

                if len(departments_api) == 0:
                    generate_log('department {} not found in ciashop'.format(departments_database['erpId']), fail=True)

                for department_api in departments_api:
                    if departments_database['id'] != department_api['id']:
                        values_keys.update({departments_database['erpId']: department_api['id']})

        self._departments_controller.update_departments_database(values_keys)

    def update_database_departament_id_products(self):
        self._product_controller.update_department_id

    def update_api_brands(self):
        products_database_update = {}
        for product_api in self._products_api:
            products_database = filter(lambda x: x['erpId'] == product_api['erpId'], self._products_database)
            products_database = list(products_database)

            if len(products_database) == 0:
                generate_log('product {} not found in database'.format(product_api['erpId']), fail=True)

            for product_database in products_database:
                if product_api['brand'] != product_database['brand']:
                    products_database_update.update({product_api['id']: {'brand': product_database['brand']}})

        self._product_controller.update_products_api(products_database_update)

    def update_api_filters(self):
        products_database_update = {}
        for product_api in self._products_api:
            products_database = filter(lambda x: x['erpId'] == product_api['erpId'], self._products_database)
            products_database = list(products_database)

            for product_database in products_database:
                if ('filters' in product_database) and ('filters' in product_api):
                    if product_database['filters'] != product_api['filters']:
                        products_database_update.update({product_api['id']: {'filters': product_database['filters']}})

        self._product_controller.update_products_api(products_database_update)

application = Application()
application.synchronize()