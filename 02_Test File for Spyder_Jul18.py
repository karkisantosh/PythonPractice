# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 19:18:54 2018

@author: 607495308
"""

#%%

### To remove defalut next line character from print statement
print('This is Santosh')
print('and I stay in Delhi')

print('This is Santosh ', end = '')
print('and I stay in Delhi')


def printeven(N):    
    x = 2
    while x <= N:
        print(x, ',', end = '')
        x = x + 2
    print()
    print('This is the list of even numbers upto', N)

printeven(20)

#%%

###To check if string has anything other than digits. (Useful in input 
### function which expects digits/numbers only )

'string name'.isdigit() 
'12343'.isdigit()
'123.3'.isdigit() # Has a . character so returns False

#%%

newEngland = [["Massachusetts",6692824],["Connecticut",3596080],
              ["Maine",1328302],["New Hampshire",1323459],
              ["Rhode Island",1051511],["Vermont",626630]]



print ('Population \t State')
for i in newEngland:
    print(i[1], '\t', i[0])
    

    
midAtlantic = [["New York",19746227],["New Jersey",8938175],
               ["Pennsylvania",12787209]]

print('\n')

def report2(statelist):
    print ('Population \t State')
    for i in range (0, len(statelist)):
        print(statelist[i][1], '\t', statelist[i][0])

report2(midAtlantic)

print('\n')

report2(NewEngland)


#%%

fo1 = open ('mytestfile1.txt', 'w')
fo1.write('This is my first Line \n')
fo1.close()

fo1 = open ('mytestfile1.txt', 'a')
fo1.write('This is my 2nd Line')
fo1.close()


fo1 = open ('mytestfile1.txt', 'a')
for i in range (20):
    fo1.write ('This is my ..... Line \n')
fo1.close()

fo2 = open ('mytestfile2.txt', 'w')
fo2.write('This is my first Line in Flie-2 \n')
fo2.close()

fo2 = open ('mytestfile2.txt', 'r+')
fo2.write('This is my 2nd Line in Flie-2 \n')
fo2.close()

fo2 = open ('mytestfile2.txt', 'w')
fo2.write('This is my first Line in Flie-2 \n')
fo2.close()




#%%

def copyfile(fromfilename, tofilename):

    fromfile_object = open (fromfilename)
    tofile_object = open (tofilename, 'a')
    for line in fromfile_object:
        tofile_object.write(line)
    fromfile_object.close()
    tofile_object.close()


#%% 24 Jul 2018
    

import sys

name = sys.argv[1]
age = int(sys.argv[2])

print('Hello ', name, 'you will be ', age+10, ' after 10 years' )
    
#%% 24 Jul 2018

def textedit(txtfile):
    myfile = open (txtfile)
    
    for line in myfile:
        print(line)
        for word in line.split():
            print (word, end = ' ')
            print()
            for ch in word:
                print(ch)
 
#%%    25 Jul 2018
    
def texteditlist(txtfile):
    """"function to count # of lines, words & characters in a txt file & display them in list"""
    myfile = open (txtfile)
    linelist = []
    wordlist = []
    chlist = []
    for line in myfile:
        line = line.split('\n')[0]
        linelist.append(line)
    print ('Total Lines in this file are ', len(linelist))
    print(linelist)
    print()
    for i in range(len(linelist)):
        for word in linelist[i].split():
            wordlist.append(word)
        i = i + 1
    print ('Total words in this file are ', len(wordlist))       
    print(wordlist)
    print()
    for word in wordlist:
        for ch in word:
            chlist.append(ch)
    print ('Total alphabets in this file are ', len(chlist))
    print(chlist)
    



#%% 25 Jul 2018
    # doing same thing as above but with use of functions n methods

def texteditlist(txtfile):
    """"function to count # of lines, words & characters in a txt file & display them in list"""
    myfile = open (txtfile)
    data = myfile.read()
    num_lines = len(data.splitlines())
    num_words = len(data.split())
    num_ch = len(data)
    print('Total Lines in this file are ', num_lines)
    print(data.splitlines())
    print()
    print('Total words in this file are ', num_ch)
    print(data.split())
    print()
    print('Total alphabets in this file are ', num_ch)
    print(data)
    
    
    
#%%   26 Jul 2018
# Creating files
    
