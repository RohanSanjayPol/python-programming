# list revision

#1) append method
list=[11,22,33,44,55]
emptyList=[]
 
for i in list:
    emptyList.append(i)
print(emptyList)   

#insert the element the at specified position
list.insert(4,69)
print(list)

#remove the whatever element you want to delete
list.remove(69)
print(list)

#pop- deletes the last element
list.pop()
print(list)

#index -returns the index number of specified x element
print(list.index(33))

#sort - sort the items
l1=[12,53,64,67,45,334]
l1.sort()
print(l1)

# reverse the elements
list.reverse()
print(list)

#count the elements in the list 
print(list.count(44))

l3=list.copy()
print(l3)

