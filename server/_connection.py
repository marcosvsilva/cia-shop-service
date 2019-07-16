import pymssql
from _config import Config, Token, generate_log


class Connection:

    def __init__(self):
        try:
            token = Token()

            server = token.get_key('server')
            port = token.get_key('port')
            database = token.get_key('database')
            user = token.get_key('uid')
            password = token.get_key('pwd')

            if port != '':
                self.__connection = pymssql.connect(server=server, port=port, database=database, user=user,
                                                    password=password)
            else:
                self.__connection = pymssql.connect(server=server, database=database, user=user, password=password)

        except pymssql.Error as fail:
            raise Exception('exception connection, fail : {}'.format(fail))

    def sql_query(self, sql_query, table_columns):
        try:
            cursor = self.__connection.cursor()
            cursor.execute(sql_query)
            row = cursor.fetchone()
            response = []
            while row:
                row_json = {}
                index_column = 0
                for column in table_columns:
                    row_json.update({column: row[index_column]})
                    index_column += 1
                response.append(row_json)
                row = cursor.fetchone()

            return response
        except Exception as fail:
            raise Exception('exception get sql, fail: {}'.format(fail))

    def sql_update(self, sql_update, list_update):
        try:
            config = Config()
            if config.get_key('export_update_sql_log') == 'yes':
                generate_log('update sql: {}'.format(sql_update))

            cursor = self.__connection.cursor()
            cursor.executemany(sql_update, list_update)
            self.__connection.commit()
        except Exception as fail:
            self.__connection.rollback()
            raise Exception('exception update sql {}, fail: {}'.format(sql_update, fail), True)
    
    def sql_execute(self, sql_script):
        try:
            config = Config()
            if config.get_key('export_update_sql_log') == 'yes':
                generate_log('update sql: {}'.format(sql_script))

            cursor = self.__connection.cursor()
            cursor.execute(sql_script)
            self.__connection.commit()
        except Exception as fail:
            self.__connection.rollback()
            raise Exception('exception update sql {}, fail: {}'.format(sql_script, fail), True)

    @staticmethod
    def get_file_sql(file_name):
        with open('sqls//{}'.format(file_name)) as file:
            sql = file.read()
        return sql
