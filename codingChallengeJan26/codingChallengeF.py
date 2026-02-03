import random #this adds a random

counter = 0
lettersFound = [ ]
ranFourDig = str(random.randint(1000, 9999)) #generates the random four digit number
userGuess = " " #empty string so that the variable exists outside the loop
while ranFourDig != userGuess: #this loop will keep looping UNLESS the user inputs the correct answer
    userGuess = str(input("Input a 4 digit number. ")) #the user guessing the number via input
    for ch in ranFourDig:
        for chTwo in userGuess:
            if ch == chTwo: #if one number in userGuess matches one in ranFourDig
                if not ch in lettersFound: 
                    lettersFound.append(ch)
                    counter = counter + 1 #add one to the counter to tell user how close they are
    print("You are", counter, "digits close.")

print("Well done! You found the random four digit number!") 
                
