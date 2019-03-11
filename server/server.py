from _controller import ProductController
from _config import generate_log
from _connection import Connection
import pandas as pd


class Application:

    def __init__(self):
        product_controller = ProductController()
        #self.__products = product_controller.get_products_api()
        self.__products_database = product_controller.get_products_database()

    def synchronize(self):
        generate_log('start process')

        '''
        for product in self.__products:
            generate_log('print product')
            print('-------------------')
            print(prod
            print('-------------------')
            print('\n')
        '''

        for product in self.__products_database:
            generate_log('print product')
            print('-------------------')
            print(product.describe)
            print('-------------------')
            print('\n')


app = Application()
app.synchronize()
connection = Connection()
df = pd.DataFrame()
df = connection.sql_query('select * from CSI_PRODUTO')
print(df.keys())
print(df['PROD_ID'])