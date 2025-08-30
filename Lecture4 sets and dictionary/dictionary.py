'''
dictionary are used to store data values in key:value pairs
they are ordered , mutable and don't allow duplicate keys
'''
std={
    "name":'krishna',
    "age":20,
    "address":"Baneshwor"}
print(std)
print(type(std))
print(std["name"])
std["name"]="Dhiran "
std["class"]=10
print(std)