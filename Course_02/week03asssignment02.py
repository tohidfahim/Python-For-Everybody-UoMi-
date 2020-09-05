# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:07:57 2020

@author: Tohid Fahim
"""

file_name = input("Enter File Name : ")
file = open(file_name)
counter = 0
sval = 0

for line in file:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    counter = counter + 1
    #print(line)
    ind = line.find(':')
    val = float(line[ind+1:])
    sval = sumval + val 
    
print('Average spam confidence:', sval/counter)