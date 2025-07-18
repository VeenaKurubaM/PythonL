age =int(input("Enter your age: "))
while age<=0:
    print("please enter valid age ")
    age =int(input("Enter your age: "))
print(f"your age is {age}")

#food  order
food=input("Please enter the food to order ( q to quit) ")
while not food == "q":
    
    print(f"you like {food} ")
    food=input("please enter another food  to order (q to quit) ")
print("Bye")

def is_palindrome(x: int) -> bool:
    if x < 0:
        return False  # Negative numbers are never palindromes
    
    original = x
    reversed_num = 0
    
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    
    return original == reversed_num

# Examples
print(is_palindrome(121))   # True
print(is_palindrome(-121))  # False
print(is_palindrome(10))    # False
