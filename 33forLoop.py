# for loop in python 

names=["rohan","bablu","husen","mahesh"]
for name in names:
    print(name)
print()    

single_name="Rohan"
for name in single_name:
    print(name)    
print()    

for name in names:
    print(name)
    if name=="rohan":
         print(" hello its me")
print()         

# square of each items in the list and put into into the another list 
my_list=[2,3,4,5,6,7,8,9]
empty_list=[]
for i in my_list:
    square=i*i
    empty_list.append(square)    
print(empty_list)