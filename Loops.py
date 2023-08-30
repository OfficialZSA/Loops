# Author: Zaid A.Yusuf
# Date: 08/29/2023
# Python Loops

#
#1a#
#
#This method categorises pH values as acidic, neutral, or alkali
#
#The word 'VERY' if the pH value is more than 3 units away from 7.
#
# Return a string representing the classification of the pH value.
def classify_ph(pH):
    if pH > 7:
        if pH > 3:
            return "VERY alkali"
        else:
            return "alkali"
    elif pH == 7:
        return "neutral"
    else:
        if ph < 3:
            return "VERY acidic"
        else:
            return "acidic"
#
#1b#
#
def is_habitable(min_temp, max_temp):

# This program assesses if a planet is livable depending on its ambient temperature.
#
# Min-Max temp is a decimal floating-point value that represents the lowest temperature in degrees Celsius.
#
# Return A string indicating if there is liquid water, whether crops can bloom, and whether the planet is sustainable.

    water_present = "Liquid water can be present." if min_temp > 0 and max_temp < 100 else "Liquid water cannot be present."
    crops_grow = "Crops can grow." if min_temp > 21 and max_temp < 32 else "Crops cannot grow."
    habitable = "The planet is habitable." if "Liquid water can be present." in water_present and "Crops can grow." in crops_grow else "The planet is not habitable."

    return f"{water_present} {crops_grow} {habitable}"

#1c#
def triangle_type(a: int, b: int, c: int) -> str:
    
# Return a message identifying the kind of triangle as well as whether the provided edges constitute a valid triangle.
#
    # Args:
        # a (int): The length of side a.
        # b (int): The length of side b.
        # c (int): The length of side c.
#
#Return a message identifying the kind of triangle and whether the specified sides make up a valid triangular.

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "This is an equilateral triangle."
        elif a == b or b == c or c == a:
            return "This is an isosceles triangle."
        else:
            return "This is a scalene triangle."
    else:
        return "These sides do not form a valid triangle."
#
#2#
#
# The application will keep asking for input until the user types "quit."
#
while True:
    user_input = input("Enter pH value (or 'quit' to exit): ")
    if user_input == "quit":
        break
    try:
        pH = float(user_input)
        if pH > 9 or pH < 3:
            print("VERY " + ("alkali" if pH > 7 else "acidic"))
        elif pH == 7:
            print("neutral")
        else:
            print("alkali" if pH > 7 else "acidic")
    except ValueError:
        print("Invalid input. To continue, you must input a positive floating point numeric value that is acceptable or enter 'quit'.")

