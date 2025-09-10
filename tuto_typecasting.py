#Typecasting basically means converting one data type into another data type.
a = "5" #string
b = int(a) #integer as we changed the data type of a from string to interger using int()
#similarly we can use float() and str() to convert to float and string respectively.

#same can be done for boolean
c = bool(b) #boolean as we changed the data type of b from integer to boolean  
print(a)
print(b)
print(c)
#output will be 5, 5, True as a is string "5", b is integer 5 and c is boolean True as any non zero number is considered True in boolean.
#Note: we cannot convert string to integer or float if the string does not represent a number. For example:
d = "Hello" #string
#e = int(d) #this will give an error as "Hello" cannot be converted to integer.
#f = float(d) #this will also give an error as "Hello" cannot be converted to float.
#However, we can convert string to boolean. Any non empty string is considered True in boolean.
g = bool(d) #boolean as we changed the data type of d from string to boolean.       
print(g) #output will be True as d is a non empty string.
#An empty string will be considered False in boolean.   
#for example:
h = ""
print(bool(h)) #output will be False as h is an empty string.

