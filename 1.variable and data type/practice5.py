"""
Write a program that:
    .Takes name, age, and salary
    .Converts age → int, salary → float
    .Prints:
        .Name
        .Age after 5 years
        .Salary after 10% increase 
"""
name = input("enter your name :")
age = int(input("enter your age :"))
salary = float(input("enter your salary :"))

print("Name :",name)
print("age after 5 years:",age+5)
print("salary after 10% increase :",salary+salary*0.1)