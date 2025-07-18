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