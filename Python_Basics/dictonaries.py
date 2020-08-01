ages = {"dave" : [23,32,11],
        "mary" : [14,41,67,87,89],
        "rio" : "error",
        1 : 3}
ages[4] = 16
ages[1] = "no error"
print(ages["mary"])

print( "dave" in ages)

print(ages.get("rio"))
print(ages.get(5))
print(ages.get(5,"not in the dictonary"))

print(ages.get(4,3) + ages.get(5,7))



