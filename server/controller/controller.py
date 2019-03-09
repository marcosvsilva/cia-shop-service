from server.service.request import Request
from server.service.token import Token


class Controller(object):

    def __init__(self):
        self.token = Token()
        self.request = Request(store_name=self.token.get_store_name(), token=self.token.get_token())
