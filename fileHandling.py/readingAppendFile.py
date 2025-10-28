with open("/workspaces/gcse-24-27-Muskaan-Yousaf/fileHandling.py/practiceRead.txt", "r") as file:
    content = file.read()
    print(content)
with open("/workspaces/gcse-24-27-Muskaan-Yousaf/fileHandling.py/practiceRead.txt", "a") as file:
    file.write("This is a new line")