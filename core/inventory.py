class Inventory:
    def __init__(self):
        self.__products = {}

    def add_product(self, product):
        self.__products[product.get_details()['product_id']] = product

    def update_product(self, product_id, name=None, category=None, price=None, quantity=None):
        if product_id in self.__products:
            self.__products[product_id].update_details(name, category, price, quantity)
        
    def remove_product(self, product_id):
        if product_id in self.__products:
            del self.__products[product_id]

    def view_products(self):
        for product in self.__products.values():
            details = product.get_details()
            print(f"ID: {details['product_id']}, Name: {details['name']}, Quantity: {details['quantity']}")