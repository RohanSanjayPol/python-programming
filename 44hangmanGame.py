# hangman game in python

print("Lets play hangman game! ")
empty_list=["_","_","_","_","_"]
secret_word=["r","o","h","a","n"]
print("you have only six lives so try to guess the word within 6 attempts! good luck!!")
print(empty_list)
guess_letter=input("Guess the letter: ")

if(guess_letter=="r"):
    correct_letter="r"
    empty_list[0]=correct_letter
    print(empty_list)
else:
    print('''0''')    