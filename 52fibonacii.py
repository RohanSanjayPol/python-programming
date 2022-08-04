# fibonacii using recursion
def fibonacii(i,j,n,count):
    if(count==n):
        return 0
    print(j)
    fibonacii(j,i+j,n,count+1)

#calling the function
fibonacii(0,1,7,0)    