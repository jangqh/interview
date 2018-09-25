# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 13:41:00 2018

@author: 10144678
"""

"""
输入一个整数n，给出第n项斐波那契数列
1.[a,b] = [0,1]
更新规则，是当i为偶数时，a更新，i为奇数时，b更新

青蛙跳台,每次可以跳一阶，也可以跳两阶
1.
"""

class Solution:
    def Fibonacii(self, n):
        temp_array = [0,1]
        if n > 2:
            for i in range(2, n+1):
                temp_array[i%2] = temp_array[0] + temp_array[1]
        return temp_array[n%2]
    def jumpFloor(self, number):
        temp_array = [1,2]
        if number > 3:
            for i in range(3, number+1):
                temp_array[(i+1)%2] = temp_array[0] + temp_array[1]
        return temp_array[(number+1)%2]


test = Solution()
print(test.Fibonacii(10))
print(test.jumpFloor(10))