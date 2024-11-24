# payment.py

class Payment:
    def __init__(self, amount, date, status='pending'):
        self.amount = amount
        self.date = date
        self.status = status

    def process_payment(self):
       # Mark the payment as 'processed' 
        self.status = 'processed'

    def send_payment_reminder(self):
        #Send a reminder if payment is pending 
        if self.status == 'pending':
            print("Reminder: Your payment is still pending.")
        else:
            print("Payment has been processed.")

    def apply_penalty(self):
        #Apply penalty if payment is late 
        if self.status == 'pending':
            print("Penalty applied: Late payment")
            self.amount += 50  # Assume penalty amount is $50
        else:
            print("No penalty applied as payment is processed.")
