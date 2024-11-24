{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8a9c3722-1d53-4399-9bcb-3be180ae5b5c",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Payment:\n",
    "    def __init__(self, payment_id, policyholder_id, product_id, amount):\n",
    "   \n",
    "        #payment with an ID, associated policyholder and product IDs, amount, and pending status by default#\n",
    "       \n",
    "        self.payment_id = payment_id\n",
    "        self.policyholder_id = policyholder_id\n",
    "        self.product_id = product_id\n",
    "        self.amount = amount\n",
    "        self.status = \"pending\"\n",
    "\n",
    "    def process_payment(self):\n",
    "       \n",
    "        #payment marked as paid#\n",
    "        \n",
    "        self.status = \"paid\"\n",
    "\n",
    "    def apply_penalty(self, penalty_amount):\n",
    "        \n",
    "        #Apply a penalty to the payment amount#\n",
    "    \n",
    "        self.amount += penalty_amount\n",
    "        self.status = \"penalty_applied\"\n",
    "\n",
    "    def send_reminder(self):\n",
    "       \n",
    "        #reminder message#\n",
    "       \n",
    "        return f\"Reminder: Payment of ${self.amount} for Policyholder ID {self.policyholder_id} is pending.\"\n",
    "\n",
    "    def get_details(self):\n",
    "       \n",
    "        #Return payment details as a dictionary#\n",
    "        \n",
    "        return {\n",
    "            \"Payment ID\": self.payment_id,\n",
    "            \"Policyholder ID\": self.policyholder_id,\n",
    "            \"Product ID\": self.product_id,\n",
    "            \"Amount\": self.amount,\n",
    "            \"Status\": self.status,\n",
    "        }\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70d76e59-6dcb-4f40-9fa0-b8bddf10fd1e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
