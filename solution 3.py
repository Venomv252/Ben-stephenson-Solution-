"""Exercise 3: Area of a Room

Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with."""

length = float(input("Enter length of Room(in meters)"))
breadth = float(input("Enter length of Room(in meters)"))
print("The length of room is",length,"meters")
print("The breadth of room is",breadth,"meters")
area= length * breadth
print("The area of room is ", area,"sq. meters")
