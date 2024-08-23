from product import Product
from inventory import Inventory
from datetime import datetime
from sale import Sale
from invoice import Invoice
from returns import Return
from csv_generator import CSVGenerator

def main():
    inventory = Inventory()
    transactions = []
    alltransactions = []

    while True:
        print("\n1. Add Product\n2. View Products\n3. Update Product\n4. Delete Product\n5. Record Sale\n6. Record Return\n7. Generate Invoice\n8. Generate Report\n9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(product_id, name, category, price, quantity)
            inventory.add_product(product)
        elif choice == '2':
            inventory.view_products()
        elif choice == '3':
            product_id = input("Enter product ID to update: ")
            name = input("Enter new product name (leave blank to keep current): ")
            category = input("Enter new product category (leave blank to keep current): ")
            price = input("Enter new product price (leave blank to keep current): ")
            quantity = input("Enter new product quantity (leave blank to keep current): ")
            inventory.update_product(product_id, name or None, category or None, float(price) if price else None, int(quantity) if quantity else None)
        elif choice == '4':
            product_id = input("Enter product ID to delete: ")
            inventory.remove_product(product_id)
        elif choice == '5':
            transaction_id = input("Enter transaction ID: ")
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity sold: "))
            price = float(input("Enter sale price: "))
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sale = Sale(transaction_id, product_id, quantity, price, date)
            transactions.append(sale)
            alltransactions.append(sale)
            inventory.update_product(product_id, -quantity)
        elif choice == '6':
            transaction_id = input("Enter transaction ID: ")
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity returned: "))
            price = float(input("Enter return price: "))
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            reason = input("Enter reason for return: ")
            return_transaction = Return(transaction_id, product_id, quantity, price, date, reason)
            transactions.append(return_transaction)
            alltransactions.append(return_transaction)
            inventory.update_product(product_id, quantity)
        elif choice == '7':
            invoice_id = input("Enter invoice ID: ")
            customer_id = input("Enter customer ID: ")
            total_amount = sum([t.get_details()['price'] * t.get_details()['quantity'] for t in transactions])
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            invoice = Invoice(invoice_id, customer_id, transactions, total_amount, date)
            invoice.generate_pdf()
            transactions.clear()
        elif choice == '8':
            file = CSVGenerator('report.csv')
            file.write_to_csv(alltransactions)
            
        elif choice == '9':
            break

if __name__ == "__main__":
    main()