import sys

def createfiles(fileprefix, n):
    
    for i in range (1, n):
        fo = open(fileprefix + '_' + str(i) + '.txt', 'w')
        fo.close()
        i = i + 1

createfiles('Myfile', 10)
        
 #%%    26 Jul 2018   
# Renaming files        

import os

def renamefiles(path):
    n = 1
    list_of_files = os.listdir(path)
    for filename in list_of_files:
        if filename.startswith('Myfile'):
            newfilename = filename.replace(filename[:-4], 'Yourfile'+'_'+str(n))
            os.rename(filename, newfilename)
            print(newfilename)
            n = n + 1
#    print(os.listdir(path))    
        
renamefiles('C:\Santosh\Optional Data\Python_files\Spyder_Files\Test folder')
   
    
 #%%    26 Jul 2018   
# Renaming real files        

import os

def renamefiles(path):
    n = 1
    list_of_files = os.listdir(path)
    list_of_files.sort()
    for filename in list_of_files:
        if filename.startswith('IMG'):
            newfilename = filename.replace(filename[:-4], 'Book2_Page_' + str(n))
            os.rename(filename, newfilename)
            print(newfilename)
            n = n + 1
#    print(os.listdir(path))    
        
renamefiles('C:\Santosh\Optional Data\Docs-General Technical\Python Study Material\BookTry')
   

#%% 27 Jul 2018 Just testing

import os        
def numcount(path):
    list_of_files = os.listdir(path)
    L = []
    L_new = []
    for filename in list_of_files:
        if filename.startswith('IMG'):
            x = int(filename[4:8])
            L.append(x)
    print(L)
    print
    L.sort()
    print(L)
    for i in range(1, len(L)):
        L_new.append(i)
    print(L_new)
    
        
numcount('C:\Santosh\Optional Data\Docs-General Technical\Python Study Material\BookTry')            
          

#%% 27 Jul 2018 Just testing


abc = [2,4,6,76,87,90,9,76,34,66]
print(abc)
abc.sort()
print()
print(abc)

for i in range(1, 11):
    print(i)
    
     
#%%   27 Jul 2018 
# fibonacci series upto number n

def fibo(n):
   num1 = 1
   num2 = 0
   i=0
   L = []
   while i<n:
       num3= num1 + num2 
       L.append(num3)
       num1 = num2          # we can also do num1, num2 = num2, num3
       num2 = num3
       i = i+1
   print('Fibonacci Series upto number', n, 'is')
   print(L)
       
#%%     28 Jul 2018 

import csv
def makecsv(filename, L):
    
    fo = open(filename, 'w', newline = '')
    for item in L:
        csv.writer(fo).writerow(item)
    fo.close()
# Example file

List1 = [['Name', 'Age', 'EIN'], ['Santosh', 42, 607654345], ['Sundar', 30, 9876543]]
List2 = ['Name', 'Age', 'EIN']

makecsv('mycsvfile1.csv', List1)
makecsv('mycsvfile2.csv', List2)     
    
#%% 28 Jul 2018 

import csv

L = []
L2 = []
f = open('Test file for Spyder.csv')
for row in f:
    L.append(row)
f.close()

#%% ....Santosh Karki......29 Jul 2018

import csv
def updatecsv(oldfilename):
    fo1 = open(oldfilename)
    sum = 0
    L1 = []
    for row in csv.reader(fo1):
        L1.append(row)
    for item in L1:
        if item[1].isdigit():
            sum = sum + int((item[1]))
    avg = sum / (len(L1)-1)
    print(avg)        
    L1.append(['Average', avg ])
    fo1.close()
    fo1 = open(oldfilename, 'w', newline = '')
    for item in L1:
        csv.writer(fo1).writerow(item)
    fo1.close()

       
#%%   ....Santosh Karki......30 Jul 2018

import random

x = random.random() # gives random number between 0 & 1
print(x)

y = random.random()*50 # gives random number between 0 & 50
print(y)

z = random.random()*50 + 100 # gives random number between 100 & 150
print (z)

ab = random.random()*20 + 5 # gives random number between 5 & 25
print(ab)


#%%    ....Santosh Karki......30 Jul 2018

# random number between num1 & num2

import random
def random_real_num(a, b):
    return (b-a)* random.random() + a 
    
