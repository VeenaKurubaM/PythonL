# Output: My name is Alice and I am 30 years old.
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Alice is learning Python
# Bob is learning Java
print("{0} is learning {1}".format("Alice", "Python"))
print("{name} is learning {lang}".format(name="Bob", lang="Java"))

name = "Charlie"
age = 25
print(f"My name is {name} and I am {age} years old.")

#Numeric Formatting
num = 123.4567
print("{:.2f}".format(num))   # 123.46 (2 decimal places)
print(f"{num:.1f}")           # 123.5
print(f"{num:10.2f}")         # '    123.46' (width 10, 2 decimals)

#   Padding and Alignment
print("{:<10}".format("Hi")) # < Left Hi        
print("{:>10}".format("Hi")) # > Right.         Hi
print("{:^10}".format("Hi")) # ^ Cente.      Hi    

#Thousand Separators
num = 1000000
print("{:,}".format(num))     # 1,000,000
print(f"{num:_}")             # 1_000_000 (underscore as separator)

#Integer Formatting
num = 255
print("{:d}".format(num))     # 255 (decimal)
print("{:b}".format(num))     # 11111111 (binary)
print("{:o}".format(num))     # 377 (octal)
print("{:x}".format(num))     # ff (hex lowercase)
print("{:X}".format(num))     # FF (hex uppercase)

#Percentage
value = 0.85
print("{:.0%}".format(value))   # 85%
print(f"{value:.2%}")           # 85.00%

#String Truncation
name = "Alexander"
print("{:.5}".format(name))    # Alexa (first 5 chars)

#Combining Multiple Options
num = 12.3456
print("{:10.2f}".format(num))  # '     12.35' (width 10, 2 decimals)
print(f"{num:*>10.2f}")        # '*****12.35' (fill with '*')



