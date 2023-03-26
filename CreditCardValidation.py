from flask import Flask, request
from flask_jwt_extended import JWTManager, jwt_required
from flask_restful import Api, Resource
import re
import tkinter as tk
from tkinter import messagebox

# Create a Tkinter window
window = tk.Tk()
window.title("Credit Card Validator")
window.geometry('400x150')

# Create a label for the credit card number
label = tk.Label(window, text="Enter credit card number:")
label.pack(padx=10, pady=10)

# Create a text entry box for the credit card number
entry = tk.Entry(window, width=30)
entry.pack(padx=10, pady=10)

# Define a function to validate the credit card number
def validate_credit_card_number():
    # Get the credit card number from the entry box
    card_number = entry.get()

    # Remove all non-numeric characters from the card number
    card_number = re.sub('[^0-9]', '', card_number)

    # Check if the card number matches the format for each type of card
    if re.match(r'^4[0-9]{12}(?:[0-9]{3})?$', card_number): # Visa
        messagebox.showinfo("Credit Card Validator", "Valid Visa credit card number")
    elif re.match(r'^5[1-5][0-9]{14}$', card_number): # Mastercard
        messagebox.showinfo("Credit Card Validator", "Valid Mastercard credit card number")
    elif re.match(r'^3[47][0-9]{13}$', card_number): # American Express
        messagebox.showinfo("Credit Card Validator", "Valid American Express credit card number")
    elif re.match(r'^6(?:011|5[0-9]{2})[0-9]{12}$', card_number): # Discover
        messagebox.showinfo("Credit Card Validator", "Valid Discover credit card number")
    elif re.match(r'^(?:2131|1800|35\d{3})\d{11}$', card_number): # JCB
        messagebox.showinfo("Credit Card Validator", "Valid JCB credit card number")
    else:
        messagebox.showwarning("Credit Card Validator", "Invalid credit card number")

# Create a button to validate the credit card number
button = tk.Button(window, text="Validate", command=validate_credit_card_number)
button.pack(padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
