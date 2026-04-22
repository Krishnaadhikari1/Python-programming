# Build a simple calculator using if-else.

num1=int(input("enter the frist number :"))
num2=int(input("enter the second number :"))
op=input("enter the operation want to do :")

if (op=='+'):
    calculation= num1+num2
    print(calculation)

elif(op=='-'):
    calculation =num1-num2
    print(calculation)

elif(op=='*'):
    calculation =num1*num2
    print(calculation)

elif(op=='/'):
    calculation =num1/num2
    print(calculation)

elif(op=='%'):
    calculation =num1%num2
    print(calculation)

else:
    print("can't do that operation ")