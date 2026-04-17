'''
Write a program that:
    .Takes 2 numbers as input (string)
    .Converts them to integers
    .Performs:
        Addition
        Subtraction
        Multiplication
        Division
    Also print:
        Which number is greater
        Whether both numbers are equal or not 
'''
num1 = int(input("enter the frist number :"))
num2 = int(input("enter the second number :"))

print("addition:",num1+num2)
print("substraction :",num1-num2)
print("division:",num1/num2)
print("multiplication :",num1*num2)

if(num1>num2):
    print("num1 :",num1,"is greater")
else:
    print("num2 :",num2,"is greater")
