lst = [1, 2, 3]
lst.append(4)
lst.remove(2)
print("List:", lst)
print("3 in list?", 3 in lst)


lst1 = [5, 2, 9, 1]
lst1.sort()
print("Ascending:", lst1)
lst1.sort(reverse=True)
print("Descending:", lst1)

#duplicate remove

lst = [1, 2, 2, 3, 4, 4]
unique = list(set(lst))
print("Without duplicates:", unique)


#List Statistics

lst = [5, 2, 9, 1]
print("Min:", min(lst))
print("Max:", max(lst))
print("Average:", sum(lst)/len(lst))
