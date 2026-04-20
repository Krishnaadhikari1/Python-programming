"""string """
str1="krishna "
str2='adhikari'
str3="""dhiran"""
print(str1)
len1=len(str1)
print(len1)
finalstr=str1+str2
print(finalstr)

"""indexing """
str="madan bhandari"
print(str[3])

"""slicing """
#accessing parts of a string 
print(str[7:10])
print(str[6:len(str)])
print(str[-5:-1])
#string function
print(str.endswith("er"))
print(str.capitalize())
print(str.replace("i","e"))
print(str.find("d"))