#print the multiplication table of a number n.
i=1
while(i<=10):
    print(3*i)
    i+=1
#print the elements of the following list using a loop:[1,,4,9,16,25,36,49,64,81,100]
Num= [1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(Num):
    print(Num[idx])
    idx+=1
    
x=36
i=0
while(i<len(Num)):
    if(Num[i]==x):
        print("found at idx ",i)
    else:
        print("finding ....")
    i+=1   
