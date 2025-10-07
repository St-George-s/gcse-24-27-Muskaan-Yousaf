#Create an array of five integers [1, 2, 3, 4, 5]. Print the array. 
fiveNumbers = [1, 2, 3, 4, 5]
print(fiveNumbers)

#Given the array [10, 20, 30, 40, 50], print the first and last elements of the array. 
qTwo = [10, 20, 30, 40, 50]
print(qTwo[0])
print(qTwo[4])

#Given the array [10, 20, 30, 40, 50], change the element at index 2 to 100. Print the modified array. 
qThree = [10, 20, 30, 40, 50]
qThree[2] = 100
print(qThree)

#Given the array [5, 10, 15, 20, 25], print all elements of the array using a loop. 
qFour = [5, 10, 15, 20, 25]
for counter in range(len(qFour)):
    print(qFour[counter])

#Given the array [2, 4, 6, 8, 10], calculate the sum of all elements. Print the result. 
qFive = [2, 4, 6, 8, 10]
total = 0
for counter in range(len(qFive)):
    total = total + qFive[counter]
print(total)

#Given the array [12, 45, 2, 9, 50, 33], find and print the maximum value in the array. 
qSix = [12, 45, 2, 9, 50, 33]
for counter in range(len(qSix)):
    