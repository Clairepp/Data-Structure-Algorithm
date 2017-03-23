# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        for i in range(len(array)-1,0,-1):
            for j in range(i):
                if (array[j]%2 == 0 and array[j+1]%2 == 1):
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array
