# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
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
