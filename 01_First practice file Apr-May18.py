# -*- coding: utf-8 -*-
"""
April/May 2018

@author: Santosh Karki

Start of learning Python

"""

#%%

print ("jan Feb Mar")

print ("jan\nFeb\nMar") # use /n for next line 

x = input ("Enter your name....")
print (x)

x = input ("Enter your name....")
print ("Hello", x, "How are you doing?")

y = input ("Enter your name....")
print ("Hello {}.... How are you doing man !!".format(y))

#%%


Hello = "Hellow World !!"

print (hello)

print ("hello my name is %s and my age is % and I live in %s" % ("Santosh", 40, "Delhi"))

"Hello World"
name = "santosh"

#Maths operation sequence:
#BODMAS : Brackets, Order (cube, square etc.), Division, MAS
#calling built-in modules of Python:
#use - import
#import random

#random.randint(a,b)
#random integer between number a and b
#random is module & randint is function

#rounding number
#round(2.1)
#round(1.5)

#For more complex maths function import math module

#import math
#math.floor(1.5)---- round down
#math.ceil(2.1)---- round up

import random
import math

health = 50

difficulty = 2

health_potion = int (random.randint (25, 50) / difficulty)

health = health + health_potion

print (health)

test1 = math.factorial (20)

print (test1)

round (2.1)

math.cos(0)

#%%
name = input ("whats ur name    ")
age = input ("whats ue age?    ")
City = input("where do u live    ")
Job = input ("what do u do    ")
string = "{} who is {} years old & stays in {} does almost {} everytime"
Output = string.format(name,age,City,Job)
print(Output)

#%% Data structures - Lists

x= "hello world"
print("x")
#just testing timepass


# Tuples are kind of read-only lists as they can not be changed once defined

mylist = [25, 30, 40, "santosh", [5,6,7,"karki"],45,"abc",45]
#create a list which is a type of Python data structure

print(mylist[0:2])
# to see 1st to 3rd index, use:  ) 

del mylist[1]
#delete by index number from a list

mylist.remove(40)
#remove a value from list

45 in mylist
#to find if a value is present in a list

mylist.append(50)
#to add a value in list

mylist + [112, 65]
#another way to append

