# Merge two lists and remove duplicates.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
merged = []
for item in list1 + list2:
    if item not in merged:
        merged.append(item)
print(merged)