#%%     ....Santosh Karki......30 Jul 2018   
    
import random

def random_real_list(n):
    L = []
    for i in range(n):
        L.append(random_real_num(5000, 6000))
    print(L)        

def random_real_num(a, b):
    return (b-a)* random.random() + a 


#%% ....Santosh Karki......30 Jul 2018 

def testfun(numb):
    try:
        num = int(numb) + 100
        print('adding 100 to this will result in', num)
    except Exception as e:
        print('Oops its not a number. The Python error is: \n', e)
        



#%% ....Santosh Karki......31 Jul 2018 
        
def testf1(fname, lname):
    print('My firstname is', fname, 'and lastname is', lname )
    
def testf2(fname, lname):
    print('My firstname is {} & lastname is {}'.format(fname,lname))
    
def testf3(fname, lname):
    print('My firstname is {0} & lastname is {1}'.format(fname,lname))    
    # same as above. No change if we put argument index numbers inside{}



#%%    ....Santosh Karki......13 Aug 2018

while True:
    try:
        x = int(input ('Whats your age? : '))
        if x == 0:
            print('The end')
            break   
        elif x <=40:
            print('U r young')
        elif x <=60:
            print('u r ok')
        else:
            print('You are old')
    except:
        print("Not a number. Please enter digits only !")
        quit()
print ('Program Ends !!')

#%%    ....Santosh Karki......13 Aug 2018

def grade():
    

    while True:
        score = input("Enter Score: ")
        if score.lower() == 'none':
            print('Thanks')
            break
        try:
            s = float(score)
        except:
            print('Error. Not a valid score.')
            continue
        if s >= 1.0:
            print('Error - Out of Range')
            continue
        elif s >= 0.9:
            print('A')
        elif s>=0.8:
            print('B')
        elif s >=0.7:
            print ('C')
        elif s >=0.6:
            print('D')
        elif s>=0.0:
            print('F')
        else:
            print('Error - Out of Range')

#%%    ....Santosh Karki......13 Aug 2018
    
while True:
    text = input ('>>>> ')
    if text == 'done':
        break
    print (text)
print('Finis')


#%%    ....Santosh Karki......13 Aug 2018

def largeNsmall():
    L = []
    while True:
        xstr = input ('Enter the Number (& when done type None): ')
        if xstr.lower() == 'none':
            break
        try:
            x = int(xstr)
            L.append(x)
        except:
            print('Not a number. Please enter a number!')            
    max = L[0]
    for i in L:
        if i > max:
            max = i
    
    min = L[0]
    for i in L:
        if i < min:
            min = i
    
      
    print('Out of', L)
    print('Largest number is:', max, ', and Smallest number is:', min)  

    total = 0
    for i in L:
        total = total + i
        
    print('Sum of all numbers is:', total)
    print('Average of numbers is:', total/len(L))
    
#%%    ....Santosh Karki......13 Aug 2018

def largesmall():
    

    largest = None
    smallest = None
    
    while True:
        num = input("Enter a number: ")
        if num == "done" : 
            break
        
        try:
            inum = int(num)
        except:
            print('Invalid Input')
            continue
        
        if largest is None:
            largest = inum
        elif inum > largest:
            largest = inum
        
        if smallest is None:
            smallest = inum
        elif inum < smallest:
            smallest = inum
        
    print("Maximum is ", largest)
    print("Minimum is ", smallest)

#%%    ....Santosh Karki......20 Aug 2018
# Same as above but w/o else..... i.e. by adding or to reduce code    

def largesmall2():
    largest = None
    smallest = None
    while True:
        num = input("Enter a number: ")
        if num == "done" : 
            break
        try:
            inum = int(num)
        except:
            print('Invalid Input')
            continue
        if largest is None or inum > largest:
            largest = inum
        if smallest is None or inum < smallest:
            smallest = inum
    print("Maximum is ", largest)
    print("Minimum is ", smallest)
 
#%%    ....Santosh Karki......13 Aug 2018

def countvouwle(string):
    count = 0
    counta = 0
    for alp in string:
        if alp.lower() in ['a', 'e', 'i', 'o', 'u']:
            count = count + 1
        if alp.lower() == 'a':
            counta = counta + 1
                
    print('# of vouwles in this string are:', count)
    print('# "a" in this string are:', counta)
          
  

