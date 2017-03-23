#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 21:47:26 2017

@author: claire
"""
# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class Solution:
    # array 二维列表
    def Find(self, target, array):
        ncol = len(array[0])
        nrow = len(array)
        nr = nrow - 1
        nc = 0
        while (nr >= 0) and (nc < ncol ):
                key = array[nr][nc]
                if (target == key):
                    return True
                elif (target > key):
                    nc += 1
                else:
                    nr -= 1
        return False

a = [[1, 2, 8, 9],
     [2, 4, 9, 12],
     [4, 7, 10, 13],
     [6, 8, 11, 15]]
x = Solution()
y = x.Find(14,a)
print (y)
y = x.Find(7,a)
print (y)
y = x.Find(0,a)
print (y)
        
