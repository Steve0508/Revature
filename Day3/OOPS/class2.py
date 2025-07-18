




class Dog:
    species="canine"


    def __init__():
        print ("im default")



    def __init__(self,name="hi",age=21):   #_init_ means default constructure in java like
        self.name=name #instance attributes
        self.age=age#innstance attributes



        #creating an object of dog class

dog1=Dog()
dog2=Dog("Praveen",3)


print(dog1.name)    #buddy

print(dog1.species)  #Output :canine

print(dog2.name)  