#%%    ....Santosh Karki......13 Aug 2018

def mytitle(str):
    for word in str.split():
        print(word[0].upper()+word[1:].lower(), end = ' ')

#%%    ....Santosh Karki......14 Aug 2018
    
def yangfile(filename):
    leaves = []
    fo = open(filename)
    for line in fo:
        line = line.strip()
        if line.startswith('leaf '):
            lpos = line.find('{')
            leaves.append(line[len('leaf '):(lpos-1)])
    print(leaves)

#%%    ....Santosh Karki......14 Aug 2018
#exactly same functionality as above but with inverted logic & 'continue'
    
def yangfile2(filename):
    leaves = []
    fo = open(filename)
    for line in fo:
        line = line.strip()
        if not line.startswith('leaf '):
            continue
        lpos = line.find('{')
        leaves.append(line[len('leaf '):(lpos-1)])
    print(leaves)


#%%    ....Santosh Karki......14 Aug 2018

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)

#%%    ....Santosh Karki......14 Aug 2018
   
def strman():
# Use the file name mbox-short.txt as the file name
    fname = input("Enter file name: ")
    fh = open(fname)
    count = 0
    total = 0
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") : 
            continue
        count = count + 1
        num = float(line.strip('X-DSPAM-Confidence:'))
        total = total + num
    avg = total / count    
    print("Average spam confidence:", avg)
     
#%%    ....Santosh Karki......14 Aug 2018
        
def abc():
    x = 'Any string'
    L = []
    for item in dir(x):
        if item[0] == '_':
            continue
        L.append(item)
    print('Methods available for strings:')
    print(L)
    print()
    L1 = []
    for item in L:
        if item.startswith('is'):
            L1.append(item)
    print('Methods available for strings that start with "is":')
    print(L1)
    print()
    L3 = []
    for item in dir(L1):
        if item[0] == '_':
            continue
        L3.append(item)
    print('Methods available for Lists:')
    print(L3)       
   
#%%    ....Santosh Karki......14 Aug 2018

def Avg():
    L = []
    while True:
        num = input('Enter the number: ')
        if num == 'done':
            print('Thanks')
            break
        inum = float(num)
        L.append(inum)
    avg = sum(L) / len(L)
    print('Average is: ', avg)

#%%    ....Santosh Karki......14 Aug 2018

def xyz(filename):

    fh = open(filename)
    filestr = fh.read()
    filewords = filestr.split()
    wordlist = []
    for word in filewords:
        if word in wordlist:
            continue
        wordlist.append(word)
    print(wordlist)
    fh.close()

#%%    ....Santosh Karki......14 Aug 2018

fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From '):
        continue
    count = count + 1
    line = line.split()
    print(line[1])

print("There were", count, "lines in the file with From as the first word")

#%%    ....Santosh Karki......14 Aug 2018

def makedic(filename):
    fh = open(filename)
    filestr = fh.read()
    filewords = filestr.split()
    wordlist = []
    for word in filewords:
        wordlist.append(word)
    print(wordlist)
    print()
    fh.close()
    mydic = {}
    for item in wordlist:
        mydic[item] = mydic.get(item, 0) + 1
    print(mydic)
  
#%%    ....Santosh Karki......14 Aug 2018

D1 = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5}
print()
print(D1.items())
print()
print(D1.keys())
print()
print(D1.values())
print()

print('To see all Keys one at a time:')
for key in D1:
    print(key)
print()    
print('To see all values one at a time:')
for key in D1:
    print(D1[key])
print()
for i in D1.items():
    print(i)
print()
for i, j in D1.items(): # Only Python can do it !! iterate on 2 variables !
    print(i, j)

#%%    ....Santosh Karki......14 Aug 2018

D1 = {'jan':3455, 'feb':3323, 'mar':8839, 'apr':3234, 'may':8805}

if 'jan' in D1:
    D1['jan'] = D1['jan'] + 1
else:
    D1['jan'] = 1
    
# or can be written as:

D1['jan'] = D1.get('jan',0) + 1    

    
    
#%%    ....Santosh Karki......14 Aug 2018

