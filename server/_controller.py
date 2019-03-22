import pprint
import json
from _config import Config, Token
from _request import Request
from _models import Product
from _connection import Connection, get_file_sql


class Controller:

    def __init__(self):
        token = Token()
        self.__request = Request(store_name=token.store_name, token=token.token)
        self.__connection = Connection()
        self.__config = Config()

    def _get_api(self, table):
        json_file = self.__request.get_list(table)
        self._export_json(table, json_file)
        return json_file

    def _get_database(self, sql_table, sql_query):
        json_file = self.__connection.sql_query(sql_query)
        self._export_json(sql_table, json_file)
        return json_file

    def _export_json(self, archive, archive_name):
        if self.__config.system_export_requests_json and (len(archive) > 1):
            with open('{}.json'.format(archive_name), 'w') as file:
                json.dump(archive, file)


class ProductController(Controller):

    def __init__(self):
        super().__init__()
        self.get_products_api()
        self.get_products_database()

    def get_products_api(self):
        try:
            json_api = self._get_api('products')
            json_api = sorted(json_api, key=lambda k: int(k['erpId']))
            return self._get_api('products')
        except:
            return None

    def get_products_database(self):
        try:
            products = self._get_database('products', get_file_sql('products.sql'))
            filters = self._get_database('filters', get_file_sql('filters.sql'))

            return products
        except:
            return None


con = ProductController()
