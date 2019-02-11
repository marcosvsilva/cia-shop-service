class DiscountsFess:

    def __init__(self, response):
        self.code = response.by_key('code')
        self.type = response.by_key('type')
        self.value = response.by_key_float('value')
        self.description = response.by_key('description')
        self.source = response.by_key('source')