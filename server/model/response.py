import json
import pprint


class Response(object):

    def __init__(self, request):
        self.json = json.loads(request.text)

    def printr(self):
        pprint.pprint(self.json)