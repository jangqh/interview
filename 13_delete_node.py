# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:14:35 2018

@author: 10144678
"""
class ListNode:
    """给定一个单向链表的头指针和一个节点
    """
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None
    
class Solution:
    """
    """
    def delete_node(self, pListHead, pToBeDeleted):
        if not pListHead or not pToBeDeleted:
            return None
        if pToBeDeleted.next != None:
            pNext = pToBeDeleted.next
            pToBeDeleted.val = pNext.val
            pToBeDeleted.next = pNext.next
            pNext.__del__()
            
        elif pToBeDeleted == pListHead:
            pToBeDeleted.__del__()
            pListHead.__del__()
        
        else:
            pNode = pListHead
            while pNode.next != pToBeDeleted:
                pNode = pNode.next
            pNode.next = None
            pToBeDeleted.__del__()



node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(12)
node4 = ListNode(13)
node5 = ListNode(16)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
s.delete_node(node1, node3)
print(node3.val)
print(node2.val)

s.delete_node(node1, node3)
print(node3.val)
print(node2.val)

s.delete_node(node1, node1)
print(node1.val)

s.delete_node(node1, node1)
print(node1.val)
