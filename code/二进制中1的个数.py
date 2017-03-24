
#输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        l = []
        if (n < 0):
            n = 2**32 + n
        while n>0:
            num = n % 2
            l.append(num)
            n = n //2
             
        count = 0
        for i in range(len(l)):
            if (l[i] == 1):
                count += 1
        return count
