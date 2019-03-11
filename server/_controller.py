from _config import Token
from _request import Request
from _models import Product
from _connection import Connection


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
        list_products = self._get_api('products')
        products = []
        for product in list_products:
            products.append(Product(product))
        return products

    def get_products_database(self):
        sql_query = "SELECT PROD_CODIGO as id, PROD_ID_CIASHOP as erpId, '' as filters FROM CSI_PRODUTO"
        query = self._get_database(sql_query)
        products = []
        for product in query:
            products.append(Product(product))
        return products
