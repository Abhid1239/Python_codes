
file = open("snake.py", "r")

print(file.read())

print(len(open("a.rtf").readlines()))

for line in file:
    print(line)

str=file.read()


print(len(str))

print("finished")



file.close()
