#input takes input from user. The input is always in the form of string.
#The string can be converted to any other data types using type casting.

noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun:")
adjective1 = input("Enter an adjective: ")


print(f"I went to a {noun1} yesterday.")
print(f"I saw a {noun2} there.")
print(f"{noun2} was really {adjective1}.")
print(f"I couldn't stop thinking about {noun2}")
print(f"I want to see {noun2} again.")


#Calculating the area of a rectangle using user input.

length = float(input("Enter the length of the rectangle:"))
breadth = float(input("Enter the breadth of the rectangle:"))
area = length * breadth
print(f"The area of the rectangle is {area}")   

#note: input() function always takes input as a string. So,
#typecasting must be done to convert the string to float or integer
#inorder to perform mathematical operations.
