# # Write a Python program to extract the first and last characters of a string entered by the user. 
# string = input("gimme a string: ")
# print(string[0])
# print(string[-1])

# Write a Python program to reverse a string entered by the user. 
# userString = input("give me another string: ")
# reverseString = ""
# for character in userString:
#     reverseString = character + reverseString
# print(reverseString)

# Write a Python program to check if a string is a palindrome (reads the same forward and backward). 


# Write a Python program to count the number of vowels in a string. 

# Write a Python program to replace all spaces in a string with underscores (_). 

 

# Generate and print one random integer from 1 to 6. 
# import random
# myRandomNumber = random.randint(1, 6)
# print(myRandomNumber)

# Roll two dice (1–6) and print both values and their total using + string concatenation. 
# import random
# myRandomNumber = random.randint(1, 6)
# myRandom2 = random.randint(1, 6)
# print(str(myRandomNumber), " + ", str(myRandom2), " = ")
# print(str(myRandomNumber + myRandom2))


# Given the list below, use a random integer to select a valid index and print the item at that index. 
#animals = ["otter", "red squirrel", "pine marten", "seal", "oystercatcher"] 
 
#Write program code that will generate a random number between 1 and 3
# import random

# myRandomNumber = random.randint(1, 3)
# print(myRandomNumber)

#Create an algorithm that will generate a random number between 1 and 3 and
#  then use this to display a message to either walk 10km, run 5km or swim 1km.
# import random

# myRandomNumber = random.randint(1, 3)
# print(myRandomNumber)

# if myRandomNumber == 1:
#     print("You will walk 10 kilometers.")
# elif myRandomNumber == 2:
#     print("You will run 5 kilometers.")
# elif myRandomNumber == 3:
#     print("You will swim 1 kilometer.")

# Create an algorithm that will allow the user to enter a word and then count
#  how many times the letter A appears in that word. Both upper case (“A”) and 
# lower case (“a”) letters must be counted. The algorithm should repeat until a
#  word is entered that has 3 or more letter As.
# numberOfLetterA = 0

# while numberOfLetterA < 3:
#     word = input("Enter a word: ")
#     numberOfLetterA = 0
#     for letter in word:
#         if letter == "a" or letter == "A":
#              numberOfLetterA = numberOfLetterA + 1
# print("The amount of times the letter A comes up in this word is " , numberOfLetterA)