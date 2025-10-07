#create arrays
height = [3.4, 5.4, 8.6,]
names = ["Muskaan", "Kurt Cobain", "Conan Gray"]
print(names[1]) #prints Kurt
print(names[0]) #prints Muskaan
print(names[2]) #prints Coneeeeee

for counter in range(len(names)):
        print(names[counter]) # Counter is 0 then 1 then 2
        print(height[counter])

#Append (add)
height.append(2.2)
names.append("Jimmy")

print(height)
print(names)