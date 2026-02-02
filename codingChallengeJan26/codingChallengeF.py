import random

counter = 0
lettersFound = [ ]
ranFourDig = str(random.randint(1000, 9999))
print(ranFourDig)
userGuess = " "
while ranFourDig != userGuess:
    userGuess = str(input("Input a 4 digit number. "))
    for ch in ranFourDig:
        for chTwo in userGuess:
            if ch == chTwo:
                if not ch in lettersFound:
                    lettersFound.append(ch)
                    counter = counter + 1 
    print("You are", counter, "digits close.")

print("Well done! You found the random four digit number!")
                
