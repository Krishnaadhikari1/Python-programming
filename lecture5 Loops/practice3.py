# WAP to find the factorial of first n numbers using for loop
n = int(input("Enter a positive integer: "))

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    print(f"Factorial of {i} is {fact}")
