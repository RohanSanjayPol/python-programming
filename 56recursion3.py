def factorial(a,b,mul):
    mul=mul*a
    if a==b:
        return mul
    return factorial(a+1,b,mul)

mul=factorial(1,5,1)
print(mul)  