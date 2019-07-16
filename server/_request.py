import requests
import json
from _config import Config, Token, generate_log


class Request:

    def __init__(self):
        token = Token()
        self.__token = token.get_key('token')
        self.__store_name = token.get_key('store_name')

        self.__request = requests.Session()
        self.__protocol = 'https'
        self.__version_api = 'v1'

        self.__init_request()

    def __init_request(self):
        authorization = {'Authorization': 'Bearer {}'.format(self.__token)}
        content_type = {'Content-Type': 'application/json'}

        self.__request.headers.update(authorization)
        self.__request.headers.update(content_type)
            
    def get_list(self, table, max_id=0):
        config = Config()
        try:
            if max_id > 0:
                url_request = '{}://{}/api/{}/{}/?minId={}'.format(self.__protocol, self.__store_name,
                                                                   self.__version_api, table, max_id)
            else:
                url_request = '{}://{}/api/{}/{}'.format(self.__protocol, self.__store_name, self.__version_api, table)

            if config.get_key('export_url_request_log') == 'yes':
                generate_log('url api request: {}'.format(url_request))

            request = self.__request.get(url_request)
            request.encoding = 'utf-8'
            json_request = json.loads(request.text)

            max_register = int(config.get_key('register_max_returns'))
            if len(json_request) == max_register:
                json_request = json_request + self.get_list(table, json_request[max_register - 1]['id'])

            return json_request
        except Exception as fail:
            raise Exception('exception api request, fail: {}'.format(fail))

    def put_list(self, table, products_update):
        try:
            for key, data in products_update.items():
                url_put = '{}://{}/api/{}/{}/{}'.format(self.__protocol, self.__store_name, self.__version_api,
                                                        table, key)
                json_put = json.loads(json.dumps(data))
                response = self.__request.put(url_put, data=str(json_put))
                response_json = json.loads(response.content)

                if response.status_code == 200:
                    generate_log('update {}, key {}, success! link {}'.format(table, key, response_json['url']))
                else:
                    raise Exception('update {}, key {}, fail! fail: {}: {} - {}'.format(table,
                                                                                     key,
                                                                                     response.status_code,
                                                                                     response_json['message'],
                                                                                     response_json['errors'][0]
                                                                                     ['message']))
        except Exception as fail:
            raise Exception('exception api post, fail: {}'.format(fail))
