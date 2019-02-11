import json
import pprint
from datetime import datetime


class Response:

    def __init__(self, json_file):
        self.json_file = json_file

    def print_json(self):
        pprint.pprint(self.json_file)

    def by_key(self, key):
        return self.json_file[key]

    def by_key_float(self, key):
        return float(self.by_key(key))

    def by_key_int(self, key):
        return int(self.by_key_float(key))

    def by_key_date(self, key):
        return self.parse_date(self.by_key(key))

    @staticmethod
    def parse_date(date):
        result = None
        try:
            if date != '':
                result = datetime.strptime(date, '%Y-%m-%d')
        except:
            result = None

        return result
