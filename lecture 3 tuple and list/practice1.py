#wap to cheak if a list contains a palindrome of elements.
list1=[1,2,3,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome ")
else:
    print("not palindrome")
