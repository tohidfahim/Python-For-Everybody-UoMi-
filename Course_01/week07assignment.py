# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 17:20:02 2020

@author: Tohid Fahim
"""

largest = -1
smallest = 100

while True:
    val = input("Enter a Number: ")
    if val == "done":
        break
    try :
        val = int(val)
        if val > largest:
            largest = val
        elif val < smallest:
            smallest = val
    except :
        print("Invalid input")
    
print("Maximum is", largest)
print("Minimum is", smallest)