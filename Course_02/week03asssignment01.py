# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 09:02:33 2020

@author: Tohid Fahim
"""

# Use words.txt as the file name
fh = input('Enter File Name: ')
fh1= open(fh)
for line in fh1:
    line = line.rstrip()
    print(line.upper())
