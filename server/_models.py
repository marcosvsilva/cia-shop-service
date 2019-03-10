class Product:

    def __init__(self, response):
        self.response = response
        self.id = response.by_key_int('id')
        self.erpId = response.by_key('erpId')
        self.filter = self.get_filters()

    def get_filters(self):
        filters_response = self.response.by_key_response('filters')
        filters = []
        for response in filters_response:
            filters.append(Filter(response))

        return filters


class Filter:

    def __init__(self, response):
        self.response = response
        self.name = response.by_key('name')
        self.values = response.by_key('values')
