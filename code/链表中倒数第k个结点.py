# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 

# 输入一个链表，输出该链表中倒数第k个结点。

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return None
        alist = []
        while head.next != None:
            alist.append(head)
            head = head.next
        alist.append(head)
        if k > len(alist) or k == 0:
            return None
        else:
            return alist[-k]
