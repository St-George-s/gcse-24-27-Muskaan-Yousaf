# import random 

# counter = 0
# ranNum = random.randint(1, 50)
# userGuess = 0

# while userGuess != ranNum:
#     userGuess = int(input("Enter a number 1 to 50, try to guess the random number!: "))

#     if userGuess < ranNum:
#         print("Your guess is too low.")
#     counter = counter + 1 

# else:
#     print("Your guess is too high.")
#     counter = counter + 1

#     if userGuess == ranNum:
#         print("Well done, you got the correct answer!", "you tried", counter, "times!")
# #NOT FINISHED VIEW FLOWCHART IN JOTTER FOR DETAILS

import random
 
counter = 0
ranNum = random.randint(1, 50)
userGuess = 0
 
while userGuess != ranNum:
 
    userGuess = int(input("Enter a number 1 to 50, try to guess the random number!: "))
 
    if userGuess < ranNum:
        print("Your guess is too low.")
        counter = counter + 1
 
    else:
        print("Your guess is too high.")
        counter = counter + 1
 
    if userGuess == ranNum:
        print("Well done, you got the correct answer!", "you tried", counter, "times!")

    #FINISHED!