def makedic2(infile):
    fh1 = open(infile)
    worddic = {}
    for line in fh1:
        words = line.split()
        for word in words:
            worddic[word] = worddic.get(word,0)+1
    fh2 = open('output3.txt', 'w')
    for i in worddic.items():
        fh2.write(str(i))
    fh2.close()        
            
#%%    ....Santosh Karki......14 Aug 2018

def mostrepeatedword(infile):
    fh1 = open(infile)
    worddic = {}
    for line in fh1:
        words = line.split()
        for word in words:
            worddic[word] = worddic.get(word,0)+1

    maxcount = None
    most = None
    for i,j in worddic.items():
        if maxcount is None or j > maxcount:
            maxcount = j
            most = i
    print('Most repeated word in this file is:', most, '....and its repeated',maxcount, 'times')
        
#%%    ....Santosh Karki......14 Aug 2018

fname = input("Enter file name: ")
D1 = {}
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From '):
        continue
    count = count + 1
    line = line.split()
    print(line[1])

print("There were", count, "lines in the file with From as the first word")



#%%    ....Santosh Karki......19 Aug 2018

def dictofsquares(N):
    outputdict = {}
    for i in range (1, N):
        outputdict[i] = i**2
    print(outputdict)
    
    for i, j in outputdict.items():
        print('square of',i, 'is', j)


#%%    ....Santosh Karki......19 Aug 2018 
# Same function as above but with just one line !
        
def dictofsquares1(N):
    return {i: i**2 for i in range (1,N)}

def dictofcubes1(N):
    return {i: i**3 for i in range (1,N)}

#%%    ....Santosh Karki......19 Aug 2018 
    
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('what is', q, '. It is', a)


#%%    ....Santosh Karki......19 Aug 2018 

for i in range(1, 10):
    print(i)
print('.........')
for i in reversed(range(1, 10)):
    print(i)
    
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in basket:
    print(i)
print('.........')
for i in sorted(set(basket)):
    print(i)
    
#%%    ....Santosh Karki......19 Aug 2018 

def wordcount1(infile):
    fh1 = open(infile)
    worddic = {}
    for line in fh1:
        words = line.split()
        for word in words:
            if word not in worddic:
                worddic[word] = 1
            else:
                worddic[word] = worddic[word] + 1
    print(worddic)
#    fh2 = open('output.txt', 'w')
#    for k, v in worddic.items():
#        fh2.write(k, v)
#    fh2.close()
    
#%%    ....Santosh Karki......20 Aug 2018 
#Exactly same function as above but w/o if-else loop
def wordcount(infile):
    fh1 = open(infile)
    worddic = {}
    for line in fh1:
        words = line.split()
        for word in words:
            worddic[word] = worddic.get(word, 0) + 1
    print(worddic)   
    
#%%    ....Santosh Karki......20 Aug 2018 

def mostrepeatedword(infile):
    fh1 = open(infile)
    worddic = {}
    for line in fh1:
        words = line.split()
        for word in words:
            worddic[word] = worddic.get(word, 0) + 1
    print(worddic)  
    print()
    maxword = None
    maxwordcount = None
    for i, j in worddic.items():
        if maxwordcount is None or j > maxwordcount: # None is for first iteration only
            maxwordcount = j
            maxword = i
    print('Word', maxword, 'is repeated the most-', maxwordcount, 'times in this file')
 
#%%    ....Santosh Karki......21 Aug 2018 
# excercise 9.4 coursera

def excercise94():
    name = input("Enter file:")
    filehandle = open (name)
    wordlist = []
    namedict = {}
    for line in filehandle:
        if not line.startswith('From '):
            continue
        line = line.split()
        wordlist.append(line[1])
    for word in wordlist:
        namedict[word] = namedict.get(word, 0) + 1
    print(namedict)
    maxcount = None
    maxname = None
    for i, j in namedict.items():
        if maxcount is None or j > maxcount:
            maxcount = j
            maxname = i
    print(maxname, maxcount)
    
#%%    ....Santosh Karki......22 Aug 2018 

D1 = {'jan':3455, 'feb':3323, 'mar':8839, 'apr':3234, 'may':8805}
print(D1.items())
print('......')
for i in D1:
    print(i)
print('......')    
for i, j in D1.items():
    print(i, j)
print('......')
for i, j in sorted(D1.items()):
    print(i, j)
