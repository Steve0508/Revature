a="Praveen"
b=21
msg="My n ame is {0} , my age is  {1}.".format(a,b)
print(msg)





a="python" 
print("the code is {}".format(a))

print("my nmae is {} and my age is {}.".format("Praveen",21))

#fstring

name ='Om' 
age=21

print(f"Hello , my name is {name} and im {age} yeras old")



def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))