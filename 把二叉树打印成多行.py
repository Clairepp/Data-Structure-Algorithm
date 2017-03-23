# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, root):
        if not root: return []
        res, temp, stack =[], [], [root]
        while stack:
            for i in xrange(len(stack)):
                node=stack.pop(0)
                temp+=[node.val]
                if node.left: stack+=[node.left]
                if node.right: stack+=[node.right]
            res+=[temp[::1]]
            temp=[]
        return res        
        
        
