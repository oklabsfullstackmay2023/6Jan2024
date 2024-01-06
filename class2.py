#1. Class defination is one time process
class MyClass(): # always class name written in PascalCase
    #1 member
    #2 member
    #3.1 Function defination is one time process
    def myFunction(self):#self is cio
        print(f'My Favourite Fruit is Mango')
        print(f'My Favourite Fruit is Apple')
        print(f'My Favourite Fruit is Papaya')
        print(f'My Favourite Fruit is Muskmelon')
        pass

#2. create class object is many time process
ceo1=MyClass()
ceo2=MyClass()
ceo3=MyClass()
ceo4=MyClass()
#3.2 Function calling/invoking is many time process
#ceo.method
ceo1.myFunction()
ceo2.myFunction()
ceo3.myFunction()
ceo4.myFunction()
