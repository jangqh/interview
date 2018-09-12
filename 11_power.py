# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:18:52 2018

@author: 10144678
"""

"""
给定一个double类型的浮点数base和一个int类型的exponent，求base的exponent次方
1.当指数为负数时
2.当底数为0，,指数为负数时
3.在判断底数base是不是等于0的时候，不能直接写base == 0，因为计算机表示是有误差的

4.n为偶数时，a^n = a^(n/2) * a^(n/2)
5.n为奇数时，a^n = a^((n-1)/2) * a^((n-1)/2) * a
6.
"""

class Solution:
    def power(self, base, exponent):
        if base == 0.0 and exponent  == 0:
            return 1
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1 and base != 0:
            return 1/base

        result = self.power(base, exponent >> 1) 
        result *= result
        if exponent & 0x1 == 1:
            result *= base
        return result
        
s = Solution()
print(s.power(2,10))