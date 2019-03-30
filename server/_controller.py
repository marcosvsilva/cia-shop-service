import json
from _request import Request
from _config import Config, generate_log
from _connection import Connection


class Controller:

    def __init__(self):
        self.__request = Request()
        self.__connection = Connection()

    def _get_api(self, table):
        try:
            json_file = self.__request.get_list(table)
            self._export_json('api_{}'.format(table), json_file)
            return json_file
        except Exception as fail:
            raise Exception(fail)

    def _update_api(self, table, products_update):
        try:
            return self.__request.put_list(table, products_update)
        except Exception as fail:
            raise Exception(fail)

    def _get_database(self, sql_table, sql_query, table_columns):
        try:
            json_file = self.__connection.sql_query(sql_query, table_columns)
            self._export_json('database_{}'.format(sql_table), json_file)
            return json_file
        except Exception as fail:
            raise Exception(fail)

    def _update_database(self, sql_update, list_update):
        try:
            self.__connection.sql_update(sql_update, list_update)
        except Exception as fail:
            raise Exception(fail)

    def _get_sql(self, file_sql):
        try:
            return self.__connection.get_file_sql(file_sql)
        except Exception as fail:
            raise Exception('fail find sql file, fail: {}'.format(fail))

    @staticmethod
    def _export_json(archive_name, archive):
        try:
            config = Config()
            if config.get_key('export_requests_json') == 'yes':
                if len(archive) > 1:
                    with open('{}.json'.format(archive_name), 'w') as file:
                        json.dump(archive, file)
                else:
                    generate_log('archive {} is empty'.format(archive_name))
        except Exception as fail:
            raise Exception('fail to export json request, archive: {}, fail: {}'.format(archive_name, fail))


class ProductController(Controller):

    def __init__(self):
        super().__init__()

    def get_products_api(self):
        try:
            return self._get_api('products')    
        except Exception as fail:
            generate_log('fail get products to api, fail: {}'.format(fail), fail=True)
            return None

    def update_products_api(self, products_update):
        try:
            return self._update_api('products', products_update)
        except Exception as fail:
            generate_log('fail update products to api, fail: {}'.format(fail), fail=True)
            return None

    def get_products_database(self):
        try:
            columns_products = ['erpId', 'id', 'brand']
            columns_filters = ['erpId', 'name', 'values']
            products = self._get_database('products', self._get_sql('get_products.sql'), columns_products)
            filters_products = self._get_database('filter', self._get_sql('get_filters.sql'), columns_filters)

            if (len(products) > 0) and (len(filters_products) > 0):
                for product in products:
                    product = self.__add_brand_product(product)
                    filters = filter(lambda x: x['erpId'] == product['erpId'], filters_products)
                    for filter_product in filters:
                        self.__add_filter_product(product, filter_product)

            self._export_json('database_products_final', products)
            return products
        except Exception as fail:
            generate_log('fail to database request products, fail: {}'.format(fail), fail=True)
            return None

    def update_products_database(self, keys_values):
        for key, value in keys_values.items():
            try:
                list_update = [(value, key)]
                sql_update = self._get_sql('update_csi_id_products.sql')
                self._update_database(sql_update, list_update)
                generate_log('update database: product {} ciashop_id {}'.format(key, str(value)))
            except Exception as fail:
                generate_log('fail to database update product {}, fail: {}'.format(key, fail), fail=True)

    @staticmethod
    def __add_filter_product(product, filter_product):
        list_filters = []
        if 'filter' in product:
            list_filters = product['filter']

        list_filters.append({'name': filter_product['name'], 'values': [filter_product['values']]})
        product['filter'] = list_filters
        return product

    @staticmethod
    def __add_brand_product(product):
        brand_value = product['brand']
        product['brand'] = {'name': brand_value}
        return product