remove = input ("would u want to get removed y/n?".strip().lower()
#take input from user & strip any spaces and make it lower case
        
>>> list_A = [23,43,56,72,54]
>>> list_A
[23, 43, 56, 72, 54]
>>> list_A = list_A + [5,6,7,8]
>>> list_A
[23, 43, 56, 72, 54, 5, 6, 7, 8]
>>> ist_A = list_A + [[5,6,7,8]]
>>> list_A = list_A + [[5,6,7,8]]
>>> list_A
[23, 43, 56, 72, 54, 5, 6, 7, 8, [5, 6, 7, 8]]
>>> list_A.append([1,2,3])
>>> list_A
[23, 43, 56, 72, 54, 5, 6, 7, 8, [5, 6, 7, 8], [1, 2, 3]]
>>> 

# Dictionary - similar to Lists. Have "keys" and associated "values"

test_dictionary = {}
                
#%% Security System App using Lists & if-else

print ("This is a security system programme written in Python")

GGN_SMT_WL2 = ["Santosh", "Puneet", "Kapil", "Hitesh", "Ashish", "Harsh"]

name = input ("Whats your First name?.... ").capitalize()

if name == "Harsh":
        print("Sorry bahi you are still interim but thats ok. You are SMT. Welcome")   
elif name in GGN_SMT_WL2:
    print("Welcome to Hell !!")
else:
    print("Sorry, you are not part of GGN SMT")
    add_new = input ("Do u want to be part of SMT? y/n?   ")
    if add_new == "y":
        warn_new = input ("Ek baar fir shooch lo... Do you really wanna join SMT? y/n?   ")
        if warn_new == "y":
            GGN_SMT_WL2.append(name)
            print ("you are added in GGN SMT. Yes its that simple !")
        elif warn_new == "n":
            print ("ok no problem. Thanks. You made great decision")
    elif add_new == "n":
              print ("ok no problem. Thanks. You made great decision")
              
          
# to see 1st to 3rd index, use:  print (GGN_SMT_WL2[0:2])          
# to delete last entry in list, use : del GGN_SMT_WL2 [-1]
#%% Dictionary
# Dictionary - similar to Lists. Have "keys" and associated "values" represented in Key:value format
# Keys and values are called as "items"

test_dictionary = {"santosh":40, "bob":35}
test_dictionary

# To make one key old multiple values/data use lists inside dictionary

test_dictionary2 = {"santosh":[40,"M","Delhi"], "Bob":[50,"M","London"]}

>>> test_dictionary2 ["santosh"]
[40, 'M', 'Delhi']

#%% for loops


# for loop works on any iterable data type or data which can be indexed
# i.e. which is made up of elements
# for loop looks at each element of the data one by one & operate on the
# data based on some logic / condition

for x in [1,2,3,4,5,6,7,8,9]:
	print (x)

print ("code-1 ends.....")	

# another way of doing the above

for x in range (1,10):
    print (x)

print ("code-2 ends.....")

# another way of doing the above with steps

for x in range (1,20,2):
    print (x)
    
print ("code-3 ends.....")

# Example code to find vowles and consonant in a text

vowels = 0
consonants = 0
for x in "Ye kya ho raha hai bhai. Starting from too early":
    if x in "aeiouAEIOU":
        vowels = vowels + 1
    elif x == "":
        pass
    else:
        consonants = consonants + 1

print ("There are {} vowels and...".format(vowels))
print ("there are {} consonants in the text".format(consonants))

# Other way to do is to use..... if x.lower() in "aeiou"....In this case we do not need capital letter AEIUO         
    
print ("code-4 ends.....")

#Ues of For loop with Dictionary

test_dictionary = {
    "GGN":["Santosh", "Hitesh", "Harsh", "Ashish"],
    "BLR":["Dinesh", "Nishant", "Satish"]
    }
for key in test_dictionary.keys():
    for x in test_dictionary[key]:
        if "a" in x:
            print (x)

print ("code-5 ends.....")
            
# with some mid way points in the above programe

#lets print all the names with letter "a" in them
for key in test_dictionary.keys():
    print (key)
# if you only wanna see the key names
    print (test_dictionary[key])
# if you wanna see the key values
    for x in test_dictionary[key]:
        if "a" in x:
            print (x)

print ("code-6 ends.....")
#%% List comprehensions
# List comprehensions : variables + for loop + if statement
# shortcut method to combine variables, for loops and if statements to
# create a list or comprehend a list in one line of code e.g. : below is the
# code to print all even numbers from 1 to 100

even_number = [x for x in range (1,101) if x % 2 == 0]
print (even_number)

print ("end of code-1")

#otherwise w/o list comprehensions, we would have to write big code to do same

# example for odd numbers:

odd_number = [x for x in range (1,101) if x % 2 != 0]
print (odd_number)

print ("end of code-2")

# List comprehensions are used to create Lists which u can then further use

# Another example (using strings this time):

words = ["what", "is", "going", "on", "in", "CDH", "ask", "Rajnish"]

answer = [[w.upper(), w.lower(), len(w)] for w in words]
print (answer)

# w is the variable here used to check each string of the list word
# it then creates another list using List comprehensions
# BTW, l is lenght of the string.

#%% Pig latin translator code

# get input sentence from user

original = input ("Please enter a sentence you wanna translate to pig latin:... ").lower().strip()

# split sentence into words

words = original.split()


#split function take a sentence string & break them in words and make a Python list of it

# loop thu words & convert to pig latin
# pig latin rules are = if word starts with vowel, just add "yay"
# if it starts with consonent, move 1st consonent cluster to the end and add "ay"

new_words_list = []

for word in words:

    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words_list.append(new_word)
    else:
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position+1
            else:
                break
        cons = word[:vowel_position]
        the_rest = word[vowel_position:]
        new_word = the_rest + cons + "ay"
        new_words_list.append(new_word)

print (new_words_list)
 
# stick words back together in a sentence and output the final string

finaloutput = " ".join(new_words_list)

print (finaloutput)
#%% Functions

# functions are kind of small modules that can be created once and then called
# up multiple times (reuse) in the code for further use.
# They need to be defined using "def" keyword.
# If they are supposed to give us something back, use "return" keyword.
# returing is not same as printing.
# return save the ans in a variable for further use. Print does not. It just shows ans on the screen

def add(x,y):
    return x+y

answer = add(345,765)
print (answer)

print ("end of code-1...")

#or we can do it this way:

print (add(345,765))

print ("end of code-2...")


# in built Python function to write reverse string/word

word = "Santosh"
word [::-1]
print (word [::-1])


print ("end of code-3...")

# lets build a function (code) for reversing the text 


def reverse(userinput):
    return userinput[::-1]
userinput = input("Please enter a text you wanna reverse....").strip()
print (reverse(userinput))

print ("end of code-4...")


#%% variable scope 

# Variable Scope: 2 types: one big Global scope and multiple little Local scope
# if variable is in global scope, it can be seen anywhere in the entire code/programme
# if variable is in local scope, its limited to only that part of the code
# Functions always create local scopes.
# Loops and if create global scope variables

a = 100
def fun1():
    print(a)
def fun2():
    print(a)
fun1()
fun2()

print ("end of code-1...")

# "a" variablle is global variable in code-1 thus used by whole code (all functions)

def fun1():
    b = 200
    print(b)
def fun2():
    print(b)
fun1()
fun2()

print ("end of code-2...")

# "b" variablle is local scope variable in code-2 thus used by only fun1 where its defined
# so we get an error for fun2 as its in fun1's local scope only

c = 250
def fun1():
    c=50
    print(c)
def fun2():
    c=100
    print(c)
fun1()
fun2()
print (c)

print ("end of code-3...")

#%%
# Variable Scope: 2 types: one big Global scope and multiple little Local scope
# if variable is in global scope, it can be seen anywhere in the entire code/programme
# if variable is in local scope, its limited to only that part of the code
# Functions always create local scopes.
# Loops and if create global scope variables

c = 250
def fun1():
    c=50
    print(c)
def fun2():
    c=100
    print(c)
fun1()
fun2()
print (c)

print ("end of code-1...")

# by default Local overrides global within function but global remains same
# bcoz Python by default will protech global varible
# if we wanna override global by local this is how we do:


d = 250
def fun1():
    global d
    d=50
    print(d)
def fun2():
    d=100
    print(d)
fun1()
fun2()
print (d)

print ("end of code-2...")

# Here fun1 variable overwrites global value (from 250 to 50)


# same is tru with other data type variables e.g. for lists:

c = [1,2,3]
def fun1():
    c=50
    print(c)
def fun2():
    c=100
    print(c)
fun1()
fun2()
print (c)

print ("end of code-3...")

#slight exception to the override rule is in lists
# w/o using global keyword, we can override some element in global list variable
# same applies for dictionary (w/o using global keyword, we can override...)

c = [1,2,3]
def fun1():
    c[0]=5
    print(c)
def fun2():
    c=100
    print(c)
fun1()
fun2()
print (c)

print ("end of code-4...")
#%% Functions, parameters n arguments

# Functions, positional arguments, Keyword Arguments, Default Parameters
# Parameters are used when we define a Function and
# Arguments are used when we call a function


def about(name, age, likes):
    sentence = "Meet {} !! He is {} years old and likes {}".format(name,age,likes)
    return sentence


print (about ("santosh", 40, "football"))

print ("end of code-1....")




# In the code above, for function about :    
# name, age, likes are Parameters
# "santosh", 40, "football" are Arguments
# So parameters are kind of variables in a function which we define
# and arguments are data for those variables which we provide to the function


# By default parameters & arguments follow the same order and map 1:1
# however we can alter the order by using Keyword Arguments

print (about (age = 40, name = "santosh", likes = "football"))

print ("end of code-2....")


# is called as keyword argument as each argument is assiciated with a keyword (parameter)
# code-1 and 2 will give same output though the order of arguments is different
# as in code-2, we are using "keyword arguments"
# code-1 uses "positional arguments"

# we can also use default value to any parameter so that if thats not entered
# by the user, code will use the default.



def about1(name, age, likes = "cricket"):
    sentence = "Meet {} !! He is {} years old and likes {}".format(name,age,likes)
    return sentence


print (about1 ("santosh", 40,))

print ("end of code-3....")

# if given explicit value/argument, it will override the default

def about1(name, age, likes = "cricket"):
    sentence = "Meet {} !! He is {} years old and likes {}".format(name,age,likes)
    return sentence


print (about1 ("santosh", 40, likes = "football"))

print ("end of code-4....")

def about1(name, age, likes = "cricket"):
    sentence = "Meet {} !! He is {} years old and likes {}".format(name,age,likes)
    return sentence


print (about1 ("santosh", 40, "football"))

print ("end of code-5....")


# One rule however with default is that it must go at the end
# parameters with default value have to go last
# so can't do this : about1(name = "Bob", age, likes)
# will have to instead do : about1(age, likes, name = "Bob")
# can have as much defaults as we want - but at the end


def about1(name = "Rajnish", age = 40, likes = "girls"):
    sentence = "Meet {} !! He is {} years old and likes {}".format(name,age,likes)
    return sentence


print (about1 ())

print ("end of code-6....")
#%%
# Packing & Unpacking variables. Tricks to work with functions.
# Packing & unpacking arguments & keywork arguments.

print (1,2,3,4,5)

print ("end of code-1....")

# 1,2,3,4 & 5 are arguments

numbers = [1,2,3,4,5]
print (numbers)

print ("end of code-2....")

# Here the argument is a list with numbers from 1 to 5
# So "print" will print the list as such 

print(*numbers)

print ("end of code-3....")

# the above will print individual elements/variables/arguments of the list or
# it wiill unpack the arguments. So * will convert one single list argument to
# its mini-arguments of individual numbers
# So we can unpack any "iterable" data type before they go into functions

print ("abcd")

print ("end of code-4....")

# will give abcd as output but

print (*"abcd")

print ("end of code-5....")

# will give a b c d as output which is same as:

print ("a","b","c","d")

print ("end of code-6....")

# bcoz strings like lists are also iterable data type

# lets see its use in functions

def add(x,y):
    return x + y

print(add (10,30))

print ("end of code-7....")


def add (*numbers):
    total = 0
    for x in numbers:
        total = total + x
    return (total)

print(add(5,6,4,3,45,65,87,30,3,4))

print ("end of code-8....")

# Here we used Tuple to give us a lot of flexibility
# use when u do not know how many arguments we may have to work on


# Now lets use packing & unpacking with keyword arguments
# Use dictonary for this as it has two values: keyword & argument


def about (name, age, likes):
    sentence = "Meet {}. He is {} years old & likes {}".format (name, age,likes)
    return sentence

dictionary = {"name":"Santosh", "age":40, "likes":"Python"}

print(about(**dictionary))

print ("end of code-9....")

# one star (*) for normal/positional arguments & two stars (**) for keyword arguments)

# can use any order e.g.

def about (name, age, likes):
    sentence = "Meet {}. He is {} years old & likes {}".format (name, age,likes)
    return sentence

dictionary = {"age":40,"name":"Santosh","likes":"Python"}

print(about(**dictionary))

print ("end of code-10....")

# w/o dictionary, its same as :


def about (name, age, likes):
    sentence = "Meet {}. He is {} years old & likes {}".format (name, age,likes)
    return sentence

print(about (name = "Santosh", age = 40, likes = "Python"))

print ("end of code-11....")

# So this was unpacking data from dictionary. Lets see packing data
# in a dictionary

def test(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key,value))

