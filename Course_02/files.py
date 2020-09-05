# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 15:14:08 2020

@author: Tohid Fahim
"""

fhand = open('file.txt', 'r')
print(fhand)

for i in fhand:
    print(i)
    
    
fnew = open('tohid.txt')
inp = fnew.read()
print(inp)

print('........................SKIPPING..............................')
fname = open('fahim.txt', 'r')
for line in fname:
    line = line.strip()
    if line.startswith('aa'):
        continue
    print(line)