while True:
    print("TELL ME THE TWO NUMBERS U WANT TO DO ANY OPERATION WITH")
    x = float(input("number 1 = "))
    y = float(input("number 2 = "))
    print("'ADD' or 'SUBT' or 'MUL' or 'DIV' or 'QUIT'")
    U_I=input()
    if U_I =="ADD":
        z=x+y
        
    elif U_I == "SUBT":
        z=x-y
    elif U_I == "MUL":
        z=x*y
    elif U_I == "DIV":
        z=x/y
    elif U_I == "QUIT":
        break
    else:
        break
    print("THE ANS WILL BE",z , "\n \n '''''''''''''by ashish'''''''''''''''''''THE END''''''''''''''''''''''''''''''''\n\n")
