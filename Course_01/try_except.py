# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:20:17 2020

@author: Tohid Fahim
"""

a = 5

try:
    print("HUH")
    a = a/0
except:
    a = -1

print(a)