print('......')
L1 = []
for i, j in D1.items():
    L1.append((j, i))
print(L1)
print('......')
sorted(L1, reverse=True)

#%%    ....Santosh Karki......22 Aug 2018 

def toptenwords(infile):
    fh1 = open(infile)
    worddic = {}
    for line in fh1:
        words = line.split()
        for word in words:
            worddic[word] = worddic.get(word, 0) + 1
    list1 = []
    for k, v in worddic.items():
        list1.append((v,k))
    list1sorted = sorted(list1, reverse = True)
    for v, k in list1sorted[:10]:
        print('word ',k, '\t', v, 'times')
    
#%%    ....Santosh Karki......22 Aug 2018 
# same as above but with less lines of code
def toptenwords1(infile):
    fh1 = open(infile)
    worddic = {}
    for line in fh1:
        words = line.split()
        for word in words:
            worddic[word] = worddic.get(word, 0) + 1
    print(sorted([(v, k) for k, v in worddic.items()], reverse=True))
# [(v, k) for k, v in worddic.items()]
# its an example of List comprehension i.e.
# list represented as an expression rather than creating an empty list & usign append in a for loop etc.
# List comprehension creates dynamic list
#%%    ....Santosh Karki......22 Aug 2018 
# Another example of list comprehension    
D1 = {'jan': 3455, 'feb': 3323, 'mar': 8839, 'apr': 3234, 'may': 8805}
print([(k, v) for k, v in D1.items()])

#%%    ....Santosh Karki......22 Aug 2018 
# excercise 10.2 coursera

def excercise102():
    name = input("Enter file:")
    templist = []
    fh = open(name)
    for line in fh:
        if not line.startswith('From '):
            continue
        line = line.split()
        for word in line:
            if ':' in word:
                word = word.split(':')
                templist.append(word[0])
#    print(templist)
    tempdict = {}
    for i in templist:
        tempdict[i] = tempdict.get(i, 0) + 1
#    print(tempdict)
    for k, v in sorted(tempdict.items()):
        print(k, v)

#%%    ....Santosh Karki......22 Aug 2018 

def finding(infile):
    fh = open(infile)
    for line in fh:
        line = line.rstrip()
        if line.find('Santosh') >=0: # line.find() returns -1 if sub-string not found in the string
            print(line)

#%%    ....Santosh Karki......22 Aug 2018 
# Same function as above but using reg. expression instead of find method
# Search function of re library returns True of False based on whether it found the substring in string.
import re
def finding1(infile):
    fh = open(infile)
    for line in fh:
        line = line.rstrip()
        if re.search('Santosh', line): 
            print(line)
           
#%%    ....Santosh Karki......22 Aug 2018 

def finding3(infile):
    fh = open(infile)
    for line in fh:
        line = line.rstrip()
        if line.startswith('Santosh'):
            print(line)


#%%    ....Santosh Karki......22 Aug 2018 
# Same function as above but using reg. expression instead of startswith method
import re
def finding4(infile):
    fh = open(infile)
    for line in fh:
        line = line.rstrip()
        if (re.search('^Santosh', line)):
            print(line)

#%%    ....Santosh Karki......22 Aug 2018 
import re
def finding5(infile):
    fh = open(infile)
    for line in fh:
        line = line.rstrip()
        x = re.findall('[0-9]+', line)
        if x != []:
            print(x)

#%%    ....Santosh Karki......23 Aug 2018 
import re
def finding6(infile):
    fh = open(infile)
    emails = []
    for line in fh:
        line = line.rstrip()
        x = re.findall('\S+@\S+', line)
        if x != []:
            if x[0] in emails:
                continue
            else:
                emails.append(x[0])
    print(emails)

#%%    ....Santosh Karki......23 Aug 2018 
# same as above but non-greedy
import re
def finding7(infile):
    fh = open(infile)
    emails = []
    for line in fh:
        line = line.rstrip()
        x = re.findall('\S+?@\S+', line)
        if x != []:
            if x[0] in emails:
                continue
            else:
                emails.append(x[0])
    print(emails)

#%%    ....Santosh Karki......23 Aug 2018 
import re
def finddomainname(infile):
    fh = open(infile)
    domains = []
    for line in fh:
        line = line.rstrip()
        x = re.findall('@([^ ]*)', line) # or we can use '@(\S*)'
        if len(x) == 0:
            continue
        if x[0] in domains:
            continue
        domains.append(x[0])
    print(domains)
