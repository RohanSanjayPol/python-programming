# list compressions 

squares=[]
for i in range(1,11):
    squares.append(i**2)
    
print(squares) 

#another way
squares=[i**2 for i in range(10)]
print(squares)


# create a new list with the values doubled
vec = [-4, -2, 0, 2, 4]
vec2=[i**2 for i in vec]
print(vec2)


# filter the list to exclude negative numbers
vec=[-8, -4, 0, 4, 8]
posVector=[i for i in vec if i>=0]
print(posVector)


# apply a function to add the elements
vec2=[0, 2, 4]
for i in vec2:
    vec.append(i)
print(vec)

# create a list of 2-tuples like (number, square)
list=[(i,i**2)for i in range(10)]
print(list)

vec=[[1,2,3],
     [4,5,6],
     [7,8,9]]

del vec[1][0]  
print(vec)