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
        if max_id > 0:
            url_request = '{}://{}/api/{}/{}/?minId={}'.format(self.protocol, self.store_name, self.version_api, table,
                                                               max_id)
        else:
            url_request = '{}://{}/api/{}/{}'.format(self.protocol, self.store_name, self.version_api, table)
        
        config = Config()
        if config.system_print_url_request_log:
            generate_log('URL API REQUEST: {}'.format(url_request))

        request = self.request.get(url_request)
        json_request = json.loads(request.text)        
        
        if len(json_request) == 50:
            json_request.append(self.get_list(table, json_request[49]['id']))            

        return json_request
