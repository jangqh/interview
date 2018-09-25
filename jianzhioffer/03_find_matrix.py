# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:25:20 2018

@author: 10144678
"""

class Solution(object):
    def Find(self, array, target):
        if array == []:
            return False
        rownum = len(array)
        colnum = len(array[0])
        
        if type(target) == float and type(array[0][0]) == int:
            if int(target) == target:
                return False
        elif type(target) == int and type(array[0][0]) == float:
            target = float(target)
        elif type(target) != type(array[0][0]):
            return False
        
        i = colnum -1
        j = 0
        
        while i >= 0 and j < rownum:
            if array[j][i] < target:
                j += 1
            elif array[j][i] > target:
                i -= 1
            else:
                return True
        return False
        
array = [[1,2,3,4],[3,4,5,5],[6,7,5,8],[78,76,6,0]]
target = 4.0
s = Solution()
FLAG = s.Find(array, target)
print(FLAG)