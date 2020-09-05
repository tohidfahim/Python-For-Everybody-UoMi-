# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:53:36 2020

@author: Tohid Fahim
"""

a = ['tohid', 143107, '01689512987', 3.46]
print(a)
print(type(a))

for i in a:
    print(i)
    
print(a[2])

#mutable
a[1] = 107
print(a)


aa = "asdasdas"
print("String Length: ", len(aa))
print("List Length: ", len(a))


x = [1, 2, 3]
y = [4, 5, 6]
c = x+y
print(c)
print(c[1:3])
print(c[:])
print(c[:4])

c.append(77)
print(c)
print(2 in c)

c.append(15)
print(c)
c.sort()
print(c)