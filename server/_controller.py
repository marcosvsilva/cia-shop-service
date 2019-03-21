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
        self.__products_api = []
        self.__id_products_api = []
        
        self.__products_database = []
        self.__id_products_database = []

    def get_products_api(self):
        try:
            list_products = self._get_api('products')        
            
            for product in list_products:            
                self.__products_api.append(product)
            
            return self.__products_api

        except:
            return None            

    def get_products_database(self):        
        try:
            products = self._get_database(get_file_sql('products.sql'))            
            filters = self._get_database(get_file_sql('filters.sql'))

            products = products.order('erpId')
            filters = filters.order('id')
            
            for product in products:                            
                for filter_item in filters:
                    if filter_item.get_id == product_item.id:
                        product_item.add_filters(filter_item)

                self.__id_products_database.append(product_item.id)
                self.__products_database.append(product_item)

            return self.__products_database
        except:
            return None

    def get_id_products_api(self):
        return self.__id_products_api
    
    def get_id_products_database(self):
        return self.__id_products_database