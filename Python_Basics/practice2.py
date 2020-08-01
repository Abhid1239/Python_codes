from math import *
def printTwice(bruce):
    print(bruce,bruce)
    print()

def joinstring(one,two):
    all=one+two
    printTwice(all)

def parity(x):
    if x%2 == 0:
        print("this is an even no.")
    else :
        print("this is an odd no.")

def compare(x,y):
    if not isinstance(x, int):
        print ("Factorial is only defined for integers.")
        return -1
    elif (x < 0):
        print ("Factorial is only defined for positive integers.")
        return -1
    if(x>y):
        return 1
    elif(x<y):
        return -1
    else:
        return 0

def distance(x,y,a,b):
    return sqrt((x-a)**2 + (y-b)**2)

  
#find the slope and also find the x and y intercept of the given coordinates
def slope(x,y,a,b):
    slop=(y-b)/(x-a)
    print("this is the slope of the given coordinatex",slop)

def isBetween(l,m,n):
    if(l<=m<=n):
        return True
    return False

def factorial(z):
    if(z==0):
        return 1
    else:
        return z*factorial(z-1)

# fibonacci meaning is f(x)=f(x-1)+f(x-2) & f(0)=1 & f(1)=1
def fibonacci(c):
    if(c==0):
        return 0
    else:
        return c+fibonacci(c-1)

