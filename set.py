# Set: Unordered, Mutable, No Duplicates

my_set = {1, 2, 3, 4}

# Methods
my_set.add(5)                  # Add element
my_set.update([6, 7])          # Add multiple
my_set.remove(3)               # Remove (Error if not found)
my_set.discard(10)             # Safe remove
my_set.pop()                   # Remove random element
copy_set = my_set.copy()       # Copy set
my_set.clear()                 # Clear set

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference:", set_a.difference(set_b))
print("Symmetric Difference:", set_a.symmetric_difference(set_b))
print("Is Subset:", set_a.issubset(set_b))
print("Is Superset:", set_a.issuperset(set_b))
