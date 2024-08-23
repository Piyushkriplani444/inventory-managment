import csv

class CSVGenerator:
    def __init__(self, filename):
        self.filename = filename

    def write_to_csv(self, data):
        if not data:
            print("No data provided to write.")
            return

        dataset = [ ]
        for transaction in data:
            details = transaction.get_details()
            dataset.append(details)
        # Extract the headers from the keys of the first dictionary
        
        headers =  ['transaction_id', 'product_id', 'quantity', 'price', 'date','reason']
    
        with open(self.filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(dataset)

        print(f"CSV file '{self.filename}' created successfully.")

