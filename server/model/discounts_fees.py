class DiscountsFess(object):

    def __init__(self, response):
        self.response = response
        self.type = response.by_key('type')
        self.value = response.by_key_float('value')
        self.description = response.by_key('description')
        self.source = response.by_key('source')