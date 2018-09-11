# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:18:39 2018

@author: 10144678
"""

"""
输入某个二叉树的前序遍历和中序遍历，重建该二叉树
假设输入的前序遍历和中序遍历的结果都不含重复的数字
例如输入的前序遍历序列{1,2,4,7,3,5,6,8}， 中序遍历{4,7,2,1,5,3,8,6}， 重建二叉树

1.前序的第一个就是根节点root
2.在中序序列中找到前序序列第一个数的位置i
3.递归调用函数，前序：前序的第二个到第i个，中序：中序的前i个
4.递归结束的条件：前序与中序序列中元素有不一样的时候，或者前序和中序为None时
5.层次打印出来：
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """返回构造的TreeNode根节点
    """
    def reCoustructBinarayTree(self, pre, tin):
        if not pre and not tin:
            return None
        root = TreeNode(pre[0])
        if set(pre) != set(tin):
            return None
        
        i = tin.index(pre[0])
        root.left = self.reCoustructBinarayTree(pre[1:i+1], tin[:i])
        root.right = self.reCoustructBinarayTree(pre[i+1:], tin[i+1:])
        return root
        
        


pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
test = Solution()
newTree = test.reCoustructBinarayTree(pre, tin)


def PrintNodeAtLevel(treeNode, level):
    """层次遍历输出树种一层的值
    """
    if not treeNode or level < 0:
        return 0
    if level == 0:
        print(treeNode.val)
        return 1
    PrintNodeAtLevel(treeNode.left, level-1)
    PrintNodeAtLevel(treeNode.right, level-1)


def PrintNodeByLevel(treeNode, depth):
    for level in range(depth):
        print("level:", level)
        PrintNodeAtLevel(treeNode, level)

# 不知道树深 直接按层次遍历输出
def PrintNodeByLevel2(treeNode):
    level = 0
    while 1:
        print("level", level)
        if not PrintNodeAtLevel(treeNode, level):
            break
        level += 1
        


PrintNodeByLevel(newTree, 5)
PrintNodeByLevel2(newTree)