print (test(Santosh = "CDH", Adam = "IP&D", Puneet = "CDH"))

# it creates a dictionary named test & packs the data in it nicely
# kwarg is naming convention inn Python for Keyword Arguments
# for normal areguments its args and written as (*args)
#%% OOP Class

# Object-oriented programming (OOP) is a programming language model
# organized around objects rather than "actions" and data rather than logic. 

# "Class" is the template to make objects.
# Each class has some properties called as "states"
# Changing states is donme using "methods" or logic or using function

# Class name in Python convention start with uppercase letter
# class name is the followe by a colon :

class Pound:
    value = 1.00
    colour = "glod"
    num_edges = 1
    diameter = 22
    thickness = 3
    heads = True

# so "Pound" is a class with following states

# lets make pbject from this class.

coin1 = Pound()

print (type(coin1))

# its class type will appear as - <class '__main__.Pound'>

# so object "coin1" is created using class Pound

# to see objects state values

print(coin1.colour)
print(coin1.diameter)

# to change state :

coin1.colour = "Greenish"

print(coin1.colour)

coin2 = Pound()

print(coin1.colour)
print(coin2.colour)

# Though created from same class objects can behave independently & different from each other
# if we want objects to change states on their own, we use class methods

class Pound:
    value = 1.00
    colour = "glod"
    num_edges = 1
    diameter = 22
    thickness = 3
    heads = True

