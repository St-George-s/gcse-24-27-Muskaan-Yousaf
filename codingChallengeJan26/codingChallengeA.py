import random 

counter = 0
ranNum = random.randint(1, 50)
userGuess = input(int("Enter a number 1 to 50, try to guess the random number! "))

while userGuess!= ranNum:
userGuess = input(int("Enter a number 1 to 50, try to guess the random number! "))

if userGuess < ranNum:
    print("Your guess is too low.")
    counter = counter + 1 

else:
    print("Your guess is too high.")
    counter = counter + 1

if userGuess == ranNum:
    print("Well done, you got the correct answer!", "you tried", counter, "times!")
#NOT FINISHED VIEW FLOWCHART IN JOTTER FOR DETAILS