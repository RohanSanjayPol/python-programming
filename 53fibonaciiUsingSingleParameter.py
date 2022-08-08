# fibonacii using single parameter

def fibonacii(n):
    if n<=1:
        return n
    result= fibonacii(n-1)+fibonacii(n-2)
    return result

def printfibonacii(i):
    for i in range(i+1):
        print(fibonacii(i))

#calling the funtion 
printfibonacii(5)
