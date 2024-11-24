# product.py

class Product:
    def __init__(self, name, price, active=True):
        self.name = name
        self.price = price
        self.active = active

    def update_price(self, new_price):
       # price of the product update#
        self.price = new_price

    def suspend(self):
       #product suspension, making it unavailable for new policyholders #
        self.active = False

    def reactivate(self):
       # Reactivate the product #
        self.active = True

    def display_product_info(self):
       # Display of product's information #
        print(f"Product Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Active: {'Yes' if self.active else 'No'}")
        print("-" * 30)
