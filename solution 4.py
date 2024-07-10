"""Exercise 4: Area of a Field

Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres."""

length = float(input("Enter the length in acres "))
breadth = float(input("Enter the braedth in acres "))
print("The length of field is",length,"acres")
print("The breadth of field is",breadth,"acres")

area = length * breadth
print("The area of the field is", area,"sq. acres")