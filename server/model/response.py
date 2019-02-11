import json
import pprint
from datetime import datetime


class Response(object):

    def __init__(self, request):
        self.json = json.loads(request.text)

    def print_json(self):
        pprint.pprint(self.json)

    def by_key(self, key):
        return self.json[key]

    def by_key_float(self, key):
        return float(self.by_key(key))

    def by_key_int(self, key):
        return int(self.by_key_float(key))

    def by_key_date(self, key):
        return self.parse_date(self.by_key(key))

    def parse_date(self, date):
        result = None
        try:
            if date != '':
                result = datetime.strptime(date, '%Y-%m-%d')
        except:
            result = None

        return result
