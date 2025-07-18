
def greet():
    print("Hello, welcome")


greet()




def greet(name):
    print("Hello ",name)

    greet("Praveen")


#function return value
def add(a,b):
    return a+b

sum=add(5,8)

print("Sum:",sum)


#default parameter values

def greet(name="Guest"):
    print ("Hello,",name)


greet()
greet("Bob")


    #function with Multiple return values

def get_details():
        name="Alice"
        age=21

        return name,age
n,a=get_details()

print("Name:",n," Age:",a)


def add(*num):
     return sum(num)          #sum is predefined function

print(add(1,2,34,5))



def info(**details):
     for key,value in details.items():
          print(key, ":",value)

info(name="Alice",age=25,city="chennai")