#ignore warnings
value=input("Enter your expression: ")

if not value:
    print("No input provided")
    exit()
else:
    try:
        # Using eval to evaluate the user input
        user_value=eval(value)

        print(type(user_value))

        if type(user_value) is float:
    
            int_value=int(user_value)
            print(f"Convert float values to int for{user_value} is {int_value}")

        else:
            print(f"The user input value is not float, so user entered value is {user_value} ")
    except Exception as e:
        print(f"Input is not valid:{value}")


