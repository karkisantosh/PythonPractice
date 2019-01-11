# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 20:32:31 2018

@author: 607495308
"""

#%%
# Excercise on Python dictionaries
# https://www.w3resource.com/python-exercises/dictionary/

#%%    ....Santosh Karki......23 Sep 2018 
#Concatenate dict
    
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60} 
dic4 = {}
L1 = []
def concatdict():
    for item in dic1.items():
        L1.append(item)
    for item in dic2.items():
        L1.append(item)    
    for item in dic3.items():
        L1.append(item)
    for item in L1:
        dic4.update({item[0]:item[1]})
    print(dic4)

#%%    ....Santosh Karki......23 Sep 2018 
#Concatenate dict... same as above but small code
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60} 
dic4 = {}
def concatdict2():
    for item in (dic1, dic2, dic3): #make a tuple with each item being dic
        dic4.update(item)
    print(dic4)
#%%    ....Santosh Karki......23 Sep 2018 
def sqrdic(n):
    dictout = {}
    for i in range(1,n+1):
        dictout[i] = i**2
    print(dictout)
#%%    ....Santosh Karki......23 Sep 2018   
def mergedict(d1, d2):
    d3 = {}
    for item in (d1, d2):
        d3.update(item)
    print(d3)
#%%    ....Santosh Karki......23 Sep 2018   
# Same as above but using copy() function
def mergedict2(d1, d2):
    d3 = d1.copy()
    d3.update(d2)
    print(d3)    
#%%    ....Santosh Karki......23 Sep 2018   
def dictitems(d1):
    x = sum(d1.values())
    print('Sum of all values in this dict is: ', x)
    product = 1
    for value in d1.values():
        product = product * value
    print('Product of all values in this dict is: ', product)
    
#%%    ....Santosh Karki......26 Sep 2018   
# two ways to inject variable in string
x = 'Santosh'    
print ("Number of lines is {}".format(len(x)))
print('..........')
print ("Number of lines is %s" %len(x))


#%%    ....Santosh Karki......28 Sep 2018   
def maplists():
    L1 = [1,2,3,4,5]
    L2 = ['a', 'b', 'c', 'd', 'e']
    newdict = dict(zip(L1, L2))
    print(newdict) 
    
#%%    ....Santosh Karki......28 Sep 2018  
def sortbykey():
    D1 = {'sa':23, 'na':33, 're':44, 'za':11}
    for key in sorted(D1):
        print('{}:{}'.format(key, D1[key]))

#%%    ....Santosh Karki......01 Oct 2018  
#Q15
def minnmax():
    D1 = {'sa':23, 'na':33, 're':44, 'za':11}
    maxv = None
    for v in D1.values():
        if maxv == None or v > maxv :
            maxv = v
    print(maxv)

#%%    ....Santosh Karki......01 Oct 2018 
#Q17
inputdict = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}
    
def removeduplicates():
    outputdict = {}
    for k, v in inputdict.items():
        if v not in outputdict.values():
            outputdict[k] = v
    print(outputdict)
#%%    ....Santosh Karki......01 Oct 2018  
#Same as above but with simple dict
ind = {1:'cat', 2:'rat', 3:'mat', 4:'bat', 5:'rat', 6:'cat', 7:'snake'}    
def removeduplicates():
    outd = {}
    for key, value in ind.items():
        if value not in outd.values():
            outd[key] = value
    print(outd)  
#%%    ....Santosh Karki......01 Oct 2018 
#Q19
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
def addv():
    d3 ={}
    for k1, v1 in d1.items():
        for k2, v2 in d2.items():
            if k1 == k2:
                d3[k1] = v1 + v2
            if k1 not in d3:
                d3[k1] = v1
            if k2 not in d3:
                d3[k2] = v2
    print(d3)

#%%    ....Santosh Karki......01 Oct 2018 
#Q22
d1 = {'sa':23, 'na':33, 're':44, 'za':11, 'fd':34, 're':56,'ww':76, 'oo':4}
def top3values():
    L1 = []
    for v in d1.values():
        L1.append(v)
    L1.sort(reverse = True)
    print(L1[0], L1[1], L1[2])
    
#%%    ....Santosh Karki......01 Dec 2018 

import pprint as pp
import json

myjsonfile = open("test.json").read()
print(myjsonfile)
print("************")
jsonpy = json.loads(myjsonfile)
print(jsonpy)
for k,v in jsonpy.items():
    print(k)
    print("$$$$$$$$")
    print(v)
    
#%%

   
    


#%%



    
    