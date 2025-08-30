
""" 
Given two sets:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
Find:
(a) Union
(b) Intersection
(c) Difference (A - B)
(d) Symmetric Difference
"""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# (a) Union
union_set = A | B
print("Union:", union_set)

# (b) Intersection
intersection_set = A & B
print("Intersection:", intersection_set)

# (c) Difference (A - B)
difference_set = A - B
print("Difference (A - B):", difference_set)

# (d) Symmetric Difference
symmetric_difference = A ^ B
print("Symmetric Difference:", symmetric_difference)
