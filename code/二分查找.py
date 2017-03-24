#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 18:05:48 2017

@author: claire
"""


def BinarySearch(alist,k):
    if not alist:
        return False
    else:
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid+1:]
        if (k == alist[mid]):
            return True
        else:
            if (k > alist[mid]):
                 return BinarySearch(right,k)
            else:
                return BinarySearch(left,k)
    
    
alist = [1,3,5,7,9,11,13,15,17]
print(BinarySearch(alist,5))
print(BinarySearch(alist,80))
