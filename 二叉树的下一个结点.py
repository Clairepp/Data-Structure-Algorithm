# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
# -*- coding:utf-8 -*-

# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            t = pNode.right
            while t.left:
                t = t.left
            return t
        else:
            t = pNode
            if not t.next:
                return None
            while t != t.next.left:
                t = t.next
                if not t.next:
                    return None
            return t.next
        return None
        
        
