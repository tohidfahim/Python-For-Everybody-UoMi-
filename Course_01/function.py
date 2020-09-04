# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 13:09:49 2020

@author: Tohid Fahim
"""

m = max("tohid")
print(m)



def add(a, b):
    c = a+b
    return c



sum = add(2, 4)
print(sum)



#Assignment

def computepay(h,r) :
    if h <= 40 :
        return (h*r)
    elif h > 40 :
        return ((40*r)+((h-40)*r*1.5))

hrs = input("Enter Hours:")
hrs = float(hrs)
rph = input("Rate Per Hour:")
rph = float(rph)


p = computepay(hrs, rph)
print("Pay",p)