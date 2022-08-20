def sumOfNaturalNumbers(a,b,sum):
    sum=sum+a
    if a==b:
        return sum
    return sumOfNaturalNumbers(a+1,b,sum)

sum=sumOfNaturalNumbers(0,10,0)
print(sum)    