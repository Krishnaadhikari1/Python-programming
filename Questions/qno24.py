# Find second largest element.
numbers = [10, 5, 20, 8, 15]
largest = second_largest = float('-inf')
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
if second_largest == float('-inf'):
    print("No second largest element.")
else:
    print("Second largest element:", second_largest)