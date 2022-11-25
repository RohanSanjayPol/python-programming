# map function in python

# 1) map function with single iteratable
def square(data):
    return data*data
numbers=[2,3,4,5,6]
squared=map(square,numbers)
print(list(squared))

# 2) converting strings to integers
numbers=['1','2','3']
conversion=map(int,numbers)
print(list(conversion))

# filter function
List=[1,2,3,4,5,6,7,8,9,10,11,12,13]
def evenNumbers(x):
    return x%2==0
onlyEvenNumber=filter(evenNumbers,List)
print(list(onlyEvenNumber))

#using lambda function
List2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
evenNum=list(filter(lambda x:x%2==0 and x>5 ,List2))
print(evenNum)

#sort the elements on the basis of characters
city=['Mharashtra','sikkim','assam','goa','west bengal','bihar','up']
def length(city):
    return len(city)
Sort=sorted(city,key=length)
print(list(Sort))

#sort same by using lambda function
Sort=sorted(city, key= lambda city:len(city))
print(Sort)