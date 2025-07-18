#string indexing[start:end:step]
def pallindrome_string():
    """name is pallindrom"""
    name=input("enter name: ").strip()
    print(name[::-1])
    if name[0:]== name[::-1]:
        print("name is pallndrome")
    else:
        print("name is not pallndrome")
pallindrome_string()
def credicard_fun():
    """Credirt card funs"""
    credit_card_number="1234-6789-8978-7867"
    print(f"full credit cardnumber: {credit_card_number[0:]}")
    print(f"credit card number show from 5th digit to till 8thdigit {credit_card_number[5:9]}")#credit card number show from 5th digit to till 8thdigit 6789
    print(f"credit card number show last 4 digits ****-****-****-{credit_card_number[15:19]}")
    print(f"credit card number show last 4 digits xxxx-xxxx-xxxx-{credit_card_number[-4:]}")

    print(f"credit card number show last 4 digits ****-****-****-{credit_card_number[-4:-1]}")
    print(f"credit card number 0f fisrt 4 digits {credit_card_number[:4]}")
    print(f"credit card number 0f fisrt 5th digit onwards {credit_card_number[5:]}")
    print(f"credit card number 0f every second digit {credit_card_number[::2]}")
    print(f"credit card numberof reverse {credit_card_number[::-1]}")
    
    
credicard_fun()
    
    