# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 10:55:59 2020

@author: Tohid Fahim
"""

hrs = input("Enter Hours:")
h = float(hrs)

rph = input("Rate Per Hour:")
r = float(rph)

if h <= 40 :
    print(h*r)
elif h > 40 :
    print((40*r)+((h-40)*r*1.5))