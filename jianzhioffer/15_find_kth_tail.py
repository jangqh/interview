# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 08:43:10 2018

@author: 10144678
"""

"""
输入一个链表，输出该链表的倒数第k个节点
-- 设置两个指针：
- 第一个指针先走k-1步，第二个指针开始从头结点走
- 第一个指针指向尾节点时，第二个指针正好指向倒数第k个节点
-- 推广：寻找中间节点
-  两个指针一起，第一个指针每次走两步，第二个指针每次走一步
- 快指针指向尾部时，满指针指向中间节点
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def findKthToTail(self, head, k):
        if head == None or k < 0:
            return None
        phead = head
        pbehind = None
        
        for i in range(k-1):
            if phead.next != None:
                phead = phead.next
            else:
                return None
        pbehind = head
        while phead.next != None:
            phead = phead.next
            pbehind = pbehind.next
        return pbehind

if __name__ == '__main__':
    value = [10,11,12,13,14,15]
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(12)
    node4 = ListNode(16)
    node5 = ListNode(18)
    node6 = ListNode(21)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    
    s = Solution()
    d = s.findKthToTail(node1, 3)
    print()
    print(d.val)
        