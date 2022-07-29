# password generator in python
import random as rd
import string
print("Welcome to password generator!")
special_symcols=["!","@","#","$","%","^","&","*","(",")"]

letters=int(input("how many letters would you like in your passwords "))
symbols=int(input("how many symbols would you like "))
numbers=int(input("how many numbers would you like "))

password=[]

for i in range(numbers):
    password.append(str(rd.randint(0,9)))

for i in range(symbols):
    password.append(str(rd.choice(special_symcols)))    

for i in range(letters):
    password.append(str(rd.choice(string.ascii_uppercase)))
    password.append(str(rd.choice(string.ascii_lowercase)
))

rd.shuffle(password) 

final_password = ''.join(password)
print("Generated Password:", final_password)   



