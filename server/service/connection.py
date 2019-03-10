import pyodbc
import pandas as pd
from server.service import Config
from server.application import Log


class Connection(object):

    def __init__(self):
        self.__log = Log()
        config = Config()

        try:
            self.__connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};" +
                                               "Server={};".format(config.database_server) +
                                               "Database={};".format(config.database) +
                                               "Trusted_Connection={};".format(config.database_trusted_connection) +
                                               "uid={};".format(config.database_uid) +
                                               "pwd={};".format(config.database_pwd))
        except pyodbc.Error as fail:
            self.__log.generate_log('Exception Connection, Error : {}'.format(fail))

    def sql_query(self, query):
        try:
            query = pd.read_sql_query(query, self.__connection)
            return query
        except Exception as fail:
            self.__log.generate_log('Exception Query, Error: {}'.format(fail))
