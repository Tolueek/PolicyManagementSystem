# policyholder.py

class Policyholder:
    def __init__(self, name, policy_number, status='active'):
        self.name = name
        self.policy_number = policy_number
        self.status = status
        self.products = []

    def register(self):
        #Register a new policyholder as 'active' 
        self.status = 'active'

    def suspend(self):
        # Suspend a policyholder's account
        self.status = 'suspended'

    def reactivate(self):
        #Reactivate a suspended policyholder
        self.status = 'active'

    def add_product(self, product):
        # Add a policy product to the policyholder
        self.products.append(product)

    def display_account_details(self):
        # Display the policyholder's account details
        print(f"Policyholder: {self.name}")
        print(f"Policy Number: {self.policy_number}")
        print(f"Status: {self.status}")
        print("Products Purchased:")
        for product in self.products:
            print(f"- {product.name}")
        print("-" * 30)