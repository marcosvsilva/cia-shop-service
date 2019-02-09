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

    def get_orders(self):
        url_request = '{}://{}/api/{}/orders'.format(self.protocol, self.store_name, self.version_api)
        return self.request.get(url_request)
