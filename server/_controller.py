import json
from _request import Request
from _config import Config, Token, generate_log
from _connection import Connection


class Controller:

    def __init__(self):
        token = Token()
        self.__request = Request(store_name=token.store_name, token=token.token)
        self.__connection = Connection()
        self.__config = Config()

    def _get_api(self, table):
        try:
            json_file = self.__request.get_list(table)
            self._export_json('api_{}'.format(table), json_file)
            return json_file
        except Exception as fail:
            generate_log('fail to api request, table: {}, fail: {}'.format(table, fail))
            return None

    def _get_database(self, sql_table, sql_query):
        try:
            json_file = self.__connection.sql_query(sql_query)
            self._export_json('database_{}'.format(sql_table), json_file)
            return json_file
        except Exception as fail:
            generate_log('fail to database request, table: {}, fail: {}'.format(sql_table, fail))
            return None

    def _update_database(self, sql_table, sql_update):
        try:
            self.__connection.sql_update(sql_update)
        except Exception as fail:
            generate_log('fail to database update, table: {}, fail: {}'.format(sql_table, fail))

    def _export_json(self, archive_name, archive):
        try:
            if self.__config.system_export_requests_json:
                if len(archive) > 1:
                    with open('{}.json'.format(archive_name), 'w') as file:
                        json.dump(archive, file)
                else:
                    generate_log('archive {} is empty'.format(archive_name))
        except Exception as fail:
            generate_log('fail to export json request, archive: {}, fail: {}'.format(archive_name, fail))

    def _get_sql(self, file_sql):
        try:
            return self.__connection.get_file_sql(file_sql)
        except Exception as fail:
            generate_log('fail find sql file, fail: {}'.format(fail))
            return None


class ProductController(Controller):

    def __init__(self):
        super().__init__()
        self.get_products_api()
        self.get_products_database()

    def get_products_api(self):
        json_api = self._get_api('products')

        if len(json_api) > 0:
            return json_api
        else:
            return None

    def get_products_database(self):
        try:
            products = self._get_database('products', self._get_sql('get_products.sql'))
            filters_products = self._get_database('filter', self._get_sql('get_filters.sql'))

            if (len(products) > 0) and (len(filters_products) > 0):
                for product in products:
                    filters = filter(lambda x: x['erpId'] == product['erpId'], filters_products)
                    for filter_product in filters:
                        self.__add_filter_product(product, filter_product)

            self._export_json('database_products_final', products)
            return products
        except Exception as fail:
            generate_log('fail to database request products, fail: {}'.format(fail))
            return None

    def update_products(self, keys_values):
        try:
            for key, value in keys_values.items():
                sql_update = self._get_sql('update_csi_id_products.sql')
                sql_update = sql_update.replace('%KEY%', str("'"+key+"'"))
                sql_update = sql_update.replace('%VALUE%', str(value))
                self._update_database('products', sql_update)
        except Exception as fail:
            generate_log('fail to database update products, fail: {}'.format(fail))

    @staticmethod
    def __add_filter_product(product, filter_product):
        list_filters = []
        if 'filter' in product:
            list_filters = product['filter']

        list_filters.append({'name': filter_product['name'], 'values': [filter_product['values']]})
        product['filter'] = list_filters
        return product
