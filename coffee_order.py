"""_summary_"""
#pylint: disable=invalid-name
first_name=input("Enter your name: ")
cofee=input("Enter your favourite coffee: Capuccino Espresso Latte ")
payment_option=input("Enter your payment option: Cash Credit Card Debit Card: ")
amount=5.50

# Format the out put with f string
print(f"Welcome {first_name} to our Restaurant!")
print(f"You have ordered {cofee} and payment option is: {payment_option} is this right?")
if payment_option =="1":
    print(f"Pay at cash counter {amount} dollars")
else:
    print(f" Pay {amount} dollars in the next counter")
        
    



