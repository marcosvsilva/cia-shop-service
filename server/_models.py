class Product:

    def __init__(self, response):
        self.response = response
        self.id = response.by_key_int('id')
        self.erpId = response.by_key_int('erpId')
        self.filter = self.get_filters()

    def get_filters(self):
        filters_response = self.response.by_key_response('filters')
        filters = []
        for response in filters_response:
            filters.append(Filter(response))

        return filters

    def add_filters(self, filters_response):
        filters = []
        for response in filters_response:
            filters.append(Filter(response))

        self.filter = filters

    def describe(self):
        describe = ['product', 'id: {}'.format(self.id), 'erpID: {}'.format(self.erpId)]

        for filter in self.filter:
            describe.append('filter name: {}'.format(filter.name))
            describe.append('filter value: {}'.format(filter.values))

        return '\n'.join(describe)


class Filter:

    def __init__(self, response):
        self.response = response
        self.name = response.by_key('name')
        self.values = response.by_key('values')
