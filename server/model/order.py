from CiaShopServer.server.model.discounts_fees import DiscountsFess


class Order:

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
        discounts_fees = []
        for discount_fee in self.response.by_key('discountsAndFees'):
            discounts_fees.append(DiscountsFess(discount_fee))

        return discounts_fees