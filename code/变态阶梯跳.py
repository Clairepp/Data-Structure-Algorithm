# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        n = number - 1
        f = 2 ** n
        return f
x = Solution()
n = int(raw_input())
y = x.jumpFloorII(n)
print y
