class Public:
    def __init__(self):
        self.name="Praveen"  #public attribute

    def display_name(self):
        print(self.name) #public method

obj=Public()
obj.display_name()   #Accessible
print(obj.name)  #Accessible






#################

class Protected:
    def __init__(self):
        self._age =30    #protected attributre

class Subcalss(Protected):
    def display_age(self):
        print(self._age) #Accessible in subclass



obj =Subcalss()
obj.display_age()


#######################


class Private:
    def __init__(self):
        self.__salary=50000   #Private attribute double underscore
    
    def salary(self):
        return self.__salary  # Access through public method
    
obj =Private()
print(obj.salary())  #Works
