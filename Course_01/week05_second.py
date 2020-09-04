# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:54:41 2020

@author: Tohid Fahim
"""

score = input("Enter Score : ")
score = float(score)

if score > 1.0 or score < 0.0 :
    print("Out Of Range")

else :
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")