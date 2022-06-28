# random package in python
import random as rd
#randint-it will generate random numbers from 0 to 5
randomNumbers=rd.randint(0,5)
print(randomNumbers)

#randrange- randrange is also same but it is it does not contain the last element 
random=rd.randrange(0,5)#it will not generate 5 as random numbers
print(random)

#random - it will generate random floating numbers and range is 0.0 to 1
num=rd.random()
print(num)

#for loop
n=10
for i in range(n):
    num=rd.random()
    print(num)

list=[] 
for i in range(n):
    x=rd.randint(10,1000)
    list.append(x)

print(list) 

#uniform it will give floating point numbers within a range
z=rd.uniform(1,9)
print(z)

#choice select a random from within a our created choice 
ch=[11,22,33,44,55,66,77,88,99]
m=rd.choice(ch)
print(m)

#shuffle the list - it will shuffle the list means change the elements each position
rd.shuffle(ch)
print(ch)


