class Transaction:
    def __init__(self, transaction_id, product_id, quantity, price, date):
        self.__transaction_id = transaction_id
        self.__product_id = product_id
        self.__quantity = quantity
        self.__price = price
        self.__date = date

    def get_details(self):
        return {
            'transaction_id': self.__transaction_id,
            'product_id': self.__product_id,
            'quantity': self.__quantity,
            'price': self.__price,
            'date': self.__date
        }