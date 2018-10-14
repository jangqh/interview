# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:04:58 2018

@author: jangqh

从上到下打印二叉树的每个节点，同层节点从左到由打印
按层遍历
"""

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
  
class Solution:
  def printTreeTopBottom(self, root):
    queue = [] # 里面放节点
    if not root:
      return []
    
    result = []
    queue.append(root)
    while len(queue) > 0:
      currentRoot = queue.pop(0)
      result.append(currentRoot.val)
      if currentRoot.left:
        queue.append(currentRoot.left)
      if currentRoot.right:
        queue.append(currentRoot.right)
    return result


if __name__ == '__main__':
  node1 = TreeNode(8)
  node2 = TreeNode(6)
  node3 = TreeNode(10)
  node4 = TreeNode(5)
  node5 = TreeNode(7)
  node6 = TreeNode(9)
  node7 = TreeNode(11)
  node8 = TreeNode(16)
  
  node1.left = node2
  node1.right = node3
  node2.left = node4
  node2.right = node5
  node3.left = node6
  node3.right = node7
  node6.right = node8
  
  s = Solution()
  result = s.printTreeTopBottom(node1)
  print(result)
  


