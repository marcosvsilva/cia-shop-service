from server.service.request import Request
from server.service.token import Token


class Controller(object):

    def __init__(self):
        token = Token()
        self._request = Request(store_name=token.store_name, token=token.token)
