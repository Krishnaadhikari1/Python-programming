# Level 2 – Slightly Tricky
# 1.Store your first name in one variable and last name in another, then print your full name with a space between them.
# 2.Take a string "Python is Fun" and:
#     .Print it in all uppercase
#     . Print it in all lowercase
#     . Replace "Fun" with "Awesome"
# 3.Store the value 7.5 in a variable and convert it to an integer.
# 4.Swap the values of two variables without using a third variable.
 
first_name = "krishna"
second_name = "adhikari"
print(first_name + " " + second_name)

mystring="python is fun"
print(f"Uppercase:{mystring.upper()}")
print(f"lowercase:{mystring.lower()}")
print(f"Replacement:{mystring.replace('fun','awesome')}")
 
num=7.5
print(int(num))


a=2
b=3
print(f"before swap a={a} b={b}")
a,b=b,a
print(f"after swap a={a} b={b}")