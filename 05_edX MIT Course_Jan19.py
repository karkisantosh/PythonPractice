# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 17:08:22 2018

@author: Santosh Karki
edX Online MIT course
Introduction to Computer Science and Programming Using Python

"""

#%% Santosh Karki 29Dec18....
# Faking tic-tac-toe grapics

def drawboard():
    n = int(input("Please enter size of the board "))
    for i in range (3):
        print(" ---" * n) #space then ---
        print("|   " * (n+1) )#| then three space
    print(" ---" * n)# for the last/additional line

#%% Santosh Karki 29Dec18....
def tic():

    GL = [[1,2,0],
          [2,2,2],
          [2,1,1]]
    blank = 0
    player1 = 1
    player2 = 2
    for entry in GL:
        if entry[0] == entry[1] == entry[2] == 1:
            print("Player1 wins")
        elif entry[0] == entry[1] == entry[2] == 2:
            print("Player2 wins")
    for i in range (3):
        if GL[0][i] == GL[1][i] == GL[2][i] == 1:
            print("Player1 wins")
        if GL[0][i] == GL[1][i] == GL[2][i] == 2:
            print("Player2 wins")            
      
            
#        for entry1 in entry:
#           print (entry1)


#%% Santosh Karki 29Dec18....
# cube root of a number.... by guess n check         
def cuberoot():
    x = int(input("Enter the Integer "))
    ans = 0
    while ans**3 < x :
        ans = ans + 1
    if ans ** 3 == x:
        print ("Cube root of", x, "is", ans)
    else:
        print (x, "is not a perfect cube")
          
            
#%% Santosh Karki 29Dec18....
# cube root of a number.... by guess n check
def cuberoot2():
    x = int(input("Enter the Integer "))
    for ans in range (x+1):
        if ans**3 == x:
            print("Cube root of", x, "is", ans)
        else:
            print (x, "is not a perfect cube")
            break
#%%
def cubert(n):
    ans = 0
    epsilon = 0.01
    increment = 0.0001
    numofguess = 0
    while ans**3 - n <= epsilon and ans <= n:
        ans += increment
        numofguess += 1
    print("Cube root of {} is {} and it took {} guesses".format(n,ans,numofguess ))
  
#%% Santosh Karki 01Jan19....  
# Square root of a number.... by guess n check. Bisect method
def sqrt(x):
    epsilon = .001
    low = 0.0
    high = x
    ans = (low + high) / 2.0
    num_guess = 0
    
    while abs(ans**2 - x) >= epsilon:
        num_guess = num_guess + 1
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    print ("Square root of", x, "is", ans,)
    print ("It took", num_guess, "gusses")
  
#%% Santosh Karki 01Jan19....  
# Cube root of a number.... by guess n check. Bisect method
def cube3(x):
    epsilon = .001
    low = 0.0
    high = x
    ans = (low + high) / 2.0
    num_guess = 0
    
    while abs(ans**3 - x) >= epsilon:
        num_guess = num_guess + 1
        if ans ** 3 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    print ("Cube root of", x, "is", ans,)
    print ("It took", num_guess, "gusses")
  
#%% Santosh Karki 02Jan19....
# Practicing Python class creation

class myclass():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def sqra(self):
        self.a = self.a ** 2
        print(self.a)
print()
x1 = myclass(1, 2, 3)
print (x1)
print (x1.a)        



#%% Santosh Karki 03Jan19....
# Practicing Python class creation
    
class coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        xaxis = (other.x - self.x) ** 2
        yaxis = (other.y - self.y) ** 2
        dis = (xaxis + yaxis) ** 0.5
        return dis
    def __str__ (self):
        return "("+str(self.x)+","+str(self.y)+")"
         
#%% Santosh Karki 03Jan19.... 
# Practicing Python class creation
        
class fraction():
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer)+"/"+str(self.denom)
    def getnumer(self):
        return self.numer
    def getdenom(self):
        return self.denom
    def convert2float(self):
        return self.numer/self.denom
    
    def __add__(self, other):
        newnumer = (self.getnumer()*other.getdenom()) + (other.getnumer()*self.getdenom())
        newdenom = self.getdenom()*other.getdenom()
        return fraction(newnumer, newdenom)
# with __add__ we can use + between objects to get addition
# with normal function like addition, we need to use dot notation to involve function
    def addition(self, other):
        newnumer = (self.numer*other.denom + other.numer*self.denom)
        newdenom = self.denom*other.denom
        return fraction(newnumer, newdenom)    
 

#%% Santosh Karki 04Jan19....
# Practicing Python class creation
class integerset(object):
    def __init__(self):
        self.L1 = []
    def insert (self, e):
        if not e in self.L1:
            self.L1.append(e)
        else:
            print("element alreay in the IntergerSet")
    def fetch (self, e):
        return e in self.L1
    def __str__ (self):
        return str(self.L1)


#%% Santosh Karki 04Jan19....
# Practicing Python class creation 
class testclass():
    def __init__(self, n, a, c, d = 3.14):
        self.name = n
        self.age = a
        self.city = c
        self.country = "India"
        self.d = d
# getter functions/methods    
    def get_n(self):
        return self.name
    def get_a(self):
        return self.age
    def get_c(self):
        return self.city
    def get_nation(self):
        return self.country
    def get_d(self):
        return self.d
# setter functions/methods    
    def set_n(self, new_n):
        self.name = new_n
    def set_a(self, new_a):
        self.age = new_a
        
    def agediff(self, other):
        return other.age - self.age
# In the above function, other is taken as instance of class testclass    
    def agediff2(self, other):
        return other - self.age 
# In the above function, other is taken as integer
#%% 
class BTemployee():
    def __init__ (self, name, ein, loc, role):
        self.name = name
        self.ein = ein
        self.location = loc
        self.rolecode = role

    def getname(self):
        return self.name
    def getein(self):
        return self.ein
    def getloc(self):
        return self.location
    def getrole(self):
        return self.rolecode
    def setein(self, newein):
        self.ein = newein 
        
    def __str__ (self):
        print ("BT Employee with name ein location & role :")
        print (str(self.name), str(self.ein), str(self.location), "& STST0" + str(self.rolecode))
    

#class BTIndia(BTemployee):
#    def __init__ (self, city):
#        self.city = city
#        BTemployee.__init__(self, name, ein, loc, role)
#    
#    def subband(self):
#        return self.rolecode > 4
#    
#    def __str__ (self):
#        print ("BT India Employee with Name EIN Location & Rolecode :")
#        print (self.name, str(self.ein), self.location, "& STST" + str(self.rolecode))


#Satish = BTIndia("Satish", 45678, "BLR", 5)        
#Harsh = BTIndia("Harsh", 12345, "GGM", 3)
Tim = BTemployee("Tim", 998877, "UK", 4)
John = BTemployee("John", 998877, "UK", 2)

        
#%% Santosh Karki 06Jan19....
# Practicing Python class creation 

class L1class(object):
    
    name = "This is superclass or parent class" # 'name' is class varibale
    __key = 34 # key is private class variable. 
    # all variables defined below are instance variables e.g. a, b, c, aa,bb etc. 
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.aa = 3.14
        self.__bb = 6.5 # private attribute (starts with __)
        #private attribute is not inherited in subclass
        print("A new instance of L1class is created !")
    
    def fun1(self):
        print(self.a ** 2)
        
    def fun2(self):
        print (self.b **3)
        
    def funduplicate(self):
        print("This is function from L1class")
    
    def __str__ (self):
        return "L1class Object with "+"a="+str(self.a)+" b="+str(self.b)+" c="+str(self.c)
        
class L2class(L1class):
    
    name = "This is sub-class"
    
    def __init__ (self, a, b, c, d):
        L1class.__init__(self, a, b, c)
        self.d = d
        self.dd = 5
        print("A new instance of L2class is created !")
    
    def fun3(self):
        print (self.c * 10)

    def funduplicate(self):
        print("This is function from L2class")

    def __str__ (self):
        return "L2class Object with "+"d="+str(self.d)+" ....& inherited L1class attributes, a="+str(self.a)+" b="+str(self.b)+" c="+str(self.c)
    
#%% Santosh Karki 07Jan19....
mystring = """ Pep Guardiola says the Manchester City fans played a key role in the Premier League win over Liverpool at the Etihad Stadium, and called upon them to make the difference in the Champions League.
City beat Liverpool to move within four points of the Reds in the league, and the home fans played a pivotal role in the important victory.
The sell-out crowd cheered every tackle and pass from City, who were more pragmatic in their performance than previous Premier League games.
And Guardiola said the fans gave his players an extra boost as they adapted to a more intense style of play after a hectic run of fixtures.
"Winning is so addictive," he said. "When you taste it, you want more. We spoke about that. For us it was a final. Losing today we would have been almost out. We played the game making mistakes but that is not important.
Given the change in tactics from Guardiola, the manager said the fans played an important role.
He continued: "Today the stadium was sold out, the people were closer to us than I have ever seen before in my two and a half season here. We knew that but the opponent we faced today demand this kind of game.
"Sometimes it is not necessary to fight in that way or win that way. You can play easier and win the games more easily but every single ball, backwards and action is not enough because the level is so high."
Read More
Pep Guardiola hails Man City striker Sergio Aguero for impact in 'lucky' win over Liverpool FC
Guardiola likened the game to the quality of the Champions League, saying the same atmosphere and attitude from players and fans will be needed if City are to progress further in the competition.
 """
 
mylist = []
for word in mystring.split():
    mylist.append(word)
    
mydict = {}

for word in mylist:
    mydict[word] = mydict.get(word,0) + 1

mrw = None

for k, v in mydict.items():
    if mrw == None:
        mrw = v
    if v > mrw:
        mrw = v
        word = k
print ("Most repeated word is: ", word, "repeated", mrw, "times")

#%% Santosh Karki 08Jan19....       

import turtle
san = turtle.Turtle()
san.color('red')
san.shape('turtle')
san.pensize(5)

for i in range (10):
    san.forward(100)
    san.left(90)
    san.forward(100)
    san.right(90)
    san.forward(100)


turtle.done()
   
#%% ??????

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')

# Ans: 10, 9, 8, 7, Breaking out of loop, Outside of loop

num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 

# infinite loop

#%% Santosh Karki 09Jan19....
# square of a num by repetitive addition
def abc(n):
    counter = 1
    nsqr = n
    while counter < n:
        nsqr += n
        counter += 1
    print("Square of {} is {}".format(n, nsqr))
    
def abc2(n):
    counter = n
    nsqr = 0
    while counter != 0:
        nsqr += n
        counter -= 1
    print("Square of {} is {}".format(n, nsqr))

#%% Santosh Karki 10Jan19.... 
# for loop inside of while loop
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    
    
#%% Santosh Karki 10Jan19.... 
# while loop inside of for loop
count = 0
for iteration in range (5):
    while iteration < 5:
        count += len('hello, world')
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break
    
#%% Santosh Karki 10Jan19.... 
# while loop inside of for loop. ... without using break       
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))

#%% Santosh Karki 10Jan19....   
# while loop inside of for loop. ... another way   
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))    
    
    
#%% Santosh Karki 10Jan19....  
# while loop inside of for loop. ... another way w/o using break or while
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    
    
#%% Santosh Karki 10Jan19....   
s = 'azcbobobegghakl'
count = 0
for i in range (len(s)):
    if s[i] == "b":
        index = i
        if s[i+1:i+3] =="ob":
            count += 1        
print ("Number of times bob occurs is:",count)
    
#%% Santosh Karki 10Jan19....   
s = 'azcbobobegghakl'
count = 0
for i in range (len(s)):
    if s[i:i+3] == "bob":
        count += 1        
print ("Number of times bob occurs is:",count)
 
#%% Santosh Karki 10Jan19.... 
s = 'azcbobobegghakl'
tempmax=0 
lr=0 
ur=0 
for i in range(len(s)-2): 
    max1=0
    j=i 
    k=i
    while(j < len(s)-1):
        if s[j] > s[j+1]:
            break
        else: 
            max1=max1+1
            k=j+1 
            j=j+1
            if(max1 > tempmax):
                tempmax = max1
                lr = i
                ur = k 
print ("Longest substring in alphabetical order is:",s[lr:ur+1])

#%% Santosh Karki 10Jan19.... 

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

#%% Santosh Karki 11Jan19.... 
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while guess**2 <=x :
    if abs(guess**2 -x) >= epsilon:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
 
#%% Santosh Karki 11Jan19....     
  
    
    
#%%




#%%    
    
    
    
    
    
    
    
    
    