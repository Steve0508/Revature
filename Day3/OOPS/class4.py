#python subclass

class Animal:
    def __init__(self,name):
        self.name=name
    
    def species(self):
        return "Hello"
    
class Dog(Animal):
    def sound(self):

        return "wolf////"
a=Animal("generic animal")

d=Dog("Buddy")


#Accessing attributres and methods

print (a.name)
print(d.name)
print(d.sound())


print(a.species())