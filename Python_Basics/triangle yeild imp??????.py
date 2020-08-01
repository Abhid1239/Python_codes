def countd(i):
  while i > 10:
    yield i
    i -= 1
for i in countd(11):
  print(list(countd(i)))


#triangle value is created

def inf():
  while True:
    yield 0
    
 

#for m in inf():
 # print(n)

def is_primes(num):
  for i in range(2,num):
    if num %i==0:
      return False
  return True

def get_primes():
  num=2
  while True:
    if is_primes(num):
      yield num
      num+= 1
for i in get_primes():
  print(list(get_primes()))
  

print(is_primes(941))


def numbers(x):
  for i in range(x):
    if i%2 == 0:
      yield i

print(list(numbers(111)))



#kahich samjla nhi yeild command in question mark prime numbers kashe use karayche in question mark
#