# constructure
#%% Check IP for subnet

IPAdress1 = input("Please enter a dotted quad notation IP address: ")
IPAdress2 = input("Please enter another: ")
SubnetMask = input("Please enter the subnet mask: ")

binaryIP1 = [bin(int(IPAdress1))[2:].rjust(8,'0') for IPAdress1 in IPAdress1.split('.')]
IP1 = ''.join(binaryIP1)

binaryIP2 = [bin(int(IPAdress2))[2:].rjust(8,'0') for IPAdress2 in IPAdress2.split('.')]
IP2 = ''.join(binaryIP2)

binarysub = [bin(int(SubnetMask))[2:].rjust(8,'0') for SubnetMask in SubnetMask.split('.')]
sub = ''.join(binarysub)
i=0
j=0

for (i,j) in zip(binaryIP1,binaryIP2):
    if i == j:
        print("Same Network" )
    else:
        print("Different networks")
#%% Even odd number

print ("Code to find out whether a number is even or odd")
print ("")
x = input ("Please enter the number....")
if int(x) % 2 == 0:
    print ("This is even number")
else:
    print ("This is odd number")
  
print ("End of even-odd code")
#%% Prime number

print ("Code to find if a number is prime number")

x = input ("Please enter the number you want to check if its prime or not...")

