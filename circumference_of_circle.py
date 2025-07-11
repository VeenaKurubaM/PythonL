import math

"""circumetance of a circle"""
#ignore warnings
# This program calculates the circumference of a circle given its radius.
radius = 0
def get_radius():
    """Calculate the circumetance of a circle given its radius."""
    radius=input("Enter radius of the circle: ")
    return float(radius)

def calculate_circumference(radius):
    circumetance_of_circle=2 * math.pi * radius
    return circumetance_of_circle
def print_results(radius,calculate):
    print(f"the circumference of the circle with {radius} is {calculate}")
    return radius,calculate
# The main function to execute the program
# pylint: disable=invalid-name  

def main():
    """Main function to execute the program."""
    radius = get_radius()
    calculate = calculate_circumference(radius)
    value = print_results(radius, calculate)
    return value
calculate_circumference_circle=main()




