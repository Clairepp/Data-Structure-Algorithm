# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, root):
        if not root:
            return []
        stack, temp, res, flag = [root], [], [], 1
        while stack:
            for i in xrange(len(stack)):
                node = stack.pop(0)
                temp += [node.val]
                if node.left:
                    stack += [node.left]
                if node.right:
                    stack += [node.right]
            res += [temp[::flag]]
            temp = []
            flag *= -1
        return res
                 
        
