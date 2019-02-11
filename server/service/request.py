from CiaShopServer.server.model.response import Response
import requests


class Request(object):

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
        return self.request.get(url_request)

    def get_orders(self):
        resquest = self.get_list('orders')
        return Response(resquest.text)