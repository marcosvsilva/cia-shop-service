import pyodbc
import pandas as pd
import json
from _config import Config, generate_log
from _request import Response


class Connection:

    def __init__(self):
        config = Config()
        
        driver = '/Library/Vertica/ODBC/lib/libverticaodbc.dylib'

        try:
            self.__connection = pyodbc.connect("Driver={" + driver + "};" +
                                               "Server={};".format(config.database_server) +
                                               "Database={};".format(config.database) +
                                               "Trusted_Connection={};".format(config.database_trusted_connection) +
                                               "uid={};".format(config.database_uid) +
                                               "pwd={};".format(config.database_pwd))
        except pyodbc.Error as fail:
            generate_log('Exception Connection, Error : {}'.format(fail))

    def sql_query(self, sql_query):
        responses = []

        try:
            query = pd.read_sql_query(sql_query, self.__connection)
            json_file = json.loads(query.to_json(orient='records'))

            for item in json_file:
                response = Response(item)
                responses.append(response)

        except Exception as fail:
            generate_log('Exception Query, Error: {}'.format(fail))

        return responses
