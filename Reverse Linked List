# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, head):
        if not head:
            return None
        alist = []
        while head.next != None:
            alist.append(head)
            head = head.next
        alist.append(head)
        return alist[::-1]
