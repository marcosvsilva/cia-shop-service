import requests
import json
from _config import Config, generate_log
from _config import Token


class Request:

    def __init__(self, token, store_name):
        self.__token = token
        self.__store_name = store_name

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
        try:
            if max_id > 0:
                url_request = '{}://{}/api/{}/{}/?minId={}'.format(self.__protocol, self.__store_name,
                                                                   self.__version_api, table, max_id)
            else:
                url_request = '{}://{}/api/{}/{}'.format(self.__protocol, self.__store_name, self.__version_api, table)

            config = Config()
            if config.system_export_url_request_log:
                generate_log('url api request: {}'.format(url_request))

            request = self.__request.get(url_request)
            request.encoding = 'utf-8'
            json_request = json.loads(request.text)

            if len(json_request) == config.system_register_max_returns:
                json_request = json_request + self.get_list(table,
                                                            json_request[config.system_register_max_returns - 1]['id'])

            return json_request
        except Exception as fail:
            generate_log('exception api request, fail: {}'.format(fail))
            return None

    def put_list(self, table, products_update):
        try:
            for key, data in products_update.items():
                url_put = '{}://{}/api/{}/{}/{}'.format(self.__protocol, self.__store_name, self.__version_api,
                                                        table, key)
                json_put = json.loads(json.dumps(data))
                response = self.__request.put(url_put, data=str(json_put))
                response_json = json.loads(response.content)

                if response.status_code == 200:
                    generate_log('update {} success! link {}'.format(table, response_json['url']))
                else:
                    generate_log('update {} fail! fail: {}: {} - {}'.format(table, response.status_code,
                                                                            response_json['message'],
                                                                            response_json['errors'][0]['message']))
        except Exception as fail:
            generate_log('exception api post, fail: {}'.format(fail))
            return None
