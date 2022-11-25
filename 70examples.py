# square the list of the elements
List=[1,2,3,4,5,6,7,8,9,10]
def square(x):
    return x*x
squared=map(square,List)
print(list(squared))

#map with built in function
numbers=[1.5,1.7,8.9,3.4]
convertIntoNumbers=map(int,numbers)
print(list(convertIntoNumbers))

# map using lambda function
numbers=[1,2,3,4,5]
cube=map(lambda x:x**3,numbers)
print(list(cube))

#map using multiple iteratables
num1=[1,6,4]
num2=[8,3,75]
additionOfTwoList=map(lambda x,y:x+y,num1,num2)
print(list(additionOfTwoList))

#converting strings to intergers
string=['1','5','10']
integer=map(int,string)
print(list(integer))

#combining map and filter function
#square only even numbers
number=[1,2,3,4,5,6,7,8,9,10]
squaredEvenNum=map(lambda x:x**2,filter(lambda x:x%2==0, number))
print(list(squaredEvenNum))

#convert the into uppercase
names=['rohan','bablu','husen','mahesh']
upperCase=map(str.upper,names)
print(list(upperCase))

#format the decimal with two places
num=[12.3344,34.678,23.7,78.33]
flotingnum=map(lambda x:f"{x:.2f}",num)
print(list(flotingnum))
