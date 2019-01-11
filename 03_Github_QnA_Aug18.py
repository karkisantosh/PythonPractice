#GitHub Python practice problems 

#%%    ....Santosh Karki......26 Aug 2018 
#numbers which are divisible by 7 but are not a multiple of 5
def Q1():
    L = []
    for i in range (2000, 3201):
        if i % 7 == 0:
            if i % 5 != 0:
                L.append(str(i))
    print(','.join(L))

#%%    ....Santosh Karki......26 Aug 2018 
def Q2(x):
    fact = 1
    i = 1
    while i <= x:
        fact = fact * i
        i = i+1
    print(fact) 

def Q2b(y):
    fact = 1
    for i in range(1, y+1):
        fact = fact * i
        i = i + 1
    print(fact)

#%%    ....Santosh Karki......26 Aug 2018 
def Q3(n):
    mydict = {}
    for i in range(1,n+1):
        mydict[i] = i*i
    print(mydict)
   
#%%    ....Santosh Karki......26 Aug 2018   
def Q4():
    x = input('Enter the comma seperated numbers ')
    L1 = x.split(',')
    T1 = tuple(L1)
    print(L1)
    print(T1)
  
#%%    ....Santosh Karki......26 Aug 2018  
import math
def Q6():
    x = input('Enter the comma seperated numbers ')
    Lin = x.split(',')
    Lout = []
    for item in Lin:
        ans = int(math.sqrt((100 * int(item) / 30)))
        Lout.append(str(ans))
    print(','.join(Lout))
  
#%%    ....Santosh Karki......26 Aug 2018  
def Q8():
    x = input('Enter the comma seperated strings ')
    L = x.split(',')
    L.sort()
    print(','.join(L))

#%%    ....Santosh Karki......26 Aug 2018  
def Q9():
    L = []
    while True:
        x = input('Enter the lines ')
        if x:
            L.append(x.upper())
        else:
            break
    for line in L:
        print(line)
#%%    ....Santosh Karki......26 Aug 2018      

def Q10():
    x = input('Enter the words')
    L = []
    Lin = x.split(' ')
    for word in Lin:
        if word in L:
            continue
        L.append(word)
    L.sort()
    return(' '.join(L))
#%%    ....Santosh Karki......26 Aug 2018  
def Q11():
    x = input('Enter the comma seperated 4digit binary numbers ')
    Lout = [ ]
    Lin = x.split(',')
    for item in Lin:
        if int(item,2) % 5 == 0:
            Lout.append(item)
    print(','.join(Lout))

#%%    ....Santosh Karki......26 Aug 2018  
def Q12():
    Lin =[]
    for num in range(1000, 3001):
        n = str(num)
        if int(n[0])%2==0 and int(n[1])%2==0 and int(n[2])%2==0 and int(n[3])%2==0:
            Lin.append(n)
    print(','.join(Lin))

#%%    ....Santosh Karki......26 Aug 2018  
def Q13():
    x = input('Enter the sentence')
    letters = 0
    digits = 0
    Lin = x.split()
    for word in Lin:
        for ch in word:
            if ch.isdigit():
                digits = digits + 1
            if ch.isalpha():
                letters = letters + 1   
    print('LETTERS=', letters)
    print('DIGITS=', digits)

#%%    ....Santosh Karki......27 Aug 2018  
def Q14():
    x = input('Enter the sentence')
    upletters = 0
    lowletters = 0
    Lin = x.split()
    for word in Lin:
        for ch in word:
            if ch.isupper():
                upletters = upletters + 1
            if ch.islower():
                lowletters = lowletters + 1   
    print('Upper case Letters=', upletters)
    print('Lower case Letters=', lowletters)

#%%    ....Santosh Karki......17 Sep 2018  
def Q15():
    x = input('Please enter one digit integer: ')
    n = int(input ('Repeat how many times? :'))
    sumof = 0
    for i in range(1, n+1):
        num = int(x * i)
        print(num)
        sumof = sumof + num
    print(sumof)

