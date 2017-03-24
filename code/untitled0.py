#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:02:36 2017

@author: claire
"""

class Solution():
        
    def isReverse(self,num):
        if num < 0:
            return False
        p = 0
        m = num
        while num>0:
            p = p*10 + num%10
            num //= 10      
        if (p == m):
            return True
        else:
            return False
        
    
x = Solution()
y = x.isReverse(0)
print(y)