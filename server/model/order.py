from CiaShopServer.server.model.discounts_fees import DiscountsFess


class Order(object):

    def __init__(self, response):
        self.response = response
        self.id = response.by_key_int('id')
        self.createdAt = response.by_key_date('createdAt')
        self.updatedAt = response.by_key_date('updatedAt')
        self.deliveredAt = response.by_key_date('deliveredAt')
        self.deliveryEstimatedDate = response.by_key_date('deliveryEstimatedDate')
        self.status = response.by_key('status')
        self.cancellationReason = response.by_key('cancellationReason')
        self.statusMsgStore = response.by_key('statusMsgStore')
        self.statusMsgCustomer = response.by_key('statusMsgCustomer')
        self.templateId = response.by_key_int('id')
        self.subtotal = response.by_key_float('subtotal')
        self.discountsAndFees = self.get_discounts_fees()

    def get_discounts_fees(self):
        discounts_fees_response = self.response.by_key_response('discountsAndFees')
        discounts_fees = []
        for discount_fee in discounts_fees_response:
            discounts_fees.append(DiscountsFess(discount_fee))

        return discounts_fees

    def print_order(self):
        print('Order id: {}'.format(self.id))
        print('Order createdAt: {}'.format(self.createdAt))
        print('Order updatedAt: {}'.format(self.updatedAt))
        print('Order deliveredAt: {}'.format(self.deliveredAt))
        print('Order deliveryEstimatedDate: {}'.format(self.deliveryEstimatedDate))
        print('Order status: {}'.format(self.status))
        print('Order cancellationReason: {}'.format(self.cancellationReason))
        print('Order statusMsgStore: {}'.format(self.statusMsgStore))
        print('Order statusMsgCustomer: {}'.format(self.statusMsgCustomer))
        print('Order templateId: {}'.format(self.templateId))
        print('Order subtotal: {}'.format(self.subtotal))
        for discont_fee in self.discountsAndFees:
            print('Discount type: {}'.format(discont_fee.type))
            print('Discount value: {}'.format(discont_fee.value))
            print('Discount description: {}'.format(discont_fee.description))
            print('Discount source: {}'.format(discont_fee.source))