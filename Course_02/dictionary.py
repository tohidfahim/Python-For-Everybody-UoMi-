# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:59:23 2020

@author: Tohid Fahim
"""

purse = dict()
purse['money'] = 150
purse['mobile'] = 'samsung'
purse['tissue'] = 175

print(purse)
print(purse['mobile'])

purse['mobile'] = 'one-plus'
print(purse)

purse['money'] = purse['money'] + 50
print(purse)

#....................................................

counts = dict()
names = ['A', 'C', 'R', 'A', 'A', 'V', 'C', 'W']

for name in names:
    if name not in counts:
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1

print(counts)