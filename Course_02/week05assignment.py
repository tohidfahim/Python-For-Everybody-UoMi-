# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:30:26 2020

@author: Tohid Fahim
"""

file_input = input('Enter file Name : ')
file_open = open(file_input)

email = list()
count = dict()

for line in file_open:
    if not line.startswith('From '):
        continue
    stre = line.split()
    email.append(stre[1])
  
#dictionary
for name in email:
    if name not in count:
        count[name] = 1
    else :
        count[name] = count[name] + 1
#print(count)
    
maxi = 0

for key,val in count.items():
    if val > maxi:
        mail = key
        maxi = val
print(mail, maxi)
        
    