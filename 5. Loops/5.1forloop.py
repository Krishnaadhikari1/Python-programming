# A for loop in Python is used to repeat a block of code for each item in a sequence (like a list, string, or range).

list= [1,2,3,4,5,6,7,8,9]
name=["krishna","dhiran","chiran","neelam"]
for val in list:
    print(val)
for data in name:
    print(data)

grade=[1,2,3,4,5,6,7,8,9,10]
for i in grade:
    print(i)

#print the number 0 to 7
for i in range(8):
    print(i)

# Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)