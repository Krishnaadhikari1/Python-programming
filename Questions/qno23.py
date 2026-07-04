# Sort a list without using sort().
numbers = [5, 2, 9, 1, 7]
n = len(numbers)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
print(numbers)