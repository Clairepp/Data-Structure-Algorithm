# 输入一个链表，从尾到头打印链表每个节点的值。

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        result = []
        while listNode:
            result.append(listNode.val)
            listNode = listNode.next
        return result[::-1]
         
