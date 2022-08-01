# check wheather year is leap or not if it is leap year then add day

def leapYear(year):
    if year %4 ==0 or year% 400==0 :
        return 29
    else:
        return 28

year=int(input("Enter a year: "))
lY=leapYear(year)
print(lY)