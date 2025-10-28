#Write a Python program to read and print the contents of a text file. 
with open("/workspaces/gcse-24-27-Muskaan-Yousaf/fileHandling.py/practiceRead.txt", "r") as file:
    content = file.read()
    print(content)