s = 0

for y in range (1, int(x)):
    if int(x) % int(y) == 0:
        s = s+1
    if s == 2:
            print ("its a PRIME number")
    else:
        print ("it's NOT a PRIME number")

print ("End of code")


#%% Functions

def sumof(a, b, c):
    addition = a + b + c
    return addition

def averageof(x, y, z):
    average = sumof(x, y, z) / 3
    return average

print (averageof(34, 87, 98))


print ('\n')


# These are all void functions i.e. they dont return any value as such. Just return "None"

def quote():
    print("What is this")
quote()


def quote1():
    print("What is this")
    return      # No impact of return w/o any variable.
quote1()

def quote2(name):
    print("What is this ", name )
quote2('Harsh')

def quote3(name):
    print("What is this ", name )
    return      # No impact of return w/o any variable.
quote3('Harsh')




####
#Code-1

def temp_conv(temp_c):    
    temp_f = (temp_c*9) / 5 + 32    
    return temp_f

print(temp_conv(30))

print ('\n')

###
#Code-2

def temp_conv(temp_c):    
    temp_f = (temp_c*9) / 5 + 32    
    return temp_f

x = temp_conv(35)
print(x)
print('temp_f value is returned by the function & then assigned to variable x in Code-2.')

print ('\n')

###
#Code-3

def temp_conv(temp_c):    
    temp_f = (temp_c*9) / 5 + 32    
    
x = temp_conv(35)
print(x)
print('Without return statement as in Code-3, value "None" is returned.')

print ('\n')

###  
#Code-4

def temp_conv():
    temp_c = int(input('Enter the temperature in Celsius...'))
    temp_f = (temp_c*9) / 5 + 32
    return temp_f

