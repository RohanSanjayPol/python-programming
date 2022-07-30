# while loop in python

# simple while loop structure in python
count =1
while (count<5):
    print(count)
    count+= 1
print()    

#while loop with else statement
count=1
while(count<5):
    print(count)
    count+=1
else:
    print("out from the loop")   
print() 

#while loop with else statement
count=1
while(count<10):
    if(count==5):
        break
    print(count)
    count+=1
else:
    print("out from the loop")   
print() 

# while loop with if user enter -1 then exit

number=int(input("Enter a number"))
while(True):
    print(number)
    if(number==-1):
        break
    number=int(input("Enter a number press and -1 to exit"))
    
