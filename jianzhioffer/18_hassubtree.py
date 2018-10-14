# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:30:38 2018

@author: 10144678

输入两颗二叉树A，B，判断B是不是A的子结构
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """返回 True or false
    """
    def hasSubTree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.doesTree1HasTree2(pRoot1, pRoot2)
            if not result:
                result = self.hasSubTree(pRoot1.left, pRoot2)
            if not result:
                result = self.hasSubTree(pRoot1.right, pRoot2)
        return result
        
    def doesTree1HasTree2(self, pRoot1, pRoot2):
        """用于递归判断树的每个节点是否相同
        需要注意的地方是：前面两个if语句可以颠倒顺序
        如果颠倒顺序，会
        """
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        result = self.doesTree1HasTree2(pRoot1.left, pRoot2.left) and \
                self.doesTree1HasTree2(pRoot1.right, pRoot2.right)
        return result

        
if __name__ == '__main__':
    pRoot1 = TreeNode(8)
    pRoot2 = TreeNode(8)
    pRoot3 = TreeNode(7)
    pRoot4 = TreeNode(9)
    pRoot5 = TreeNode(2)
    pRoot6 = TreeNode(4)
    pRoot7 = TreeNode(7)
    
    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot5.left = pRoot6
    pRoot5.right  = pRoot7
    
    pRoot8 = TreeNode(8)
    pRoot9 = TreeNode(9)
    pRoot10 = TreeNode(2)
    
    pRoot8.left = pRoot9
    pRoot8.right = pRoot10
    
    s = Solution()
    print(s.hasSubTree(pRoot1, pRoot8))