class Product:

    def __init__(self, response):
        self.response = response
        self.id = response.by_key_int('id')
        self.createdAt = response.by_key_date('createdAt')
        self.updatedAt = response.by_key_date('updatedAt')
        self.name = response.by_key('name')
        self.shortDescription = response.by_key('shortDescription')
        self.brand = response.by_key_dict('brand', 'name')
        self.filters = self.get_filters()
        self.preSaleDateStart = response.by_key_date('preSaleDateStart')
        self.releaseDate = response.by_key_date('releaseDate')
        self.releaseDateEnd = response.by_key_date('releaseDateEnd')
        self.blocked = response.by_key_bool('blocked')
        self.bonus = response.by_key_int('bonus')
        self.sortOrder = response.by_key_int('sortOrder')
        self.erpId = response.by_key('erpId')

    def get_filters(self):
        filters_response = self.response.by_key_response('filters')
        filters = []
        for response in filters_response:
            filters.append(Filter(response))

        return filters

    def print_product(self):
        self.response.print_json()


class Filter(object):

    def __init__(self, response):
        self.response = response
        self.name = response.by_key('name')
        self.values = response.by_key('values')
