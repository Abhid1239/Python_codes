file = open("edit.py","w")
file.write("\n#this is not part of code")
file.close()

file = open("edit.py","r")
print(file.read())
file.close

#write program without deleting initaial data

file = open("edit.py","r")
print(file.read)
print("finish")
file.close()

file = open("edit.py", "w")
file.write("anything which is not required")
file.close()

file = open("edit.py","r")
print(file.read)
file.close()