#%%    ....Santosh Karki......18 Sep 2018  
def Q16():
    userinput = input('Enter the list of integers seperated by comma: ')
    oddlist = []
    numlist = userinput.split(',')
    for numstr in numlist:
        num = int(numstr)
        if num % 2 == 0:
            continue
        oddlist.append(str(num))
    print(','.join(oddlist))

#%%    ....Santosh Karki......18 Sep 2018     
def Q17():
    balance = 0
    while True:
        userinput = input('Enter your transactions: ')
        if userinput == '':
            break
        L1 = userinput.split(' ')
        if L1[0] == 'D':
            balance = balance + int(L1[1])
        elif L1[0] =='W':
            balance = balance - int(L1[1])
    print(balance)


#%%    ....Santosh Karki......19 Sep 2018     
import re    
def Q18():
    ans = []
    pwdstr = input('Enter the passwords seperated by comma: ')
    pwdlist = pwdstr.split(',')
    for pwd in pwdlist:
        if not re.search('[a-z]',pwd):
            continue
        elif not re.search('[A-Z]',pwd):
            continue
        elif not re.search('[0-9]',pwd):
            continue
        elif not re.search('[$#@]',pwd):
            continue
        else:
            pass
        ans.append(pwd)
    print(','.join(ans))
  
#%%    ....Santosh Karki......20 Sep 2018
#sorted
#operator
from operator import itemgetter, attrgetter
def Q19():
    mylist = []
    while True:
        userentry = input('Enter Name, Age & Score : ')
        if not userentry:
            break
        L1 = userentry.split(',')
        T1 = tuple(L1)
        mylist.append(T1)
# sort by name then age & finally by score
    print(sorted(mylist, key=itemgetter(0,1,2)))
    print('...........')
# sort by score
    print(sorted(mylist, key=itemgetter(2)))
    
#%%    ....Santosh Karki......21 Sep 2018 
def test1():
    mystring = input('Enter the string to be sorted: ')
    print(sorted(mystring.split(), key=str.lower))
     
#%%    ....Santosh Karki......21 Sep 2018        
def Q20_pre(n):
    for i in range (0,n):
        if i % 7 == 0:
            yield i
def Q20():
    x = int(input('Enter the max number: '))
    for j in Q20_pre(x):
        print (j)  
#%%    ....Santosh Karki......21 Sep 2018.... same as above 
#yield
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j
x = int(input('Enter the string to be sorted: '))
for i in putNumbers(x):
    print (i)        

#%%    ....Santosh Karki......22 Sep 2018
import math   
def Q21():
    x = 0
    y = 0
    while True:
        userinput = input('Enter Movement: ')
        if not userinput:
            break
        T1 = tuple(userinput.split())
        if T1[0] == 'UP':
            x = x + int(T1[1])
        elif T1[0] == 'DOWN':
            x = x - int(T1[1])
        elif T1[0] == 'RIGHT':
            y = y + int(T1[1])
        elif T1[0] == 'LEFT':
            y = y - int(T1[1])
    print(int(math.sqrt(x**2 + y**2)))
# ans is 'distance' NOT co-ordinates          
            
#%%    ....Santosh Karki......22 Sep 2018 
# Histogram example          
def Q22():
    userinput = input('Enter the string: ')
    L1 = userinput.split()
    L1.sort()
    D1 = {}
    for word in L1:
        D1[word] = D1.get(word, 0) + 1
    for tup in D1.items():
        print(tup[0]+':'+str(tup[1]))

#%%    ....Santosh Karki......22 Sep 2018 
# Same as above but w/o shortcut
def Q22a():
    userinput = input('Enter the string: ')
    L1 = userinput.split()
    L1.sort()
    D1 = {}
    for word in L1:
        if D1.get(word) == None:
            D1[word] = 1
        if D1.get(word) != None:
            D1[word] = D1[word] + 1
    for tup in D1.items():
        print(tup[0]+':'+str(tup[1])) 

#%%    ....Santosh Karki......22 Sep 2018 
# Same as above 
#construct dictionary #dictionary
def Q22b():
    userinput = input('Enter the string: ')
    L1 = userinput.split()
    L1.sort()
    D1 = {}
    for word in L1:
        D1[word] = D1.get(word, 0) + 1
    for key in D1:
        print ("%s:%d" % (key,D1[key]))
  
