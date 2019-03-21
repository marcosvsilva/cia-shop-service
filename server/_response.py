import json
import pprint
from datetime import datetime


class Response:

    def __init__(self, json_file):
        self.json_file = json_file

    def get_json(self):
        return self.json_file
    
    def print_json(self):
        pprint.pprint(self.json_file)

    def get_id(self):
        return self.by_key('id')

    def get_erpId(self):
        return self.by_key('erpId')

    def by_key(self, key):
        return self.json_file[key]

    def by_key_float(self, key):
        result = 0
        if is_valid(self.by_key(key)):
            result = float(self.by_key(key))

        return result

    def by_key_int(self, key):
        result = int(self.by_key_float(key))
        return result

    def by_key_date(self, key):
        return parse_date(self.by_key(key))

    def by_key_bool(self, key):
        return self.by_key(key) == 'true'

    def by_key_dict(self, key, value):
        return self.by_key(key)[value]

    def by_key_list(self, key):
        result = []

        for json_file in self.by_key(key):
            result.append(json_file)

        return result

    def by_key_response(self, key):
        list_response_key = []

        for json_file in self.by_key(key):
            list_response_key.append(Response(json_file))

        return list_response_key
    
    def adict(self, key, response_add):
        return self.json_file[key].append(response_add.get_json)        
    
    def order(self, order, reverse=False):
        return sorted(self.json_file, key=lambda x: x[order], reverse=reverse)        
        


def parse_date(date):
    result = None

    try:
        if date != '':
            result = datetime.strptime(date, '%Y-%m-%d')
    except:
        result = None

    return result


def is_valid(number):
    result = False
    if number is not None:
        if number != '':
            result = True

    return result
