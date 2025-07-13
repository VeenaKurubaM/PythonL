import math
"""This is a simple program to demonstrate the use of math module in Python."""
# ignore warnings
x=3.13
y=4
z=5.6
rounded_value=round(x)
print(f"Rounded value of {x} is {rounded_value}")
absolute_value=abs(y)
print(f"Absolute value of {y} is :{absolute_value}")
power_value=pow(y,5)
print(f"Power value of {y} is :{power_value}")
max_value=max(x,y,z)
print(f"Maximum value of {x},{y} and {z} is : {max_value}")
min_value=min(x,y,z)
print(f"Minimum value of {x},{y} and {z} is : {min_value}")
print(math.pi)
print(math.e)
squareroot_value=math.sqrt(y)
print(f"Square root of {y} is :{squareroot_value}")
#round up
roundup_value=math.ceil(x)
print(f"ceil/round up value of {x}is :{roundup_value}")
#round down
rounddown_value=math.floor(z)
print(f"floor/round down value of {z} is :{rounddown_value}")
a=input("Enter a: ")
b=input("Enter b: ")

max_number=a if a>b else b
print(f"Maximum number is :{max_number}")
min_number= a if a<b else b
print(f"Minimum number is :{min_number}")
age=int(input("Enter your age: "))
eligible_to_login="An Adult" if age >18 else "Not an adult"
print(f"User is {eligible_to_login}")


