# calulate average height from the given list dont  use sum and avg function
sum=0
count=0
height=input("Enter all height seperated by space: ")
height_list=height.split()
for i in height_list:
    count= count+1
print(count)  
for i in range(0,count):
    height_list[i]=int(height_list[i])
for i in height_list:
    sum=sum+i
avg=sum/count
print(avg)    

  
    
