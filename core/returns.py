from transaction import Transaction

class Return(Transaction):
    def __init__(self, transaction_id, product_id, quantity, price, date, reason):
        super().__init__(transaction_id, product_id, quantity, price, date)
        self.__reason = reason

    def get_details(self):
        details = super().get_details()
        details['reason'] = self.__reason
        return details