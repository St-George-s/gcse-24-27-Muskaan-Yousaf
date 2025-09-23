# Write a Python program to keep 
# asking for a code until it equals "rzy" and print "Code accepted" once the user enters "rzy". 

# correctCode = "rzy"
# userEntry = input("enter your password: ")
# while userEntry == "rzy":
#     print("correct code!")

# while userEntry != correctCode:
#     print("incorrect password")
#     userEntry = input("enter your password: ")

# question 12
#Write a Python program to keep asking for a code until it equals
#  4003 and print "Code accepted" when the code is correct. THIS WAY IS THE CORRECT WAY COMPARED TO ABOVE

# correctCode = "4003"
# userEntry = input("enter your code: ")
# while userEntry != correctCode:
#     print("incorrect code")
#     userEntry = input("reenter your code: ")
# print("code accepted!")

# question 13
# Write a Python program to keep asking for the user's age until
# it is over 14 and print "Age accepted" once the user enters an age over 14. 

# userAge = input("what is your age: ")
# while int(userAge) <= 14:
#      userAge = input ("too young, what is your age: ")
# print("you are over 14")

#question 14
#Write a Python program to keep asking the user to input a password until it is longer than 5 characters
#and print "Password accepted" once the password is longer than 5 characters. 

# password = input("what is your password?: ")
# passwordLen = len(password) 
# while len(password) < 5:
#      password = input("AGAIN, what is your password?: ")
# print("password accepted.")

#15: Write a Python program to ask the user if they would like to watch another episode of Modern Family. If they enter the 
# word "yes," then print "playing another episode" and repeat. Otherwise, print "See you later!" and stop.

# answer = input("Would you like to watch another episode of Modern Family?")
# while answer == "yes":
#     print("Playing another episode")
#     answer = input("Would you like to watch another episode of Modern Family?")
# print("See you later!!!")

#16: Write a Python program to keep asking for money until the total amount of money is greater than 100. Print 
# "I accept your offer" once the total money is greater than 100. 

moneyRequest = (float(input("How much money are you offering?")))
while moneyRequest > 100:
    moneyRequest = (float(input("How much money are you offering?")))
print("Accepted your offer.")
#UNFINISHED