# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 19:10:40 2020

@author: Tohid Fahim
"""

file_input = input('Enter file Name : ')
file_open = open(file_input)

counter = 0

for line in file_open:
    if not line.startswith('From '):
        continue
    stre = line.split()
    email = stre[1]
    print(email)
    counter = counter + 1
    
print("There were", counter, "lines in the file with From as the first word")