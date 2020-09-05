# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:12:37 2020

@author: Tohid Fahim
"""

dict_name = {'money': 150, 'mobile': 'one-plus', 'tissue': 175}

print(dict_name.keys())
print(dict_name.values())
print(dict_name.items())

#two ieration variables
for id,val in dict_name.items():
    print(id, val)