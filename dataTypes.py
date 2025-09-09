#data types
name = "kurt cobain" #this is a string
hisAge = "16" #this is an integer
height = "1.75m" #this is a decimal number (float/real)
hasAGuitar = True #this is a boolean (true/false)

#casting (change from one data type to another)
age = input("enter age: ")
print(age)
print(age + "10") #concatenate 2 strings together (join them)
ageAsAnInt = int(age)
print(ageAsAnInt + 10) #add two integers together (maths addition)
print("Your age is " + str(ageAsAnInt))

# data types - more examples
stillAnInteger = -4
myNumber = "9832462974" #always store as a string

#arithmatic operators
add = 10 + 10
subtract = 10 - 10
multiply = 10 * 10
division = 10 / 10 #will output a float
integerDivision = 11 // 10 #forces output to be an int
print(add, subtract, multiply, division)
print(integerDivision)
moduo = 13 % 10 # remainder of the division
print(moduo)
exponent = 2 ** 3
print(exponent) #to the power of

#activity one - take 2 inputs, multiply them together and output answer
age2 = input("enter an age: ")
ageAsAnInt = float(age2)
time = input("enter a time: ")
timeAsAnInt = float(time)
multiply = timeAsAnInt * ageAsAnInt
print(multiply)

#activity 2 - input user's age, output age times 7
userAge = input("enter your age: ")
userAgeAsAnInt = int(userAge)
multiply2 = (userAgeAsAnInt * 7)
print(multiply2)

#activity 3 - take radius as input, output volume of sphere (v = 4/3 x pi x r^3)
radius = float(input("enter radius: "))
print("Volume of a sphere with radius ", radius, " is ", 4/3 * 3.14169 * radius ** 3)