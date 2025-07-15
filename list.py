# List: Ordered, Mutable, Allows Duplicates

my_list = [10, 20, 30, 40]

# Methods
my_list.append(50)              # Add at end
my_list.insert(2, 25)           # Insert at index
my_list.extend([60, 70])        # Add multiple items
my_list.remove(20)              # Remove by value
popped = my_list.pop()          # Remove last
index_30 = my_list.index(30)    # Find index
count_10 = my_list.count(10)    # Count occurrences
my_list.reverse()               # Reverse the list
my_list.sort()                  # Sort ascending
copy_list = my_list.copy()      # Copy list
my_list.clear()                 # Clear all elements

print("Original List after clear:", my_list)
print("Copied List:", copy_list)
print("Popped Element:", popped)
print("Index of 30:", index_30)
print("Count of 10:", count_10)
