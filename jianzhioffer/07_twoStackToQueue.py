# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:06:12 2018

@author: 10144678
"""

"""
1.定义两个栈，列表
2.往第一个栈push元素，10,12,123
3.pop时，判断第二个栈是否为空，如果为空，则把第一个栈的元素加入第二个栈（列表），返回最上面的元素
如果不为空，则跳过，直接输出最上面的元素
4.再压入元素进入第一个栈，pop时，判断第二个栈是否为空，重复2

程序有错误，不知为啥？？？
AttributeError: 'Solution' object has no attribute 'stack1'
已解决：由于__init__函数写成了 _init__，少了一个下划线
"""
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def pushh(self, node):
        self.stack1.append(node)
    def popp(self):
        if len(self.stack2) == 0 and len(self.stack1) == 0:
            return
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


p = Solution()
p.pushh(10)
p.pushh(12)
p.pushh(123)
print(p.popp())
print(p.popp())
p.pushh(146)
print(p.popp())
print(p.popp())
print(p.popp())
print(p.popp())
p.pushh([1,2,3,4,5])
print(p.popp())