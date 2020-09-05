# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 22:31:09 2020

@author: Tohid Fahim
"""

st1 = "Tohid "
st2 = "Fahim"
st3 = st1 + st2

print(st3)
print(st1[0])
print(len(st3))


for i in st1:
    print(i)
    
    
print(st3[0:6])
print('T' in st1)

if 'ahi' in st3:
    print("Found It")


print(st3.lower())
print(st3.upper())
print(st3.find('hi'))
st4 = st3.replace('hi', 'hhhhhhhhhhhiiiiiiiiiiiiiiii')
print(st4)


#..........................................................................................................
new = "                   TH FM                       "
print(new.lstrip())
print(new.rstrip())
print(new.strip())

#...........................................................................................................
em = "fd.  tohidfahim3110@gmail.com atc 12-34-56.56"

email = em.find('@')
print(email)
email_last = em.find('.',email)
print(email_last)

print(em[email+1:email_last])



