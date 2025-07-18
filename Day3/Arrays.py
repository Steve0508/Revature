numbers=[1,2,3,4]
print(numbers)

print(numbers[0])
print(numbers[-1])

numbers[1]=25

print(numbers)


numbers.append(5)
numbers.insert(10,150)

numbers.remove(25)
numbers.pop()  #remove last item


del numbers[0] #remove item at index
del numbers[1:3]   #index 1 and index 2
del numbers  #delete the entire array

for num in numbers:
    print(num)







    import array
    arr=array.array('i',[1,2,3,4])

    print(arr[2])