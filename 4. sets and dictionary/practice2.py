#Create a dictionary to count the frequency of each element in a list.
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Frequency Dictionary:", frequency)
