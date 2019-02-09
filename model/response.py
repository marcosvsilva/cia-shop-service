import json


class Response:

    def __init__(self, response):
        self.json = json.loads(response.text)

    def print(self):
        print(json)
