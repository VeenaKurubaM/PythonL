Python provides a rich set of string methods that help with common operations like searching, modifying, validating, and formatting strings.

Here’s a categorized and concise overview of the most commonly used Python string methods:

🔍 Search & Find
Method	Description
find()	Returns index of first occurrence, or -1
rfind()	Returns last occurrence index
index()	Like find() but raises error if not found
count()	Counts occurrences of a substring
s = "hello world"
s.find("o")     # 4
s.count("l")    # 3
🧹 Modify / Transform
Method	Description
lower()	Converts to lowercase
upper()	Converts to uppercase
capitalize()	Capitalizes first character
title()	Capitalizes each word
strip()	Removes leading/trailing whitespace
lstrip() / rstrip()	Removes from left/right
replace(a, b)	Replaces all a with b
" hello ".strip()      # "hello"
"python rocks".title() # "Python Rocks"
📐 Check/Validate (Return Boolean)
Method	Description
startswith()	Checks if string starts with substring
endswith()	Checks if string ends with substring
isalnum()	Alphanumeric check
isalpha()	Alphabetic check
isdigit()	Digit check
isspace()	Checks if all characters are spaces
islower() / isupper()	Checks case
"abc123".isalnum()     # True
"   ".isspace()        # True
🔗 Split & Join
Method	Description
split()	Splits string into list
rsplit()	Splits from the right
splitlines()	Splits by line breaks
join()	Joins list into string
"one,two,three".split(",")  # ['one', 'two', 'three']
",".join(["a", "b", "c"])   # 'a,b,c'
🔁 Formatting
Method	Description
format()	Format with placeholders
zfill(width)	Pads string on the left with zeros
center(width)	Centers string
ljust(width) / rjust(width)	Aligns text
"Score: {}".format(95)       # "Score: 95"
"7".zfill(3)                 # "007"
🧪 Example Use Case
email = "  Veena.Kuruba@Example.COM "
cleaned = email.strip().lower()
username = cleaned.split("@")[0]
print(f"Username: {username}")
# Output: "username: veena.kuruba"
