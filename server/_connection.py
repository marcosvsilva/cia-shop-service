import pymssql
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

            if port != '':
                self.__connection = pymssql.connect(server=server, port=port, database=database, user=user,
                                                    password=password)
            else:
                self.__connection = pymssql.connect(server=server, database=database, user=user, password=password)

        except pymssql.Error as fail:
            self.__config.disable_service()
            print(fail)
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
            if self.__config.get_key('export_update_sql_log') == 'yes':
                generate_log('update sql: {}'.format(sql_update))

            cursor = self.__connection.cursor()
            cursor.executemany(sql_update, list_update)
            cursor.commit()
        except Exception as fail:
            raise Exception('exception update sql {}, fail: {}'.format(sql_update, fail), True)

    @staticmethod
    def get_file_sql(file_name):
        with open('sqls/{}'.format(file_name)) as file:
            sql = file.read()
        return sql
