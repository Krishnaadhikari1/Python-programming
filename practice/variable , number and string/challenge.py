# Level 3 – Challenge Yourself
#  1. Write a program that takes a user’s name and age as input and prints:
# 2. Given a string "Nepal is beautiful", print:
#      The first 5 characters
#      The last 3 characters
#      The string in reverse order
#  3.Write a program to check if a given number is even or odd.
#  4. Create a program where:
#      You store a sentence in a variable
#      Count how many times the letter "a" appears in it

name=input("enter your name :")
age=int(input("enter your age "))
print(f"my name is {name}")
print(f"i am {age} years old")


text = "Nepal is beautiful"
first_five = text[:5]
print("First 5 characters:", first_five)
last_three = text[-3:]
print("Last 3 characters:", last_three)
reversed_text = text[::-1]
print("Reversed string:", reversed_text)


num= int(input("enter a number :"))
if num%2==0:
    print(" number is even" )
else:
    print("number is odd")
    
    
sentence="my name is krishna adhikari"
count_a=sentence.count("i")
print(count_a)