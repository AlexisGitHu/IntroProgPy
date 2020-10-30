# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 19:02:02 2020

@author: Alexis Gómez Chimeno
"""

def factorial(x):
    aux = 1
    for i in range(x,1,-1):
        aux = aux*i
    return aux

print(factorial(5))