# Tuple: Ordered, Immutable, Allows Duplicates

my_tuple = (10, 20, 30, 20, 40)

# Methods
count_20 = my_tuple.count(20)       # Count of value
index_30 = my_tuple.index(30)       # First index of value

print("Tuple:", my_tuple)
print("Count of 20:", count_20)
print("Index of 30:", index_30)

# Access
print("First Element:", my_tuple[0])
print("Slice [1:4]:", my_tuple[1:4])

# Nested Tuple
nested = (1, (2, 3), [4, 5])
print("Nested Tuple:", nested)
