
# main.py
from policyholder import Policyholder
from product import Product
from payment import Payment

# Create products
product1 = Product("Health Insurance", 500)
product2 = Product("Life Insurance", 1000)

# Create policyholders
policyholder1 = Policyholder("Tolu", "P12345")
policyholder2 = Policyholder("Nejo", "P12346")

# Register the policyholders
policyholder1.register()
policyholder2.register()

# Add products to policyholders
policyholder1.add_product(product1)
policyholder2.add_product(product2)

# Create payments
payment1 = Payment(500, "2024-11-23")
payment2 = Payment(1000, "2024-11-20")

# Process payments
payment1.process_payment()
payment2.process_payment()

# Display account details for each policyholder
policyholder1.display_account_details()
policyholder2.display_account_details()

# Send reminders for payments
payment1.send_payment_reminder()
payment2.send_payment_reminder()

# Apply penalties for late payments (example for payment2)
payment2.apply_penalty()

