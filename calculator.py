"""
A calculator that can calculate the area of a given shape, as selected by the user
The calculator will be able to determine the area of the following shapes:

Circle
Triangle
Trapezoid
Square

The program should do the following:
Prompt the user to select a shape
Depending on the shape that the user selects, calculate the area of that shape
Print the area of that shape to the user

Created by Cecelia Klein
"""

from math import pi

print "Geometry calculator is starting up..."
print "What shape would you like to calculate the area of?"

option = raw_input("Enter C for Circle, T for Triangle, Z for Trapezoid or S for Square: ")

if option == "C" or option == "c":
    radius = float(raw_input("Enter radius: "))
    area = 3.141592653 * radius ** 2
    print "Area: %f" % area

elif option == "T" or option == "t":
    base = float(raw_input("Enter base: "))
    height = float(raw_input("Enter height: "))
    area = 0.5 * base * height
    print "Area: %f" % area

elif option == "Z" or option == "z":
    baseone= float(raw_input("Enter base: "))
    basetwo= float(raw_input("Enter second base: "))
    height= float(raw_input("Enter height: "))
    area= baseone + basetwo * 0.5 * height
    print "Area: %f" % area

elif option == "S" or option == "s":
    base= float(raw_input("Enter base: "))
    height= float(raw_input("Enter height: "))
    area= base * height
    print "Area: %f" % area

else:
    print "Error! Please enter; T, C, Z or S."

print "Exiting program..."
