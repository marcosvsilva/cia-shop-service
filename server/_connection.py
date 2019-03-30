#import pyodbc
import pymssql
import pandas as pd
import json
from _config import Config, generate_log


class Connection:

    def __init__(self):
        self.__config = Config()

        try:
            server = self.__config.get_key('server')
            port = self.__config.get_key('port')
            database = self.__config.get_key('database')
            user = self.__config.get_key('uid')
            password = self.__config.get_key('pwd')

            self.__connection = pymmsql.connect(server=server, port=port, database=database, user=user, password=password)

        except pyodbc.Error as fail:
            self.__config.disable_service()
            raise Exception('exception connection, fail : {}'.format(fail))

    def sql_query(self, sql_query):
        try:
            query = pd.read_sql_query(sql_query, self.__connection)
            json_file = json.loads(query.to_json(orient='records'))            
            return json_file
        except Exception as fail:
            raise Exception('exception get sql, fail: {}'.format(fail))

    def sql_update(self, sql_update):
        try:
            if self.__config.get_key('export_update_sql_log') == 'yes':
                generate_log('update sql: {}'.format(sql_update))

            cursor = self.__connection.cursor()
            cursor.execute(sql_update)
            cursor.commit()
        except Exception as fail:
            raise Exception('exception update sql, fail: {}'.format(fail), True)

    @staticmethod
    def get_file_sql(file_name):
        with open('sqls/{}'.format(file_name)) as file:
            sql = file.read()
        return sql

connection = Connection()