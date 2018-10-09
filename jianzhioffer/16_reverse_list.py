# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:33:32 2018

@author: 10144678
"""

"""
输入一个链表，输出反转之后的所有元素
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse_list(self, phead):
        """ListNode
        """
        pReverseHead = None
        pNode = phead
        pPrev = None
        while pNode != None:
            pNext = pNode.next
            if pNext == None:
                pReverseHead = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReverseHead

    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            newHead=self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next=None
            return newHead

    def print_nodelist(self, phead):
        while phead != None:
            print(phead.val, end=' ')
            phead = phead.next
        
if __name__ == '__main__':
    """
    """
    node1 = ListNode(10)
    node2 = ListNode(13)
    node3 = ListNode(15)
    node4 = ListNode(19)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    s = Solution()


    p1 = s.ReverseList(node1)
    s.print_nodelist(p1)
    print(p1)
    
    p = s.reverse_list(node1)
    s.print_nodelist(p)
    print(p)