# using list as stack

def insertElement(stack):
    elem=int(input("Enter the Element:"))
    stack.append(elem)

def deleteElement(stack):
    if not stack:
        print("stack underflow")
    else:    
        stack.pop()   

def printElements(stack):
    for i in stack:
        print(i)    

#creating an stack
stack=[] 

while True:
 choice=int(input('''Enter your choice
         1) insert the element
         2) delete the element
         3) print the element
         4)exit
         '''))
 if choice==1:
    insertElement(stack) 
 elif choice==2:
    deleteElement(stack) 
 elif choice==3:
    printElements(stack)   
 elif choice==4:
    break
 else:
    print("invlid choice")    


   
