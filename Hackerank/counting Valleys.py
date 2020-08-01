'''def countingValleys(n, s):
    count=0
    add=1
    print('_',s[0],end='')
    for  val in s:
        if val=='U':
            if(s[count-1]==s[count]):
                
                print(s[count-1],'b   b',s[count],end='')
                addspace(add)
                print('/')   
            else:
                print('new joaz',end='')
                print('/',end='')
        elif val =='D':
            if(s[count-1]==s[count]):
                addspace(add)
                print('\\')
            else:
                print('\\',end='')
        count=count+1
        add=add+1'''

def addspace(add):
    print()
    for x in range(0,add):
        print(' ',end='')

n = int(input())

s = input()



def countingValleys(n, s):
    count=1
    add=3
    if(s[0]=='U'):
      print('_/',end='')
    elif(s[0]=='D'):
       print('_\\',end='')
    while(count<n):
        if s[count]=='U':
            if(s[count-1]==s[count]):
                 addspace(add)
                 add=add+1
                 print('/',end='')
            else:
                print('/',end='')
        elif s[count]=='D':
            if(s[count-1]==s[count]):
                 addspace(add)
                 add=add+1
                 print('\\',end='')
            else:
                print('\\',end='')
        count=count+1
    print('_')
                 
                 

result = countingValleys(n, s)             
                
            
    
