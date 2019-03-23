import json
from _config import Config, Token, generate_log
from _request import Request
from _connection import Connection, get_file_sql


class Controller:

    def __init__(self):
        token = Token()
        self.__request = Request(store_name=token.store_name, token=token.token)
        self.__connection = Connection()
        self.__config = Config()

    def _get_api(self, table):
        try:
            json_file = self.__request.get_list(table)
            self._export_json('api_{}.json'.format(table), json_file)
            return json_file
        except Exception as fail:
            generate_log('fail to api request, table: {}, fail: {}!'.format(table, fail))
            return None

    def _get_database(self, sql_table, sql_query):
        try:
            json_file = self.__connection.sql_query(sql_query)
            self._export_json('database_{}.json'.format(sql_table), json_file)
            return json_file
        except Exception as fail:
            generate_log('fail to database request, table: {}, fail: {}!'.format(sql_table, fail))
            return None

    def _export_json(self, archive_name, archive):
        try:
            if self.__config.system_export_requests_json:
                if len(archive) > 1:
                    with open(archive_name, 'w') as file:
                        json.dump(archive, file)
                else:
                    generate_log('archive {} is empty!'.format(archive_name))
        except Exception as fail:
            generate_log('fail to export json request, archive: {}, fail: {}!'.format(archive_name, fail))


class ProductController(Controller):

    def __init__(self):
        super().__init__()
        self.get_products_api()
        self.get_products_database()

    def get_products_api(self):
        json_api = self._get_api('products')

        if len(json_api) > 0:
            #json_api = sorted(json_api, key=lambda k: k['erpId'])
            return json_api
        else:
            return None

    def get_products_database(self):
        try:
            products = self._get_database('products', get_file_sql('products.sql'))
            filters = self._get_database('filter', get_file_sql('filters.sql'))            

            print('test')
            for filter in filters:
                for product in products:
                    if filter['erpId'] == product['erpId']:
                        new_filter = {'filter': {filter['name']: filter['values']}}
                        product[filter] = json.loads(new_filter)
                    elif filter['erpId'] > product['erpId']:
                        break
            print('test2')

            self._export_json('database_products_final', products)
            return products
        except Exception as fail:
            generate_log('falha ao buscar produtos do banco de dados, falha: {}!'.format(fail))


con = ProductController()
