#1. class defination is one time process
class PreetMahawar():# always written in class name in PascalCase
    #1 member
    #2 member
    #3.1 Function callingg/invoking is one time process
    def myFunction(self):
        print(f'My Favourite Car is Alturas G4')
        print(f'My Favourite Car is Scorpio N')
        print(f'My Favourite Car is XUV 700')
        print(f'My Favourite Car is Fortuner Legender')
        pass
#2. create class object is many time process
ceo1=PreetMahawar()
ceo2=PreetMahawar()
ceo3=PreetMahawar()
ceo4=PreetMahawar()
#3.2 Function calling/invoking is many time process
#ceo.method()
ceo1.myFunction()
ceo2.myFunction()
ceo3.myFunction()
ceo4.myFunction()