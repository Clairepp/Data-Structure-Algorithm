# 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        else:
            return self.isMirror(pRoot.left,pRoot.right)
          
    def isMirror(self,left,right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif (left.val == right.val):
            tleft = self.isMirror(left.left,right.right)
            tright = self.isMirror(left.right,right.left)
            return tleft and tright
        else:
            return False
            
            
