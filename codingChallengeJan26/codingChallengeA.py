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
#adding a random so that the number generated is random
counter = 0
ranNum = random.randint(1, 50)
userGuess = 0
 
while userGuess != ranNum:
#this adds a loop so that the user can carry on guessing until they get the right answer
    userGuess = int(input("Enter a number 1 to 50, try to guess the random number!: "))
 
    if userGuess < ranNum:
        print("Your guess is too low.")
        counter = counter + 1
 #if the guess is lower than the generated number this message is printed and they restart, the counter increases by 1 to add to the number of tries
    else:
        print("Your guess is too high.")
        counter = counter + 1
 #if the guess is higher than the generated number this message is printed and they restart, the counter increases by 1 to add to the number of tries
    if userGuess == ranNum:
        print("Well done, you got the correct answer!", "you tried", counter, "times!")
# if the guess is correct the message will print, adding the number of tries it took to get the right answer.
    #FINISHED!