#%%    ....Santosh Karki......23 Aug 2018 
# Coursera chaper 11 (re) excercise

import re    
def excercise111(infile):
    fh = open(infile)
    numlist = []
    for line in fh:
        line = line.rstrip()
        num = re.findall('[0-9]+', line)
        if num != []:
            for x in range(0, len(num)):
                numlist.append(int(num[x]))
    print(numlist)
    print(sum(numlist))
#    num_sum = 0
#    for i in numlist:
#        num_sum = num_sum + i
#        i = i + 1
#    print(num_sum)

#%%    ....Santosh Karki......23 Aug 2018 

import socket
def myscoket1():
    
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break

        print(data.decode(),end='')
    
    mysock.close()

#%%    ....Santosh Karki......24 Aug 2018     
import re
def mywork(infile):
    fh = open(infile)
    fh2 = open('output3.txt', 'w')
    for line in fh:
        line = line.rstrip()
        newline = re.findall('^[0-9]+ (.*)', line)
        for line in newline:
            fh2.write(line)
            fh2.write('\n')
    fh1 = fh2.close()
    fh2 = fh2.close()    

#%%    ....Santosh Karki......27 Aug 2018   

import urllib.request, urllib.parse, urllib.error
def mywebdata(url):
    fh = urllib.request.urlopen(url)
    for line in fh:
        print(line.decode().strip())


#%%    ....Santosh Karki......28 Aug 2018   
# example of recursion  
def factorial(n):
    if n == 1:
        return 1
    else:
        fact = n * factorial(n-1)
        return fact
#%%    ....Santosh Karki......28 Aug 2018   

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4
# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

def webdata(url):

    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl
    
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))        
        
        
#%%    ....Santosh Karki......28 Aug 2018           
# Coursera excercise
        
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
sumof = 0
tags = soup('span')
for tag in tags:
#    print(tag)
    tagstr = str(tag)
    num = re.findall('<span class="comments">(.*)</span>', tagstr)
    sumof = sumof + int(num[0])
print(sumof)
   
#%%    ....Santosh Karki......28 Aug 2018           
# Coursera excercise

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
def excercise122(url, pos, repeat):
   # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    for i in range (repeat):
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all of the anchor tags
        L = []
        tags = soup('a')
        for tag in tags:
            x = (tag.get('href', None))
            L.append(x)
    #        L.append(re.findall('/known_by_(.*).html', x)[0])
        url = L[pos-1]
    print(re.findall('/known_by_(.*).html', url)[0])
excercise122('http://py4e-data.dr-chuck.net/known_by_Lilyana.html', 18, 7)
 
#%%    ....Santosh Karki......28 Aug 2018      
import xml.etree.ElementTree as ET
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))    
     
    
#%%    ....Santosh Karki......28 Aug 2018     
import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

#%%    ....Santosh Karki......28 Aug 2018           
# Coursera excercise
import urllib.request, urllib.parse, urllib.error
import re
def excercise131(url):
    L = []
    fh = urllib.request.urlopen(url)
    for line in fh:
        line = line.decode()
        if not line.find('<count>'):
            continue
        count = re.findall('<count>(.*)<', line)
        if count != []:
            L.append(count[0]) 
    countsum = 0
    for num in L:
        countsum = countsum + int(num)
    print(countsum)

#%%    ....Santosh Karki......29 Aug 2018           
# Coursera excercise - same as above but using xml etree function
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
def excercise131b(url):
    fh = urllib.request.urlopen(url)
    urlcontent = fh.read()
#    decodedcontent = urlcontent.decode()
#    print(decodedcontent)
    xmlfile = ET.fromstring(urlcontent)
    L1 = xmlfile.findall('comments/comment')
    sum = 0
    for item in L1:
        sum = sum + int(item.find('count').text)
    print(sum)
excercise131b('http://py4e-data.dr-chuck.net/comments_126345.xml')    
#%%    ....Santosh Karki......31 Aug 2018           
# Coursera excercise 
import urllib.request, urllib.parse, urllib.error
import json
def excercise132(url):
    fh = urllib.request.urlopen(url)
    urlcontent = fh.read()
    decodedcontent = urlcontent.decode()
    print(decodedcontent)
    print("***==========================================***")
    jsonfile = json.loads(urlcontent)
    print(jsonfile)
    print("***==========================================***")
    countsum = 0
    for item in jsonfile['comments']:
        countsum = countsum + int(item['count'])
    print(countsum)
