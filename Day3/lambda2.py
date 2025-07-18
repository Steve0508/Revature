li=[lambda arg=x: arg *10 for x in range(1,5)]
for i in li:
    print(i())


check=lambda x: "Even" if x%2==0 else "Odd"

print(check(4))
print(check(7))



calc=lambda x,y:(x+y,x*y)

res=calc(3,4)
print (res)


#list  in built one, mixed datatype , slower
#Array    ---- import arrays from module , single type, faster, numeric


n=[1,2,3,4,5,6]

even=filter(lambda x:x %2 ==0,n)   #filter() applies this condition to each element in num
print(list(even))




a=[1,2,3,4]

b=map(lambda x:x*2,a)

#map() iterates  through a and applies the transformations
print(list(b))


from functools import reduce
a=[1,2,3,4]
b=reduce(lambda x,y:x*y,a)

print(b)