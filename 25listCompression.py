# list compression
# create the list of the squares
squares=[x**2 for x in range(1,11)]
print(squares)
for i in squares:
    print(i)
print()

#filter even numbers
evenNumbers=[x for x in range(10) if x%2==0]
print(evenNumbers)

# apply a function
applyFunction=[char.upper() for char in 'rohan']
print(applyFunction)

#nested loops in list comprensions
pairs=[(x,y) for x in range(5) for y in range(5)]
print(pairs)

#using if else expression
ifElseExpression=['not allowed' if age<20 else 'allowed' for age in range(10,30)]
print(ifElseExpression)

evenOdd=['even' if num%2==0 else 'odd' for num in range(20) ]
print(evenOdd)

# generate multiplication table
table=[5*x for x in range(1,11) ]
print(table)

#extract vowels from words
name="Rohan Pol"
vowels=[char for char in name if char in 'aeiou' ]
print(vowels)

# combine the two list
names=["Rohan","bablu",'mahesh','husen']
rollNos=[6,10,12,42]
combinations=[(name,rollno)for name in names for rollno in rollNos ]
print(combinations)

#extract the digit from string
string='abc123xyz456'
digit=[char for char in string if char.isdigit()]
print(digit)

#square numbers in list skip negative
numbers = [-5, -2, 0, 3,5 ]
squareList=[i*i for i in numbers if i>=0]
print(squareList)

#create a list of the numbers
list=[i for i in range(10)]
print(list)

#create a list of the string
listOfString=[char for char in 'Rohan']
print(listOfString)

#double the each number of the string
doubleTheNumber=[num *2 for num in range(15,20)]
print(doubleTheNumber)

#filter the odd numbers
filterOddNumbers=[num for num in range(1,11) if num% 2!=0]
print(filterOddNumbers)

#convert the of the string into uppercase
string="rohan"
strIntoUppercase=[str.upper() for str in string]
print(strIntoUppercase)

#generate the square roots
import math as m
squareRoots=[m.sqrt(sqr) for sqr in range(26)]
print(squareRoots)

#extract the constants from the string
name="Rohan Sanjay Pol"
ExtractConstansts=[str for str in name if str not in 'aeiou']
print(ExtractConstansts)

#flatten a nested list
list=[[1,2,3],[4,5],[69]]
flattenList=[j for i in list for j in i]
print(flattenList)

#create a multiplication table

#input=int(input("Enter a number"))
mulTable=[num*5 for num in range(1,11)]
print(mulTable)

#filter and combine multiple conditons
filter=[num for num in range(50) if num % 3==0 and num % 5 == 0]
print(filter)

#create the tuples with conditonal logic
tuples=[(num,num+1) for num in range(20) if num>10]
print(tuples)