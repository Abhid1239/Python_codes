name = 0
while not name:
    name = input ('please entreer your name: ')
print('hello,{}!'.format(name))
print('hello,',name,'!')

words = {'this': 1,'is ':2,'not':3,'what ':4, 'i':5,'am going':6}


for this in words:
    print(this,"which no. it corresponds to",words[this])
    print(words['i'])
    
