# types of argument in python 

# 1) positional argument 
def greet(name,dept):
    print(f"my name is {name}")
    print(f"my department is {dept}")
greet("rohan","AI and ML") 

#2 keyword argument
def greet(name,dept):
    print(f"my name is {name}")
    print(f"my department is {dept}")
greet(dept="AI and ML",name="rohan") 
print()

def tuples(*numbers):
    for i in numbers:
     add=0
     add= add+i
    print(add)      


tuples(2,3,4,5,6)
