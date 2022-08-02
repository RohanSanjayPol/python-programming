# reverse the elements of the array using recursion


def reverseElements(i,n,arr):
    if i>=n/2:
        return 0
    arr[i], arr[n] = arr[n], arr[i]
    reverseElements(i+1,n-1,arr)

def printElements(i,n,arr):
    print(arr[i])
    if(i==n):
        return 
    printElements(i+1,n,arr)    




arr=[11,22,33,44,55,66]
length=len(arr)
reverseElements(0,length-1,arr)
printElements(0,length-1,arr)
