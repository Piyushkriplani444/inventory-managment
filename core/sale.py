from transaction import Transaction
# from core.transaction import Transaction

class Sale(Transaction):
    def __init__(self, transaction_id, product_id, quantity, price, date):
        super().__init__(transaction_id, product_id, quantity, price, date)

