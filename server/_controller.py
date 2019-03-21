from _config import Token
from _request import Request
from _models import Product
from _connection import Connection, get_file_sql


class Controller:

    def __init__(self):
        token = Token()
        self.__request = Request(store_name=token.store_name, token=token.token)
        self.__connection = Connection()

    def _get_api(self, table):
        return self.__request.get_list(table)

    def _get_database(self, sql_query):
        return self.__connection.sql_query(sql_query)


class ProductController(Controller):

    def __init__(self):
        super().__init__()

    def get_products_api(self):
        try:
            return self._get_api('products')
        except:
            return None

    def get_products_database(self):
        try:
            products = self._get_database(get_file_sql('products.sql'))
            filters = self._get_database(get_file_sql('filters.sql'))

            return self.__products_database
        except:
            return None

    def get_id_products_api(self):
        return self.__id_products_api

    def get_id_products_database(self):
        return self.__id_products_database
