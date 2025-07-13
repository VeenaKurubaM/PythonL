class activity_recomender:
    """class to recommend activities based on weather conditions"""
    #ignore python warnings
    @staticmethod
    def main():
        """Main function to check the weather conditions for outdoor activitiees"""
        temp=input("Enter the temperature in Celcisus: ")
        is_raining=False
        is_sunny=False
        
        temp=float(temp)

        if is_raining or temp < 10:
            print("Weather is not suitable for outdoor activities")
        elif 10 < temp <= 20 and not is_sunny:
            print("Weather is cloudy but suitable for outdoor activities")
            print("You can go for a walk or play outside")
    
        elif temp > 35 or is_sunny:
            print("Weather is suitable for outdoor activities but too hot")
            print("You can go for a walk or play outside")

        else:
            print("Weather is suitable for outdoor or indoor activities")
activity_recomender.main()

 
    