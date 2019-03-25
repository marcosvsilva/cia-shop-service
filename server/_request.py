import requests
import json
from _config import Config, generate_log


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
            
    def get_list(self, table, max_id=0):
        try:
            if max_id > 0:
                url_request = '{}://{}/api/{}/{}/?minId={}'.format(self.protocol, self.store_name, self.version_api, table,
                                                                   max_id)
            else:
                url_request = '{}://{}/api/{}/{}'.format(self.protocol, self.store_name, self.version_api, table)

            config = Config()
            if config.system_export_url_request_log:
                generate_log('url api request: {}'.format(url_request))

            request = self.request.get(url_request)
            json_request = json.loads(request.text)

            if len(json_request) == config.system_register_max_returns:
                json_request = json_request + self.get_list(table, json_request[config.system_register_max_returns - 1]['id'])

            return json_request
        except Exception as fail:
            generate_log('exception api request, fail: {}'.format(fail))
            return None
