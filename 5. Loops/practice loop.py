#print the element of the following list using a loop:
list=[1,4,9,16,25,36,49,64,81,100]
for data in list:
    print(data)
    
#search for a number x in the tuple using the loop :
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
idx = 0
for el in tup:
    if el == x:
        print("number is found at idx", idx)
        break
    idx += 1