import requests
import json

class Request:
      token = ''
      store_name = ''
      protocol = 'https'

      authorization = {'Authorization': 'Bearer {}'.format(key)}
      content_type = {'Content-Type': 'application/json'}

      request = requests.Session()
      request.headers.update(authorization)
      request.headers.update(content_type)



      def __init__(self, token, store_name):
            self.store_name = store_name
            self.token = token


      def get_orders(self):
            url_request = '{}://{}/api/v1/orders'.format(self.protocol, self.store_name)
            response = self.request.get(url_request)
            response_json = json.loads(response.text)
            return response_json