# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:59:05 2016

@author: ericgrimson
"""

def f( x ):
    x = x + 1
    print('in f(x): x =', x)
    return x

x = 3
z = f( x )
print("The value of x outside the function f is:", x)
print("The value of z is:", z)
