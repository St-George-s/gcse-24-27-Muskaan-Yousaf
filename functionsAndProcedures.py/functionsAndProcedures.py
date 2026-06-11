# #procedure
# def printName(name):
#     print(name)

# #Function
# def printNameFunc(name):
#     return name

# #call the procedure
# printName("Muskaan")

# #call the function and print returned value
# print(printNameFunc("Josh Dun"))

# #call the function and store returned value in a variable
# returnedName = printNameFunc("Tyler Joseph")
# print(returnedName)

#questions

# def add_numbers(a, b):
#     total = a + b
#     return total
# result = add_numbers(5, 3)
# print(result)

# def greet(name):
#     print("Hello", name)

# greet("COCA COLA HELLO")

# def sphere_volume(radius):
#     sphere_volume = (4/3 * 3.14 * (radius) ** 3)
#     return sphere_volume

# print(sphere_volume(67))

# volume = sphere_volume(5)
# print(volume)

def linear_search(data_list, target):
    for data_list in data_list:
        if data_list == target:
            return True
    return False

data_list = [3, 8, 2, 10, 7]
print(linear_search(data_list, 10))