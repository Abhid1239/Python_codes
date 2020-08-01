#tells to print the first string than the second again the first
print("{0}{1}{0}".format("abra","cad"))

#set ups the value by using format so the printed value would be 2,4
a = "{x}, {y}".format(x=2, y=4)
print(a)

#after every word the letter is joined in the string
print(" the ".join(["spam", "eggs", "ham"]))


#replaces or just reomoves the command typed and joints the
#starting of it with the reamining letter
print("hello ME".replace("ME", "World"))

print("this is ham ".replace("ham", "spam eggs"))

#tells whether there the starting letter is same as in the goiven startswith
#by true or false
print("this is satrt".startswith("is"))

print("this is satrt".startswith("this"))

#opposite to startswith


# ? can we use both if as well as print in a single line
b="that"
while True:
    a=input("")
    if a.startswith(b):
        print("you are out of the loop")
        print(a.upper())
        c=input("")
        print(c.split( " this " ))
        
    else:
        print("the starting is not with correct title for hint")
        print(a.lower())  

