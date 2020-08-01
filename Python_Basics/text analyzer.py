print("WELCOME TO TEXT ANALYZER")


filename = input("Enter a Filename:")
with open(filename) as f:
    text = f.read()
print(text)



def cnt_ch(text, char):
    count=0
    for m in text:
        if m == char:
            count +=1
    return count

def per_ch(text, char):
    percy = 100 * cnt_ch(text, char) / len(text)
    return percy
        
while True:
    n = int(input("press 1 to get number of words in any word: \n2 for their percentage: \n3 for all the words and their percentage:"))

    if n == 1:
        word =input("\ntype the character u want to know how many times its repeated: ")
        print("\nthis may tmes", word,"is repeated",cnt_ch(text, word), "\n")
    elif n == 2:
        word =input("\ntype the character u want to know how much percent of times it is repeated: ")
        print("\nthe percentage of character", word,"is", per_ch(text, word), "\n")
    else:        
        for char in "abcdefghijklmnopqrstuvwxyz":
            print("the char ",char,"is repeated ",cnt_ch(text, char),"times")
            print("percentage of it is {0}%".format(round(per_ch(text, char), 2)),"\n")
     
