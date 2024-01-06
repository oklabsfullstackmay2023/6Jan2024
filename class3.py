#1. Class definaiton is one time process
class PreetMahawar():# always written in class name in PascalCase
    #1 member 
    #2member 
    #3.1 Function defination is one time process
    def myFunction(self):
        print(f'My Favourite Vegetable is Ladyfinger')
        print(f'My Favourite Vegetable is Cabbage')
        print(f'My Favourite Vegetable is Cauliflower')
        pass
#2 create class object is many time process
ceo1=PreetMahawar()    
ceo2=PreetMahawar()    
ceo3=PreetMahawar()  
#3.2 Function calling/invoking is many time process
#ceo.method
ceo1.myFunction()     
ceo2.myFunction()     
ceo3.myFunction()     
        

