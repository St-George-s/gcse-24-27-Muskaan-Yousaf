#Create an array called cityNames to store the names of five cities in the UK.
cityNames = ["London", "Edinburgh", "Cardiff", "Belfast", "Glasgow" ]
population = [8908, 482, 366, 341, 635]

for counter in range(len(cityNames)):
    print(cityNames[counter] + " has a population of " + str(population[counter]))
#Using a Loop to Print Data and population

#linear search
found = False
userCity = input("What city would you like the population for: ")
for counter in range(len(cityNames)):
    if userCity == cityNames[counter]:
        print(cityNames[counter] + " has a population of " + str(population[counter]))
        found = True

if not found:
    print("Your city was not found.")

