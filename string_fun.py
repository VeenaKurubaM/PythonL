"""_String functions in Python_"""
print(help(str))
first_name=input("Enter your first name:")
#captlize function to convert the fisrt character of the string to uppder case
first_name=first_name.capitalize()
last_name=input("Enter your last name:")
phone_number=input("Enter phone number: ")
# tocheck count of -'s in phone number
phone_number_count=phone_number.count("-")
print(phone_number_count)
#replcing one character with other character
phone_number=phone_number.replace("-"," ")
print(phone_number)
#to check isdigits method to check only if digits
print(last_name.isdigit())
#to check isalpha method to check only if alphabets
print(last_name.isalpha())
#convert all characters in the string to upper case
last_name=last_name.upper()
#convert all characters in the string to lower case
#last_name=last_name.lower()
print(f"Hello {last_name}")
#pylint: disable=invalid-name
#length of the string to find first ocurence of character in given string
print(f"Hello {first_name}")
print(f"First name length: {len(first_name)}")
find_first=first_name.find(input("Enter the character you want to find: "))
print(f"The first occurence of given character in {first_name} is {find_first}")
#find the last occurence of character of given string
find_last=first_name.rfind(input("Enter last given chanracter in the string: "))
print(f"The last occurence of given character in {first_name} is {find_last}")
# to find all string methods
print(help(str))
