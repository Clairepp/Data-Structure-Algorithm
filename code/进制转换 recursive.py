# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,2))
