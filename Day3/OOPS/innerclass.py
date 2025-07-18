class Color:
    def __init(self):
        self.name='Green'
        self.lg=self.Lightgreen()
        
    def show(self):
        print('Name:',self.name)
    
    class Lightgreen:
        def __init(self):
            self.name='light green'
            self.code ='024avc'
        
        def display(self):
            print('Name:',self.name)
            print('code :',self.code)

outer =Color() #outer class object creation

outer.show()  #outer class  method invocation


g=outer.lg    #inner class object creation
g.display()    #inner class method calling