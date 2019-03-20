class Product:

    def __init__(self, response):
        self.response = response
        self.id = response.by_key_int('erpId')
        self.apiId = response.get_id()
        self.filters = self.get_filters()

    def get_filters(self):
        filters_response = self.response.by_key_response('filters')
        filters = []
        for response in filters_response:
            filters.append(Filter(response))

        return filters

    def add_filters(self, filters_response):
        if filters_response.by_key == self.id:
            self.filters.append(Filter(filters_response))

    def describe(self):
        describe = ['product', 'id: {}'.format(self.id), 'apiId: {}'.format(self.apiId)]

        for filter in self.filters:
            describe.append('filter name: {}'.format(filter.name))
            describe.append('filter value: {}'.format(filter.values))

        return '\n'.join(describe)


class Filter:

    def __init__(self, response):
        self.response = response
        self.name = response.by_key('name')
        self.values = response.by_key('values')