#%%    ....Santosh Karki......22 Sep 2018 
# Same as above 
#string.format #format
def Q22c():
    userinput = input('Enter the string: ')
    L1 = userinput.split()
    L1.sort()
    D1 = {}
    for word in L1:
        D1[word] = D1.get(word, 0) + 1
    for key in D1:
        print ("{}:{}".format(key,D1[key]))   
 
#%%    ....Santosh Karki......22 Sep 2018   
# checking is a number is prime
def Prime1():
    x = int(input('enter number'))
    L1 = []
    for i in range(2, x):
        if x % i == 0:
            L1.append(i)
    if len(L1) == 0:
        print('prime')
    else:
        print('not prime')

#%%    ....Santosh Karki......22 Sep 2018   
# Finding prime numbers upto a given number n
def Prime1(num):
    x = int(num)
    L1 = []
    for i in range(2, x):
        if x % i == 0:
            L1.append(i)
    if len(L1) == 0:
        return True
    else:
        return False
def primenum(n):
    L2 = []
    for i in range(2,n):
        if Prime1(i):
            L2.append(i)
    print(L2)

#%%    ....Santosh Karki......23 Sep 2018 
#sort() works only on Lists & sorts it in place
#sorted() works on any iterable including lists & creates new list/iterable
#operator module #itemgetter function/method  
#itemgetter takes index as parameter. 
#attrgetter takes attribute as parameter (thus used in class for objects)
# Just examples to demnstrate usage
L1 = [('name1', 23, 50, 20), 
      ('name2', 32, 45, 25), 
      ('name3', 25, 58, 19), 
      ('name4', 10, 62, 54), 
      ('name5', 33, 65, 12), 
      ('name6', 22, 55, 33)]

L1.sort(key = lambda abc : abc[1])
print(L1)
L1.sort(key = lambda abc : abc[2])
print(L1)
sorted(L1, key = lambda abc : abc[3])

import operator
sorted(L1, key = operator.itemgetter(2))

#sort by multiple 

sorted(L1, key = operator.itemgetter(1,2,3))

#%%    ....Santosh Karki......23 Sep 2018 
#sorting dictionary
D1 = {'e':5, 'a':1, 'c':3, 'd':4, 'b':2}

#To see only Keys sorted, use:
sorted(D1)

#To see only both Keys & corresponding values sorted, use for loop:

for key in sorted(D1):
    print(key, ":", D1[key])

#can even create a new dict. with sorted k:v pairs 

D2 = {} 
L1 = []   
for key in sorted(D1):
    L1.append(key)
print(L1)
for item in L1:
    D2[item] = D1[item]

print(D2)    

#other way to see sorted dict. in the form of a list
import operator
L3 = sorted(D1.items(), key = operator.itemgetter(0))
  
#%%    ....Santosh Karki......23 Sep 2018 
#sorting data in csv
import csv
import operator
fh1 = open('name of file.csv')
csv_data = csv.reader(fh1) 

sorted_csv_data = sorted(csv_data, key = operator.itemgetter(1))
#or use the following:
sorted_csv_data = sorted(csv_data, key = lambda num : num[1])  

for i in sorted_csv_data:
    print(i)

#%%    ....Santosh Karki......25 Nov 2018 
# Github excercise for Cisco NW prog. black belt
"""
**Only 1 .py file should be created, containing the solution to both the questions below. Use python version 3**

  a) Print the current date and time at the start of the program *(hint: use the datetime library and search the internet)* 
  
  b) Print out all the even numbers from the below given list of numbers. Write the solution into a function and have it called in your main block for the requested answer *(hint: use loops)*
"""
numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
def evennum(numlist):
    for i in numlist:
        for k,v in i.items():
            for num in v.split(','):
                if int(num) % 2 != 0:
                    continue
                print(num)
import datetime
x = datetime.datetime.now()
print(x)
evennum(numbers)
    
#%%    




#%%        