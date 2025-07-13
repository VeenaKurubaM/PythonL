"""_summary_"""
#pylint: disable=invalid-name

first_name=input("Enter your name: ")

cofee=input("What Coffee do you want to order?: Capuccino Espresso Latte Mocha Frappe: ")
payment_option=input("Enter your payment option: Cash Credit Card Debit Card: ")
amount=5.50



# Format the output with f string
# pylint: disable=invalid-name

print(f"Welcome {first_name} to our Cafe!")
print(f"You have ordered {cofee} and payment option is: {payment_option} is this right?")
if payment_option =="Cash":
    print(f"Pay {amount} at cash counter dollars")
else:
    print(f" Pay {amount} dollars in the next counter")
you_are_done=True
if you_are_done:
    print("Thank you for visiting our restaurant!")
       



