#RECURSION :when a function calls itself repeately.
def display(n):
    if(n==0):
        return
    print(n)
    display(n-1)
display(10)

