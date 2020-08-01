for num_of_times in range(int(input())):
    word = str(input())
    size = len(word)
    if size > 10 :
        print(str(word[0]) + str(size-2) + str(word[size-1]))
    else :
        print(word)
