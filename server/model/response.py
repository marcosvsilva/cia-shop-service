import pprint
from datetime import datetime


class Response(object):

    def __init__(self, json_file):
        self.json_file = json_file

    def print_json(self):
        pprint.pprint(self.json_file)

    def by_key(self, key):
        return self.json_file[key]

    def by_key_float(self, key):
        result = 0
        if self.is_valid(self.by_key(key)):
            result = float(self.by_key(key))

        return result

    def by_key_int(self, key):
        result = int(self.by_key_float(key))
        return result

    def by_key_date(self, key):
        return self.parse_date(self.by_key(key))

    def by_key_bool(self, key):
        return self.by_key(key) == 'true'

    def by_key_list(self, key):
        list = []

        for json_file in self.by_key(key):
            list.append(json_file)

        return list

    def by_key_response(self, key):
        list_response_key = []

        for json_file in self.by_key(key):
            list_response_key.append(Response(json_file))

        return list_response_key

    @staticmethod
    def parse_date(date):
        result = None
        try:
            if date != '':
                result = datetime.strptime(date, '%Y-%m-%d')
        except:
            result = None

        return result

    @staticmethod
    def is_valid(number):
        result = False
        if number is not None:
            if number != '':
                result = True

        return result