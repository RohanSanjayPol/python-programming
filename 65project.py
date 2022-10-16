# project guess the number
import random as rd
print("Guess the number between 10 to 50")
print('''
      1. simple
      2. medium 
      3. hard
      ''')
level=int(input('select the level: ') )

randomNumber=rd.randint(1,50)

match level:
    case 1:
        for i in range(10,0,-1):
            print(f'you have {i} attempts remaining to the guess number!')
            guessNumber=int(input("Make a guess: "))
            if(guessNumber>randomNumber):
                print('your guess is too high')
                print('guess again')
            elif(guessNumber<randomNumber):
                print('your guess is too low')
                print('guess again')
            elif(guessNumber==randomNumber):
                print('your guess is the correct')
                break
            else:
                print('your are out of guesses, you losses') 
                break  
    case 2:
        for i in reversed.range(6):
            print(f'you have {i} attempts remaining to the guess number!')
            guessNumber=int(input("Make a guess: "))
            if(guessNumber>randomNumber):
                print('your guess is too high')
                print('guess again')
            elif(guessNumber<randomNumber):
                print('your guess is too low')
                print('guess again')
            elif(guessNumber==randomNumber):
                print('your guess is the correct')
                break
            else:
                print('your are out of guesses, you losses') 
                break           
    case 3:
        for i in reversed.range(3):
            print(f'you have {i} attempts remaining to the guess number!')
            guessNumber=int(input("Make a guess: "))
            if(guessNumber>randomNumber):
                print('your guess is too high')
                print('guess again')
            elif(guessNumber<randomNumber):
                print('your guess is too low')
                print('guess again')
            elif(guessNumber==randomNumber):
                print('your guess is the correct')
                break
            else:
                print('your are out of guesses, you losses') 
                break           


                 


