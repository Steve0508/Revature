# Dictionary: Key-Value pairs, Mutable, No duplicate keys

student = {"name": "Krishna", "age": 21, "marks": 85}

# Methods
student["course"] = "B.Tech"        # Add new key-value
student.update({"grade": "A"})      # Update with another dict
age = student.get("age")            # Get value safely
keys = student.keys()               # All keys
values = student.values()           # All values
items = student.items()             # All key-value pairs
popped = student.pop("marks")       # Remove by key
student.popitem()                   # Remove last inserted
copy_student = student.copy()       # Copy dictionary
student.clear()                     # Clear all

print("Age:", age)
print("Keys:", keys)
print("Values:", values)
print("Popped Marks:", popped)
print("Copied Dict:", copy_student)
