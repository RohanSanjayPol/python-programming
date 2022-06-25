# list programms 2

my_list=[1,2,3,"rohan","y",0.34]
print(my_list)

#finding the lenght of the my_list
print(len(my_list))
#negative indexing 
print(my_list[-1])
#printing all elements
print(my_list[:])
#printing elements by customized manner
print(my_list[2:4])
#print elements with some steps
print(my_list[: :2])
#sort funtion-if list contain string then it will give an error
numbers=[34,45,75,1,6,3,87,34,56,12]
numbers.sort()
print(numbers)
# max and min value using an function
print(min(numbers))
print(max(numbers))
#append the elements in the list
numbers.append(69)
print(numbers)

#append some names using the list
name=["Rohan","husen"]
n=2
for i in range(n):
    name.append(i)
print(name)

# appending list into list
first=[1,2,3,4]
second=[66,66,66,66,66]
first.append(second)
print(first)

#insert the element at specific position using insert funtion
names=["rohan","mahesh","bablu"]
names.insert(1,"husen")
print(names)

# adds the list to another list using extend funtion
l1=[1,2,3,4,5,6,7,8,9]
l2=[99,99,99,99]
l1.extend(l2)
print(l1)

#change the values from the list
l1[2]=69
print(l1)
l1[1:6]=[22,22,22,22,22,22]
print(l1)

#remove the elements from the list 
l1.remove(9)
print(l1)

#pop the element from the list and it will return which elements you delted
l1.pop(5)
print(l1)

# count funtion prints how many values appeared
names=["rohan","rohan","rohan","husen","mahes"]
print(names.count("rohan"))
print(names)

#clear funtion it delete the all elements from the list
names.clear()
print(names)

#reverse the elements in the list
num=[1,2,3,4,5,6,7,8,9]
num.reverse()
print(num)

#words addtion
word="python"
print(word[0:1]+word[3:])

print('mmmm'+word[:])


