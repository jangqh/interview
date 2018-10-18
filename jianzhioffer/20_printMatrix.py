# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:30:58 2018

@author: jangqh
"""

"""
输入一个矩阵，按照从外向内顺时针打印
[[1,2,3,4],
[12,13,14,5],
[11,16,15,6],
[10,9,8,7]]
"""

class Solution:
    def printMatrix(self, matrix):
        printArr = []
        if matrix == None:
            return
        if matrix == []:
            return []
        start = 0
        


if __name__ == '__main__':
    matrix = [[1,2,3,4],
              [12,13,14,5],
              [11,16,15,6],
              [10,9,8,7]]
    matrix2 = [[1],[2],[3],[4],[5],[6]]
    matrix3 = [[1,2],[3,4]]
    s = Solution()
    print(s.printMatrix(matrix))
    print(s.printMatrix(matrix2))
    print(s.printMatrix(matrix3))