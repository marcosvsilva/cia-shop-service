class Product(object):

    def __init__(self, response):
        self.response = response
        self.id = response.by_key_int('id')
        self.createdAt = response.by_key_date('createdAt')
        self.updatedAt = response.by_key_date('updatedAt')
        self.name = response.by_key('name')
        self.shortDescription = response.by_key('shortDescription')
        #self.brand = self.get_brand()
        self.filters = self.get_filters()
        self.preSaleDateStart = response.by_key_date('preSaleDateStart')
        self.releaseDate = response.by_key_date('releaseDate')
        self.releaseDateEnd = response.by_key_date('releaseDateEnd')
        self.blocked = response.by_key_bool('blocked')
        self.bonus = response.by_key_int('bonus')
        self.sortOrder = response.by_key_int('sortOrder')
        self.erpId = response.by_key('erpId')
        self.mainDepartmentId = response.by_key_int('mainDepartmentId')
        self.departmentsIds = response.by_key_list('departmentsIds')
        self.installmentId = response.by_key_int('installmentId')
        self.sellOutOfStock = response.by_key_bool('sellOutOfStock')
        self.sellOutOfStockMessage = response.by_key('sellOutOfStockMessage')
        self.zoom = response.by_key_bool('zoom')
        self.variantConfirmationAlert = response.by_key_bool('variantConfirmationAlert')
        self.contractAgreementMandatory = response.by_key_bool('contractAgreementMandatory')
        self.contractDescription = response.by_key('contractDescription')
        self.urlKey = response.by_key('urlKey')
        self.discountType = response.by_key('discountType')
        self.discountDateStart = response.by_key_date('discountDateStart')
        self.discountDateEnd = response.by_key_date('discountDateEnd')

    def get_brand(self):
        brand_response = self.response.by_key_response('brand')
        brand = []
        for response in brand_response:
            brand.append(Brand(response))

        return brand

    def get_filters(self):
        filters_response = self.response.by_key_response('filters')
        filters = []
        for response in filters_response:
            filters.append(Filter(response))

        return filters

    def print_product(self):
        print('Prodct id: {}'.format(self.id))
        print('Prodct createdAt: {}'.format(self.createdAt))
        print('Prodct updatedAt: {}'.format(self.updatedAt))
        print('Prodct name: {}'.format(self.name))
        print('Prodct shortDescription: {}'.format(self.shortDescription))

        #for brand in self.brand:
            #print('Brand name: {}'.format(brand.name))

        for filter in self.filters:
            print('Filer name: {}'.format(filter.name))
            print('Filer values: {}'.format(filter.values))

        print('Prodct preSaleDateStart: {}'.format(self.preSaleDateStart))
        print('Prodct releaseDate: {}'.format(self.releaseDate))
        print('Prodct releaseDateEnd: {}'.format(self.releaseDateEnd))
        print('Prodct blocked: {}'.format(self.blocked))
        print('Prodct bonus: {}'.format(self.bonus))
        print('Prodct sortOrder: {}'.format(self.sortOrder))
        print('Prodct erpId: {}'.format(self.erpId))
        print('Prodct departmentsIds: {}'.format(self.departmentsIds))
        print('Prodct installmentId: {}'.format(self.installmentId))
        print('Prodct sellOutOfStock: {}'.format(self.sellOutOfStock))
        print('Prodct sellOutOfStockMessage: {}'.format(self.sellOutOfStockMessage))
        print('Prodct zoom: {}'.format(self.zoom))
        print('Prodct variantConfirmationAlert: {}'.format(self.variantConfirmationAlert))
        print('Prodct contractAgreementMandatory: {}'.format(self.contractAgreementMandatory))
        print('Prodct contractDescription: {}'.format(self.contractDescription))
        print('Prodct urlKey: {}'.format(self.urlKey))
        print('Prodct discountType: {}'.format(self.discountType))
        print('Prodct discountDateStart: {}'.format(self.discountDateStart))
        print('Prodct discountDateEnd: {}'.format(self.discountDateEnd))


class Brand(object):

    def __init__(self, response):
        self.response = response
        self.name = response.by_key('name')


class Filter(object):

    def __init__(self, response):
        self.response = response
        self.name = response.by_key('name')
        self.values = response.by_key('values')