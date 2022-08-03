# check the string is palindrome or not using recursion

def palindrome(i,n,str):
    if i>n/2:
        return
    if str[i]!=str[n]:
        return False
    else:
        return True
    
    return palindrome(i+1,n-1,str)


string=input("Enter a string: ")
length=len(string)
s=palindrome(0,length-1,string)
print(s)