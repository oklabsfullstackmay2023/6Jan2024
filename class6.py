#1. class defination is one time process
class FamilyMember():#alaways class name written in PascalCase
    #1 member
    #2 member
    #3.1 function defination is one time process
    def myFunction(self):
        print(f'Hello Mr. Kailash Chandra Mahawar')
        print(f'Hello Mr. Dinesh Chandra Mahawar')
        print(f'Hello Mrs.  Anita Mahawar')
        print(f'Hello Mrs. Pooja Mahawar')
        print(f'Hello Mrs. Tanishka Mahawar')
        print(f'Hello Mas. Vishal Mahawar')
        print(f'Hello Mas. Preet Mahawar')
        pass

#2. create class object is many time process
ceo1=FamilyMember()
ceo2=FamilyMember()
ceo3=FamilyMember()
ceo4=FamilyMember()
ceo5=FamilyMember()
ceo6=FamilyMember()
ceo7=FamilyMember()

#3.2 Function calling/invoking is many time process
ceo1.myFunction()
ceo2.myFunction()
ceo3.myFunction()
ceo4.myFunction()
ceo5.myFunction()
ceo6.myFunction()
ceo7.myFunction()
    
          