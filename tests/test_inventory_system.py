import unittest
from datetime import datetime
from core.product import Product
from core.inventory import Inventory
from core.sale import Sale
from core.returns import Return
from core.invoice import Invoice  
from core.transaction import Transaction

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product('P001', 'Laptop', 'Electronics', 1000.0, 10)
        details = product.get_details()
        self.assertEqual(details['product_id'], 'P001')
        self.assertEqual(details['name'], 'Laptop')
        self.assertEqual(details['category'], 'Electronics')
        self.assertEqual(details['price'], 1000.0)
        self.assertEqual(details['quantity'], 10)

    def test_update_quantity(self):
        product = Product('P001', 'Laptop', 'Electronics', 1000.0, 10)
        product.update_quantity(5)
        self.assertEqual(product.get_details()['quantity'], 15)

    def test_update_details(self):
        product = Product('P001', 'Laptop', 'Electronics', 1000.0, 10)
        product.update_details(name='Gaming Laptop', price=1200.0)
        details = product.get_details()
        self.assertEqual(details['name'], 'Gaming Laptop')
        self.assertEqual(details['price'], 1200.0)

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
        self.product = Product('P001', 'Laptop', 'Electronics', 1000.0, 10)
        self.inventory.add_product(self.product)

    def test_add_product(self):
        self.assertIn('P001', self.inventory._Inventory__products)

    def test_remove_product(self):
        self.inventory.remove_product('P001')
        self.assertNotIn('P001', self.inventory._Inventory__products)

class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = Transaction('T001', 'P001', 2, 500.0, date)
        details = transaction.get_details()
        self.assertEqual(details['transaction_id'], 'T001')
        self.assertEqual(details['product_id'], 'P001')
        self.assertEqual(details['quantity'], 2)
        self.assertEqual(details['price'], 500.0)
        self.assertEqual(details['date'], date)

class TestSale(unittest.TestCase):
    def test_sale_creation(self):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sale = Sale('S001', 'P001', 2, 500.0, date)
        details = sale.get_details()
        self.assertEqual(details['transaction_id'], 'S001')
        self.assertEqual(details['product_id'], 'P001')
        self.assertEqual(details['quantity'], 2)
        self.assertEqual(details['price'], 500.0)
        self.assertEqual(details['date'], date)

class TestReturn(unittest.TestCase):
    def test_return_creation(self):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return_transaction = Return('R001', 'P001', 1, 500.0, date, 'Defective')
        details = return_transaction.get_details()
        self.assertEqual(details['transaction_id'], 'R001')
        self.assertEqual(details['product_id'], 'P001')
        self.assertEqual(details['quantity'], 1)
        self.assertEqual(details['price'], 500.0)
        self.assertEqual(details['date'], date)
        self.assertEqual(details['reason'], 'Defective')

class TestInvoice(unittest.TestCase):
    def test_invoice_creation(self):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transactions = [
            Sale('S001', 'P001', 2, 500.0, date),
            Sale('S002', 'P002', 1, 300.0, date)
        ]
        invoice = Invoice('I001', 'C001', transactions, 1300.0, date)
        self.assertEqual(invoice._Invoice__invoice_id, 'I001')
        self.assertEqual(invoice._Invoice__customer_id, 'C001')
        self.assertEqual(invoice._Invoice__total_amount, 1300.0)
        self.assertEqual(invoice._Invoice__date, date)

if __name__ == '__main__':
    unittest.main()
