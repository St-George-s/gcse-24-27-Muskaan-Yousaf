#  #this is an example of a fixed loop. print name 10 times
# # for counter in range(10):    
# #     print("something")

# # #ask python to ask for your name then print 100 times
# # name = input("Enter a name:")
# # for counter in range(100):
# #     print(name)

# # #ask python to ask for your name then say hello 1000 times.
# # name2 = input("Enter your name: ")
# # for counter in range(1000):
# #     print (name2 + " Hello")

# #print the answers to the 8 times table from 1 to 12

# # for counter in range(1, 13):
# #     print(counter * 8)

# # #get the program to calc the 7 times table up to 12, and then print '7 x number = answer'
# # for counter in range(1, 13):
# #     print("7 * " + str(counter) + " = " + str(7 * counter))

# # #get python to ask the user the input of 10 people and print each age
# # for counter in range(1, 11):
# #     age = int(input("Enter an age: (" + str(counter) + "): "))
# #     print(str(age * 10))

# #write the program to ask the user to input the age of 10 people
# #add up all the ages
# # #print the total ages
# # total = 0
# # for counter in range(1, 11):
# #     age = float(input("enter an age: "))
# #     total = total + age
# #     print(total)

# #Write a Python program to output the 
# # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, and 12 times tables from 1 to 12.
# for counter1 in range(1,13):
#     for counter2 in range(1,13):
#         print(counter1, "X", counter2, "=", counter1 * counter2)

# Extension Activity 
# Write a Python program that: 
# Asks the user which times table they would like to see (e.g. 4, 7, 12). 
# Asks the user how far the table should go (e.g. up to 20). 
# Prints the chosen times table up to the number given. 
# Then asks the user if they would like to see another times table and repeats until they type no. 

# timestables = int(input("which timestable do you wanna see?: "))
# howFar = int(input("how far would you like to go?: "))

# for counter in range(1, howFar + 1):
#     print(counter * timestables)