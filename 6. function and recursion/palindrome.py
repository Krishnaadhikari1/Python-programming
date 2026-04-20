#write a program to cheak the palindrome or not
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

text = input("Enter a string: ").lower().replace(" ", "")

if is_palindrome(text):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
