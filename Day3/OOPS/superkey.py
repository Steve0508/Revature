#super()


class Parent():

    def show(self):
        print("inside Parent")
    
class Child(Parent):
    def show(self):



        super().show()
        print("Inside Child")

obj=Child()
obj.show()


obj1=Parent()
obj1.show()