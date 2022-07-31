# hangman game in python

print("Lets play hangman game! ")
empty_list=["_","_","_","_","_"]
secret_word=["r","o","h","a","n"]
print("you have only six lives so try to guess the word within 6 attempts! good luck!!")
print(empty_list)

length=len(secret_word)
#for i in range(length):
guess_letter=input("Guess the letter: ")

if(guess_letter==secret_word[i]):
  for i in range(length):
    correct_letter=secret_word[i]
    empty_list[i]=correct_letter
    print(empty_list)
else:
    print("0")    