import pyodbc
import pandas as pd
import json
from _config import Config, generate_log


class Connection:

    def __init__(self):
        self.__config = Config()

        try:
            self.__connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};" +
                                               "Server={};".format(self.__config.database_server) +
                                               "Database={};".format(self.__config.database) +
                                               "Trusted_Connection={};".format(self.__config.
                                                                               database_trusted_connection) +
                                               "uid={};".format(self.__config.database_uid) +
                                               "pwd={};".format(self.__config.database_pwd))
        except pyodbc.Error as fail:
            generate_log('exception connection, fail : {}'.format(fail))

    def sql_query(self, sql_query):
        try:
            query = pd.read_sql_query(sql_query, self.__connection)
            json_file = json.loads(query.to_json(orient='records'))            
            return json_file
        except Exception as fail:
            generate_log('exception get sql, fail: {}'.format(fail))
            return None

    def sql_update(self, sql_update):
        try:
            if self.__config.system_export_update_sql_log:
                generate_log('update sql: {}'.format(sql_update))

            cursor = self.__connection.cursor()
            cursor.execute(sql_update)
            cursor.commit()
        except Exception as fail:
            generate_log('exception update sql, fail: {}'.format(fail))

    @staticmethod
    def get_file_sql(file_name):
        with open('sqls/{}'.format(file_name)) as file:
            sql = file.read()
        return sql
