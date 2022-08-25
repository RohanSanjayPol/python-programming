# reverse the numbers using recursion
def reverseNumbers(a,b):
    if(a==b):
        print(a)
        return 0
    reverseNumbers(a+1,b)
    print(a)


#call the function
reverseNumbers(1,5)    