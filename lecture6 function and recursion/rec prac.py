#write a recursive function to calculate the sum of frist n nutural numbers.
def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)
print(sum_natural(5))

#write a recursive function to calculate the fibonacci sequence.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))