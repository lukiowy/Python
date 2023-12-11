#file = open("C:\Python\Day 24\Files\my_file.txt")
#contents = file.read()
#print(contents)
#file.close()

with open("C:\Python\Day 24\Files\my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("C:\Python\Day 24\Files\my_file.txt", "w") as file:
    file.write("asd")


with open("C:\Python\Day 24\Files\my_file.txt", "a") as file:
    file.write("asd")