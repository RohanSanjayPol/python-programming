# print happy birthday post using recrsion

def happyBirthday(a,b):
    if(a==b):
        print('Happy birhtday')
        return 0
    happyBirthday(a+1,b)
    print(f"{a} day is left for birthday is left")


#calling the function
happyBirthday(1,5)    