temp=input("Enter the temperature in Celcisus: ")
is_raining=input("Is it raining outside?(Y/N): ").upper()
is_sunny=input("Is it sunny outside?(Y/N): ").upper()
temp=float(temp)

if is_raining and temp < 10:
    print("Weather is not suitable for outdoor activities")

elif temp > 35 or is_sunny:
    print("Weather is suitable for outdoor activities but too hot")
    print("You can go for a walk or play outside")
else:
    print("Weather is suitable for outdoor or indoor activities")
 
    