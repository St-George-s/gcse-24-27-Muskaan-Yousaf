totalHeight = 0
height = 0
numberOfPeople = int(input("How many people?"))
for i in range(numberOfPeople):
    height = int(input("How tall are you? "))
    totalHeight = totalHeight + height
print("The average of these people is " + str(totalHeight / numberOfPeople))