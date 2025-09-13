#we can round off to a certain number of decimal places using
#the built in round() function.

num = 4.2349348434300004848
print(round(num,5))
print(round(num,2))
print(round(num,0)) #rounding off to 0 decimal places will give an integer value.
print(round(num)) #if the second argument is not provided, it will round off to the nearest integer.
#note: the second argument of round() function is optional.
#note: round() function returns a float value even if the second argument is 0 or not provided.
#to convert it to integer, we can use int() function.  
#  
print(type(round(num,0)))
print(type(int(round(num,0))))

#this shows when float is rounded to the nearest integer, then
#also the value is still float not integer.