def fibonacc (n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

one="thi is "
two="what the "
#joinstring(one,two)
#printTwice('this is cool     '*2)
print()
print(int(7/3),7%3,7//3)

print(5==6 and "x igiv" )
x=int(input("type any number"))
parity(x)

result =compare(5,6)
print(result)

print("total distance between two points is", int(distance(4,5,8,12)))

slope(4,5,8,12)

print(isBetween(4,5,6))
print(fibonacci(7))
print(fibonacc(7))


#-----------------------------------------------------------------
# iteration

#two values cannot be stored in one variable

print(3,) # tried to get the values in same line by using comma
print(4)

# a program which has not been proved whether it can be terminate or not
def sequence(n):
    while n != 1:
        print (n),
        if n%2 == 0:        # n is even
            n = n/2
        else:               # n is odd
             n = n*3+1   

#-----------------------------------------------------------------
x=1
while x <10.0:
    print(x, "\t", log2(x))
    x=x+1

x=1
while x <1025:
    print(x, "\t", log2(x))
    x=x*2
#-----------------------------------------------------------------

print("produces \n \tthis \n \t \t output.,",),print(" was it continued")

#-----------------------------------------------------------------

def mul(n):
    i=1
    while i<=10:
        print(n*i,"\t", end="")
        i=i+1
def noftable(x):
    n=1
    while n <=x:
        mul(n)
        n=n+1
#-----------------------------------------------------------------
new ="this"
length=len(new)
n=0
while n < length:
    print(new[n])
    n=n+1

for char in new:
    print(char)

#-----------------------------------------------------------------
prefixes = "JKLMNOPQ"
suffix = "ack"
suff="uack"

for letter in prefixes:
    if letter =="O" or letter =="Q":
        print(letter+suff)
    else:
        print(letter+suffix)
#-----------------------------------------------------------------
def find (str,cha): # to find a letter from a string
    index=0
    for char in str:
        if(char==cha):
            return index
        index+=1
    return -1
print(find("abcdifhvi","d"),"the output is correct")

#This pattern of computation is sometimes called a “eureka” traversal because as soon as we find what we are looking for, we can cry “Eureka!” and stop looking.

#-----------------------------------------------------------------
#import string
#from string import find
#string.find("banana","na")
#string.find("banana",na,3)     string.whitespace ?????
#print(string.ascii_lowercaase,"baNAna")

#-----------------------------------------------------------------

# LIST
lst=["hello", 2.0, 5, [10, 20]]
print(lst[2])

lst2=[range(1,11)]
print(lst2)
lst3 = range(1,10,3)

horsemen = ["spam!", "1", ["Brie", "Roquefort", "Pol le Veq"], [1, 2, 3]]

for string in horsemen:
    print (string)
    print(len(string))

#list membership can be checked by using in operator for eg.

print("spam!"in horsemen) #it is true

#for VARIABLE in LIST:
#      BODY
#This statement is equivalent to:
i=0
#while i < len(LIST):
#   VARIABLE = LIST[i] BODY
#   i=i+1
#The for loop is more concise because we can eliminate the loop variable, i. Here is the previous loop written with a for loop.
#for horseman in horsemen:
#   print horseman
#It almost reads like English: “For (every) horseman in (the list of) horsemen, print (the name of the) horseman.”

#-----------------------------------------------------------------

#TUPLE

tup1=('a','b','c')
tup2=('d','e','f')
tup2=('a',)+tup2[1:]
print(tup2)

tup1, tup2 =tup2, tup1

print(tup1,tup2)

def swap(a,b):
    return b,a

tup1, tup2 = swap(tup1,tup2)

print(tup1,tup2)

# RANDOM

from random import *

for i in range(10) :
    print(int((random())*10))

# imp list of random numbers

def randomlist(x):
    lst=[0]*x
    for n in range(x):
        lst[n]=int(random()*10)
        #print(lst)
    return lst

lst=randomlist(5000)# done

num=[0]*10
for v in lst:
    for i in range(0,10):
        if i==v:
            num[i]=num[i]+1

print(num)


#function to randomise a list of n numbers and seeing which no., repeates itself after
# n number of times dependent on the user

def listnum(list_size,number_of_division):
    lst=[0]*list_size
    num=[0]*number_of_division
    for zero in lst:
        lst[zero]=int(random()*10)
        for no in range(number_of_division):
            if no==lst[zero]:
                num[no]=num[no]+1
    return num,lst

num, lst=listnum(20000,10)
print(num)
new=0
for no in num:
    new=new+no

print(new)

#---------------------------------------------------------------------------------------------------


#DICTIONARIES

# dictonaries is used to assign names to variables instead of index
# so we can use apples =240 then just call apple and we can get the value of the no. of apples

dict={}

dict['one']='it says it has only one varible or count'
dict['new']='it states that something which was not present has came into picture'

print(dict)

eng2spa={'one':'uno','two':'dos','three':'tres','four':'focn','five':'fice'}
print(eng2spa)
print(eng2spa['two'])

del eng2spa['two']

eng2spa['one']=0
print(len(eng2spa))
print(eng2spa)


#dictonary methods where we use keys() fuunction to find all the keys of the dictonariees
# values to show all values and items to show all keys and values
print(eng2spa.keys())
print(eng2spa.values())
print(eng2spa.items())
# has_key to check whether there is a key or not
#print(dict.has_key('seven'))

#aliasing & copyingg


span=eng2spa.copy()

# matrix to dictonary conversion

matrix=[[0,0,0,0,0],[0,4,0,0,3],[0,0,0,0,0],[0,0,8,0,0]]

mat={(1,1): 4, (1,4): 3, (3,2): 8}

# here we can directly get the values but the problem is for zeros so we can use get function

print(mat.get((0,4),0))  #ans is 0



def fib (n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(10))

from random import *
dic={}
def listnu(list_size,number_of_division):
    lst=[0]*list_size
    
    for zero in lst:
        lst[zero]=int(random()*10)
        for no in range(number_of_division):
            
            if no==lst[zero]:
                dic[no]=dic.get(no,0)+1
    return dic,lst

num, lst=listnu(20000,10)
print(num)
new=0
for no in num:
    new=new+no

print(new)

numlist=num.items()
#sort=numlist.sort() it can be used on letter but giving problem for numbers

#---------------------------------------------------------------------------------------------------



#FILES & EXCEPTION

# The files whic are stored in a computer are like directories where the stored file
# is the value and the location identity is the dictonary

# work on file reading and writing and storing values and strings

# information about the error and exceptions and try and catch method for error handling

#---------------------------------------------------------------------------------------------------

#CLASSES & OBJECTS


#A class definition looks like this:
class Point:
  pass

# here a class is like an import statement where multiple functions livve
# for eg. class point is generated now we will assign pont to a word

coord = Point()

coord.x=3
coord.y=5

dist=(coord.x)**2+(coord.y)**2
print(dist)

def printpoint(p):
    print(str(p.x),str(p.y))

printpoint(coord)

low=Point()
high=Point()

low.a=5
low.b=7
high.a=5
high.b=9

print(low is high)

low=high
print(low is high)

low.x=10
low.y=20

def samepoint(low,high):
    return (low.a==high.a) and (low.b==high.b)

print(samepoint(low,high))

#Rectangle class
class rectangle:
    pass

box=rectangle()

box.length=10
box.breadth=20

box.axis=Point()

box.axis.x=5
box.axis.y=5


def center(box):
    c=Point()
    c.x = box.axis.x+box.length/2
    c.y = box.axis.y+box.breadth/2
    
    return c

m=center(box)
printpoint(m)
# ERROR SOLVEDprint(Point(m)) cant find how to remove error and didnt correctly solved
# understand the usage of classes and objects


#EXCERSIE

rec=rectangle()

rec.length=30
rec.breadth=20
rec.axis=Point()
rec.axis.x=10
rec.axis.y=15

def moverect(t,a,b):
    t.axis.x=t.axis.x + a
    t.axis.y=t.axis.y + b

moverect(rec,10,10)

print(rec.axis.x,rec.axis.y)

# same point jr copy karayche astil tr just use copy function i.e

from copy import *

new = copy(rec)

print(new.axis.x,new.axis.y)

# but we should use deep copy as it creates a whole different object 

box2=deepcopy(box)

#done


#---------------------------------------------------------------------------------------------------

#CLASSES AND FUNCTIONS


#time

class Time:
    pass

time =Time()

time.hour=11
time.minute=50
time.sec = 12

print(time)

#EXERCISE1
ct=Time()
ct.hour=5
ct.minute=56
ct.sec=59


def printTime(x):
    print(str(x.hour) + ":" + str(x.minute) + ":" +str(x.sec))

printTime(ct)

#EXCERCISE2

def addtime(x,y):
    sum=Time()
    sum.hour = x.hour+y.hour
    sum.minute=x.minute+y.minute
    sum.sec = x.sec + y.sec
    #Functional Programming style
    if sum.sec >=60:
        sum.sec=sum.sec-60
        sum.minute=sum.minute+1
    if sum.minute>=60:
        sum.minute=sum.minute- 60
        sum.hour=sum.hour+1
        
    return sum

done=addtime(time,ct)
printTime(done)

#Prototype Development

#pure function: A function that does not modify any of the objects it receives as arguments. Most pure functions are fruitful.
#modifier: A function that changes one or more of the objects it receives as ar- guments. Most modifiers are fruitless.
#functional programming style: A style of program design in which the ma- jority of functions are pure.
#prototype development: A way of developing programs starting with a proto- type and gradually testing and improving it.
#planned development: A way of developing programs that involves high-level insight into the problem and more planning than incremental development or prototype development.
#algorithm: A set of instructions for solving a class of problems by a mechanical, unintelligent process.

def timetosec(x):
    min=x.hour*60+x.minute
    sec=min*60+x.sec
    return sec

def sectotime(x):
    time=Time()
    time.hour=(x//3600)
    time.minute=(x%3600)//60
    time.sec = x%60
    return time

def addt(x,y):
    sec=timetosec(x)+timetosec(y)
    return sectotime(sec)

printTime(addt(time,ct))

#---------------------------------------------------------------------------------------------------

#CLASSES AND METHODS

#object oriented features


class Time():
    def printtime(x):
        print(x.hour,':',x.min,':',x.sec)
        
    def timetosec(x):
        minute =x.hour*60 + x.min
        sec=minute*60+x.sec
        return sec
    def sectotime(self,x):
        time=Time()
        time.hour=(x//3600)
        time.min =(x%3600)//60
        time.sec = x%60
        time.printtime()
        return time
    def addt(self,y):
        sec=self.timetosec()+y.timetosec()
        return self.sectotime(sec)
    

time=Time()
time.hour=10
time.min=20
time.sec=30

ct=Time()
ct.hour=5
ct.min=56
ct.sec=59

time.printtime()

sec=time.timetosec()

time.sectotime(sec)

time.addt(ct)


# the initializing method
# finally the usage of init it is to use the class name for eg.



class Times():
    def __init__(self,hour=0,min=0,sec=0):
        self.hour=hour
        self.min=min
        self.sec=sec
        #return ('('+str(self.hour)+':'+str(self.min)+':'+str(self.sec)+')')
    
    def printtime(x):
        print(x.hour,':',x.min,':',x.sec)
        
    def timetosec(x):
        minute =x.hour*60 + x.min
        sec=minute*60+x.sec
        return sec
    def sectotime(self,x):
        time=Time()
        time.hour=(x//3600)
        time.min =(x%3600)//60
        time.sec = x%60
        time.printtime()
        return time
    def addt(self,y):
        sec=self.timetosec()+y.timetosec()
        return self.sectotime(sec)
    
currentTime=Times(8,38,0)
currentTime.printtime()

#so the use of class is this way. here for eg.

currentTime=Times()
currentTime.printtime()    #i.e 0:0:0 or
currentTime=Times(sec=30,min=40)
currentTime.printtime()    #i.e 0:40:30

#this way classes can be used

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return('('+str(self.x)+','+str(self.y)+')')


cord=Point(3,4)
print(str(cord))
print(cord)

#---------------------------------------------------------------------------------------------------

#SETS OF OBJECTS

#cards game

class card:
    suit=["clubs","diamonds","hearts","spade"]
    rank=["extra","Ace","2","3","4","5","6","7","8","9","Jack","Queen","King"]
    
    




