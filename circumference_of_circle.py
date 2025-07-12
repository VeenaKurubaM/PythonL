import math
class circum:
    """circumetance of a circle"""
    #ignore warnings
    # This program calculates the circumference of a circle given its radius.
    radius = 0

    @staticmethod
    def get_radius():
        try:
            """Calculate the circumetance of a circle given its radius."""
            radius=input("Enter radius of the circle: ")
            return float(radius)
        except Exception as e:
            print("Invalid input, please enter a number for radius.")
        SystemExit()
    #ignore warnings
    @staticmethod
    def calculate_circumference(radius):
            circumetance_of_circle=2 * math.pi * radius
            return circumetance_of_circle
    @staticmethod
    def print_results(radius,calculate):
        print(f"the circumference of the circle with {radius} is {calculate}")
        return radius,calculate
    # The main function to execute the program
    # pylint: disable=invalid-name  
    @staticmethod
    def main():
        """Main function to execute the program."""
        radius = circum.get_radius()
        calculate = circum.calculate_circumference(radius)
        value = circum.print_results(radius, calculate)
        return value
    
circum.main()


