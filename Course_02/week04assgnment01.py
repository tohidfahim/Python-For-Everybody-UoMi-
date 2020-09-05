# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:50:47 2020

@author: Tohid Fahim
"""

fh = "But soft what light through yonder window breaks It is the east and Juliet is the sun Arise fair sun and kill the envious moon Who is already sick and pale with grief"
lst = fh.split()
print(lst)
new_list = list()

for line in lst:
    #print(line)
    if line in new_list:
        continue
    new_list.append(line)
new_list.sort()
print(new_list)