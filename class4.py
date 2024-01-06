#1. class defination is one time process
class VishalMahawar(): # always written in class name in PascalCase
    #1  member
    #2  member
    #3.1 Function defination is one time process
    def myFunction(self):
        print(f'My Favourite Colour is Blue') 
        print(f'My Favourite Colour is Orange') 
        print(f'My Favourite Colour is Black') 
        print(f'My Favourite Colour is White') 
        pass
#2. create class object
ceo1=VishalMahawar()        
ceo2=VishalMahawar()        
ceo3=VishalMahawar()        
ceo4=VishalMahawar()        

#3.2 Function calling/invoking is many time process
#ceo.method()
ceo1.myFunction()
ceo2.myFunction()
ceo3.myFunction()
ceo4.myFunction()