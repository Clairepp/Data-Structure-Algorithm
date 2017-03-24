# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        n = number -1
        f = [1,2]
        if (n < 2):
            result = f[n]
        else:
            for i in range(2,n+1):
                f.append(f[i-1]+f[i-2])
            result = f.pop()
        return result
 
x = Solution()
n = int(raw_input())
y = x.jumpFloor(n)
print y

