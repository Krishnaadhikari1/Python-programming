#list slacing 
ages=[20,18,30,13,17,14]
print(ages[1:3])
print(ages[:4])
print(ages[1:])
print(ages[-4:-1])

#list methods
ages.append(24)
print(ages)
ages.sort()#acending order
print(ages)
ages.sort(reverse=True)# decending order 
print(ages)
ages.reverse()
print(ages)
ages.insert(0,12)
print(ages)
ages.remove(12)
print(ages)
ages.pop(0)
print(ages)