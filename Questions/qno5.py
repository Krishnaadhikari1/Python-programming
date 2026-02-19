#   Find the largest of three numbers
a=int(input("enter the number  "))
b=int(input("enter the number  "))
c=int(input("enter the number  "))
if a>b and a>c:
    print("the greatest number is ",a)
elif b>a and b>c:
    print("the greatest number is ",b)
else:    
    print("the greatest number is ",c) 
    