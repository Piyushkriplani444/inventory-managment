# bad_words

To run the code, please clone the repository
Move to bad_words directory

```
cd inventory-managment
```

### Create virtual environment

```
python -m venv venv
```

### Activate virtual environment

> > Windows:
>
> `venv\Scripts\activate`

> > Linux:
>
> `source venv/bin/activate`

### Install dependencies

```
pip install - r requirements.txt
```

### Help tace to run code

```
python core/main.py -h
```

#### Response

```
1. Add Product
2. View Products
3. Update Product
4. Delete Product
5. Record Sale
6. Record Return
7. Generate Invoice
8. Generate Report
9. Exit
Enter your choice: 1

```

#### Example run comand

```
Enter your choice: 1
Enter product ID: 1
Enter product name: pen
Enter product category: school
Enter product price: 2
Enter product quantity: 100

```

#### Result

```
Enter your choice: 2
ID: 1, Name: pen, Quantity: 100
```

#### Example to hit api using curl

```
curl --request GET 127.0.0.1:5000/
```

### Command to Run Test Cases

```

python -m unittest .\tests\test_inventory_system.py

```

```
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```
