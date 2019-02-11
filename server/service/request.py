from CiaShopServer.server.model.response import Response
import json
import requests


class Request:

    def __init__(self, token, store_name):
        self.token = token
        self.store_name = store_name

        self.request = requests.Session()
        self.protocol = 'https'
        self.version_api = 'v1'

        self.init_request()

    def init_request(self):
        authorization = {'Authorization': 'Bearer {}'.format(self.token)}
        content_type = {'Content-Type': 'application/json'}

        self.request.headers.update(authorization)
        self.request.headers.update(content_type)

    def get_list(self, list):
        url_request = '{}://{}/api/{}/{}'.format(self.protocol, self.store_name, self.version_api, list)
        request = self.request.get(url_request)
        json_request = json.loads(request.text)

        list_response = []
        for json_file in json_request:
            list_response.append(Response(json_file))

        return list_response

    def get_orders(self):
        return self.get_list('orders')