x = temp_conv() # Function does not need parameter here bcoz it uses 'input' method in the body of function

print(x)

if x > 0:
    print ('Function output used in expression')

print ('\n')

###
#Code-5

def greet():
    print('Hi There !')

greet()     # Will print 'Hi There !' bcoz of function greet execution
a = greet() # Will print 'Hi There !' for this line as well...bcoz of function greet execution
print(a)    # Will print 'None' as there is no return statement

print ('\n')

###
#Code-6

def greet():
    return ('Hi There !')

a = greet() # Will print nothing as function body has no print statement. It will just assign string 'Hi There !' to variable a
print(a)    # Will print 'Hi There !' as thats what is now stored inside a by previous line statement
print(greet())

#%%   loops 




#Function to write Fibonacchi Series. Sum of two numbers is next in series

def Fibseries():
    first = 0
    second = 1
    N = int(input('Enter the number upto which you want the series'))
    print (first)
    print (second)
    for i in range (N+1):
        third = first + second
        print (third)
        first, second = second, third
        
Fibseries()        


print('\n') 

### Number guess game

import random
x = random.randint(1, 100)
print (x) #not required as such. Just for Fun !
guessnum = int (input('Enter any num from 1 to 100'))
while guessnum != x:
    if guessnum > x:
        print ('Your guess number is too high')
    else:
        print ('Your guess number is too low')
    guessnum = int (input('Enter any num from 1 to 100'))
print ('You win. You guessed correct')


print('\n')

### sum of all odd numbers upto user input number N, code-1

oddnumsum = 0
i = 1
N = int (input ('Enter the number'))

while i <= N :
    oddnumsum = oddnumsum + i
    i = i+2
print (oddnumsum)
    
print('\n')

### sum of all odd numbers upto user input number N, code-2

oddnumsum = 0
N = int (input ('Enter the number'))
for i in range (1, N+1, 2):
    oddnumsum = oddnumsum + i

print (oddnumsum)

print('\n')

### sum of all odd numbers upto user input number N, code-3

oddnumsum = 0
N = int (input ('Enter the number'))

for i in range(1, N+1):
    if i % 2 != 0 :
        oddnumsum = oddnumsum + i
        print ('sum is ', oddnumsum, 'when odd number is ', i)
print('Final answer is ..', oddnumsum)

print('\n')


### sum of all odd numbers upto user input number N, code-4

oddnumsum = 0
i = 1
N = int (input ('Enter the number'))
while i <= N :
    if i % 2 != 0 :
        oddnumsum = oddnumsum + i
    i = i + 1
print (oddnumsum)

print('\n') 

### sum of all odd numbers upto user input number N, code-5

def oddnumsum():
    oddnumsum = 0
    i = 1
    N = int (input ('Enter the number'))
    while i <= N :
        oddnumsum = oddnumsum + i
        i = i+2
    print (oddnumsum)
oddnumsum()
    
print('\n') 
               

###

percentage = int(input('Whats your number % ?..' ))

if 100 >= percentage >= 90 :
    print ('Your Grage is A+')

elif 90 > percentage >= 80 :
    print('Your grade is A')

else:
    print ('You fail')


### Print Hello 'name' (name is variable input by user) until there is some input. For no input, come out of loop


while True:
    name = input('Whats your name')
    if name == '':
        break
    else:
        print ('Hello ', name )

print ('Testing this file.... Just ignore this message')

def Areaofsquare (side):
    """This function takes one variable i.e the side of the square & provides its area as output. Can be seen from console using print (Areaofsquare.__doc__)"""
    Area = side**2
    print ("Area of your Square is", Area)
   
    
def testfunction(name):
    print ("Hello my name is " + name + " & I m testing Python function")
    

def testfunctionscope(x):
    """ To test scope of variable"""
    x = 2222
    print ("value of x inside function is ", x)

x = 23
print (testfunctionscope(x))

x = 55
print ('value of x is now overridden by value outside function to ', x)
        

#%%

        
        






    





        
    

#%%









    

       

















    







                




              
    
        
    













                









