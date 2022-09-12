# retriving the elements using loops

dictionary={
    "Name":["Rohan","husen","mahesh","bablu"],
    "college":["Nit",'anna dange','mgv','shivaji university'],
    "roll number":[1,2,3,4]
}

for i ,j in dictionary.items():
    print(f"{i}:{j}")

#print only keys and values
for i in dictionary.items():
    print(i)    


#retriving the elements using correspoding index value using enumerator method

for i,j in enumerate(["tic","tac","toa"]):
    print(i,j)

#loop over correspondence element at the same time using zip method

list1=[1,2,3,4,5,6,7,8,9]
list2=[99,88,77,66,55,44,33,22,11]
for i,j in zip(list1,list2): 
    print(i,j)   


#reverse the elements using the reversed method
for i in reversed(range(1,10,2)):
    print(i)


#sort the elements using using sorted method
list=["apple","mango","bannana","guva","chiku"]
for i in sorted(list):
    print(i)
print()


# to remove the duplicates we can use set method 
list=["apple","mango","bannana","guva","chiku","chiku","bannana"]
Set=set(list)
for i in sorted(Set):
    print(i)
print()    

dictionary={
    "Name":["Rohan","husen","mahesh","bablu"],
    "college":["Nit",'anna dange','mgv','shivaji university'],
    "roll number":[1,2,3,4]
}  
print(dictionary.values())  
print(dictionary.keys())

for i in dictionary.values():
    print(i)

for i in dictionary.keys():
    print(i)    

    


 

