from fpdf import FPDF


class Invoice:
    def __init__(self, invoice_id, customer_id, transactions, total_amount, date):
        self.__invoice_id = invoice_id
        self.__customer_id = customer_id
        self.__transactions = transactions
        self.__total_amount = total_amount
        self.__date = date

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Invoice ID: {self.__invoice_id}", ln=True)
        pdf.cell(200, 10, txt=f"Customer ID: {self.__customer_id}", ln=True)
        pdf.cell(200, 10, txt=f"Date: {self.__date}", ln=True)
        pdf.cell(200, 10, txt="Transactions:", ln=True)
        for transaction in self.__transactions:
            details = transaction.get_details()
            pdf.cell(200, 10, txt=f"Product ID: {details['product_id']}, Quantity: {details['quantity']}, Price: {details['price']}", ln=True)
        pdf.cell(200, 10, txt=f"Total Amount: {self.__total_amount}", ln=True)
        pdf.output(f"invoice_{self.__invoice_id}.pdf")