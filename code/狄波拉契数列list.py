# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。 n<=39

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        fib = [0,1]
        if (n < 2):
            f = fib[n]
        else:
            for i in range(2,n+1):
                fib.append(fib[i-1]+fib[i-2])
            f = fib.pop()
        return f
 
x = Solution()
n = int(raw_input())
y = x.Fibonacci(n)
print y
