
class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.__product_id = product_id
        self.__name = name
        self.__category = category
        self.__price = price
        self.__quantity = quantity

    def update_quantity(self, quantity):
        self.__quantity += quantity
    
    def update_details(self, name=None, category=None, price=None, quantity=None):
        if name:
            self.__name = name
        if category:
            self.__category = category
        if price:
            self.__price = price
        if quantity is not None:
            self.__quantity = quantity


    def get_details(self):
        return {
            'product_id': self.__product_id,
            'name': self.__name,
            'category': self.__category,
            'price': self.__price,
            'quantity': self.__quantity
        }