# To see indented JSON use the following     
    print(json.dumps(jsonfile, indent=4))


#%%    ....Santosh Karki......01 Sep 2018           
# Coursera excercise 
import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
#    print('Retrieved', len(data), 'characters')
#    print(data)
    jsonfile = json.loads(data)
#    print(json.dumps(jsonfile, indent=4))   
    place_id = jsonfile['results'][0]['place_id']
    print(place_id)
 
#%%    ....Santosh Karki......01 Sep 2018  
class partyanimal():
    x = 0
    def party(self):
        self.x = self.x + 1
        print('So far' , self.x)
 
#%%    ....Santosh Karki......01 Sep 2018  
import numpy as np
import matplotlib.pyplot as plt
x1 = -10
x2 = 10
y1 = -10
y2 = 10
plt.axis([x1, x2, y1, y2])
plt.axis('on')
plt.grid(True)
plt.show()

#%%    ....Santosh Karki......02 Sep 2018  

class testclass():
    start = 0
    sumof = 1
#    name = ""
    def __init__(self,a):
        self.name = a
#        print(self.name)
    def changestart(self, x):
        self.start = self.start + x
        print(self.start)
    def changesumof(self, y):
        self.sumof = self.sumof - 10
        print(self.sumof)
    def callname(self):
        print('My name is', self.name.upper())
        
class testsubclass(testclass):
    points = 10
    def addpoint():
        points = points + 5
        print(points)
    
#%%    ....Santosh Karki......03 Sep 2018 
# Coursera excercise
import sqlite3
def excercise133(fname):
    conn = sqlite3.connect('domainnamedb.sqlite')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Counts')
    cur.execute('''
    CREATE TABLE Counts (org TEXT, count INTEGER)''')
    fh = open(fname)
    for line in fh:
        if not line.startswith('From: '): continue
        pieces = line.split()
        email = pieces[1]
        org = email.split('@')[1]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                        (org,))
    conn.commit()
    # https://www.sqlite.org/lang_select.html
    sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
    for row in cur.execute(sqlstr):
        print(str(row[0]), row[1])
    cur.close()

#%%    ....Santosh Karki......03Sep18
def test(fname):
    fh = open(fname)
    for line in fh:
        if not line.startswith('From: '): continue
        pieces = line.split()
        print(pieces)
        email = pieces[1]
        print(email)
        org = email.split['@'][1]
        print(org)

#%%    ....Santosh Karki......05Sep18
# Coursera excercise    
import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('trackdb9.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE 
);          

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);    
''')

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml' 
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None
    
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    Genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None or Genre is None : 
        continue

    print(name, artist, album, count, rating, length, Genre)
#cur.execute() method allows adding data in DB
#cur.executescript() method allows creating DB tables    
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( Genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (Genre, ))
    Genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count, Genre_id) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, length, rating, count, Genre_id ) )

    conn.commit()
   
#%%    ....Santosh Karki......08Sep18
# GUI programming in Python using TKinter module  
# https://tkdocs.com/tutorial/
import tkinter as tk
def gui1():
    root = tk.Tk()
    testlable = tk.Label(root, text = 'Hello GUI ! My Name is Santosh')
    testlable.pack()
    root.mainloop()

def write_slogan():
    print("Tkinter is easy to use!")
def gui2():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    button = tk.Button(frame,text="QUIT",fg="red",command=quit)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,text="Hello Santosh !!",command=write_slogan)
    slogan.pack(side=tk.LEFT)
    root.mainloop()
    
#%%    ....Santosh Karki......08Sep18
# Coursera excercise     
import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    name = entry[0];
    title = entry[1];
    role = entry[2];

    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

    conn.commit()
    
#%%    ....Santosh Karki......28Oct18
import pandas as pd
df1 = pd.read_excel('C2M Deliverable Tracker v1.2.xlsx', sheet_name = 'Options')
print(df1.columns)
print()
for i in df1.index:
    print(i)

#%%



