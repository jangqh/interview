# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:36:03 2018

@author: 10144678
"""

"""
输入一个链表。从尾到头打印链表
"""
class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next  =None

class Solution():
    def printListFromTailToHead(self, listNode):
        if listNode.val == None:
            return
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l
            

#1. 多个节点
node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(17)
node5 = ListNode(20)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

#2. 一个节点
singleNode = ListNode(12)

#3.无节点
test = ListNode()

s = Solution()
print(s.printListFromTailToHead(node1))
print(s.printListFromTailToHead(singleNode))
print(s.printListFromTailToHead(test))