if __name__ == '__main__':
    test_case = int(input())
    for a in range(test_case):
        n,k,p = map(int,input().split())
        np = list(list(map(int,input().split())) for _ in range(n))
        print(n,k,p,"\n",np)
        val = []
        n = 0
        for x in range((n*k)):
                print(x)
